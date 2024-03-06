import requests
import os
from myfastapi.modules.pyhuey_logger import configuration as logger_configuration
import logging
logger_configuration()

logger = logging.getLogger(__name__)

# Set up authentication
headers = {
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
    'Content-Type': 'application/json',
}

def get_password():
    print(f'PWTOKEN = {os.getenv("PWTOKEN")}')
    try:
        if os.getenv('PWTOKEN'):
            print("stuff")
            logger.error(f"PWTOKEN is {os.getenv('PWTOKEN')}")
        else:
            logger.error("PWTOKEN not set")
    except Exception as err:
        logger.error(f"could not find PWTOKEN. Error: {err}")

    
    # Make a GET request to retrieve a secret
    response = requests.get('https://my.1password.com/vaults/VaultID/items/ItemID', headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        secret_data = response.json()
        # Process the secret data as needed
        print(secret_data)
    else:
        print('Error:', response.status_code)
        print(response.text)

if __name__ == "__main__":
    get_password()