import requests
import json
import os
from pyhuey_logger import configuration as logging_configuration
import logging
logging_configuration()

app_name = (os.path.basename(__file__)).rstrip('.py')
vault_name = "Automation"

def get_hue_user_name():
    pass

def discover():
    response = requests.get("https://discovery.meethue.com")
    hue_bridge_ip = (json.loads(response.text)[0]['internalipaddress'])['ip']
    return hue_bridge_ip

def make_hue_user_name(hue_bridge_ip):
    response = requests.post(f'{hue_bridge_ip}/api', json={"devicetype": {app_name}})
    return response.json()

def push_hue_bridge_button():
    wait_time = int(60) # seconds
    start_increment = int(0) # start at 0 seconds
    logging.info("please push the button on top of your hue bridge.")
    logging.info("this process can take up to a minute please be patient")
    get_hue_user_name(vault_name)
    while start_increment < wait_time:

def get_user_name(vault_name):
    
    if not user_name:
        logging.info("user name found")
        return user_name
    else:
        logging.info("User name found")
        return "not found"
# def wait_for_button_push(event):
#     if 'error' in response_data


    return "foo"

if __name__ == "__main__":
    my_hue_bridge = discover()
    # get_hue_user_name()
    ## TODO: Setup 1password API to hold key and other creds