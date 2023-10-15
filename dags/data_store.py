from pymongo import MongoClient
import logging

mongo_conn_str = 'mongodb://mongo:27017/'

def store_data(processed_data):
    try:
        client = MongoClient(mongo_conn_str)
        db = client['products_database']
        collection = db['products']

        for record in processed_data:
            collection.insert_one(record)

        client.close()
        logging.info("Data stored in MongoDB successfully.")
    except Exception as e:
        logging.error(f"Error occurred while storing data in MongoDB: {e}")
