"""
Module responsible for fetching animal data from the API.
"""

import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_KEY")


def fetch_data(animal_name):
    """
    Fetches animal data from the API based on the provided animal name.

    Parameters:
        animal_name (str): The name of the animal to search for.

    Returns:
        list: A list of dictionaries, each representing an animal.
    """
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    try:
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print("Error fetching data:", error)
        return []
