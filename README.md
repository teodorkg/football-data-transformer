# Big Data Management Project

## Project Overview
This Big Data Management project demonstrates the ability to handle, transform, and combine large datasets from diverse sources into a coherent and structured format. The project involves sourcing data from MongoDB Atlas, CSV files, and JSON files, processing and transforming this data using PySpark, and finally outputting the integrated data into a Relational Database.

## Data Sources
- **MongoDB Atlas**: NoSQL database hosting unstructured data.
- **CSV Files**: Structured data files containing tabular data.
- **JSON Files**: Semi-structured data files, often used for nested or hierarchical data.

## Key Features
- **Data Extraction**: Implementation of methods to extract data from MongoDB Atlas, CSV, and JSON files.
- **Data Transformation**: Utilization of PySpark for cleaning, transforming, and normalizing data from different formats.
- **Data Integration**: Combining data from multiple sources into a single, unified schema.
- **Output to Relational DB**: Storing the transformed data in a relational database format for further use and analysis.

## Technologies Used
- **PySpark**: For handling and processing big data.
- **MongoDB Atlas**: As a source NoSQL database.
- **Relational Database (e.g., PostgreSQL, MySQL)**: For final data storage.
- **Python**: As the primary programming language.
- **Jupyter Notebook**: For interactive development and documentation.

## Getting Started
### Prerequisites
- Python 3.12
- PySpark
- MongoDB Atlas account
- Relational Database (e.g., PostgreSQL, MySQL)

### Installation
1. Clone the repository: `git clone https://github.com/teodorkg/football-data-transformer.git`
2. Install the required Python packages: `pip install -r requirements.txt`

## Usage
1. **Data Extraction**: Run the scripts to extract data from MongoDB Atlas, CSV, and JSON files.
2. **Data Transformation**: Execute the PySpark notebooks/scripts to perform data transformation.
3. **Data Loading**: Load the transformed data into the chosen relational database.

## Documentation
- The `docs` directory contains detailed documentation of the project.
- The Jupyter Notebook includes comments and explanations for each step of the data transformation process.