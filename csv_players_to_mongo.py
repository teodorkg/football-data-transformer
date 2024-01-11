import os
import pandas as pd
from urllib.parse import quote_plus
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class Player:
    def __init__(self, player_info, valuations):
        for key, value in player_info.items():
            setattr(self, key, value)
        setattr(self, 'valuations', valuations)

    def to_dict(self):
        return self.__dict__

username = quote_plus('common')
password = quote_plus(os.environ.get('MONGODB_PASSWORD'))
uri = f"mongodb+srv://{username}:{password}@playervaluations.v7jevdf.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['player_valuations']
collection = db['players']

players_df = pd.read_csv('raw_data\\transfermarkt\\players.csv')
valuations_df = pd.read_csv('raw_data\\transfermarkt\\player_valuations.csv')

grouped_valuations = valuations_df.groupby('player_id').apply(lambda x: x.to_dict('records'))

# Process each player
for index, row in players_df.iterrows():
    player_id = row['player_id']
    player_info = row.to_dict()
    valuations = grouped_valuations.get(player_id, [])
    player = Player(player_info, valuations)
    collection.insert_one(player.to_dict())

client.close()