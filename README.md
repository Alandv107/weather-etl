# Weather Data ETL Pipeline

This project fetches, cleans, merges and stores weather and PM2.5 data from MongoDB into MySQL.

## Features

- Time-based MongoDB ObjectId data slicing
- Weather and PM2.5 cleaning by hour and city
- AM/PM data merging
- Automatic table appending into MySQL

## Technologies

- Python
- MongoDB / PyMongo
- Pandas / NumPy / SciPy
- SQLAlchemy
- dotenv

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Edit your .env with actual credentials
