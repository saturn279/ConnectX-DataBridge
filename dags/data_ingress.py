import requests
import logging

API_ENDPOINT = 'http://api_server/api/products'

def fetch_data():
    try:
        response = requests.get(API_ENDPOINT, headers={"Content-Type": "application/json"})
        response.raise_for_status()
        api_data = response.json()
        return api_data
    except Exception as e:
        logging.error(f"Error occurred while calling API: {e}")
        return None
