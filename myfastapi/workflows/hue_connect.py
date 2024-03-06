import requests
import json
import os
from myfastapi.modules.pyhuey_logger import configuration as logging_configuration
import logging
import time
logging_configuration()

app_name = (os.path.basename(__file__)).rstrip('.py')
vault_name = "Automation"
hue_token = os.getenv('hue_token')

def discover():
    response = requests.get("https://discovery.meethue.com")
    # hue_bridge_ip = json.loads(response.text)[0]['internalipaddress']
    return response.text

def create_hue_user_name(hue_bridge_ip):
    response = requests.post(f'http://{hue_bridge_ip}/api', data={"devicetype": {app_name}})
    return response.json()

def setup(hue_bridge_ip):
    wait_time = int(60) # seconds
    start_increment = int(0) # start at 0 seconds
    logging.info("please push the button on top of your hue bridge.")
    logging.info("this process can take up to a minute please be patient")
    while start_increment <= wait_time:
        response_data = create_hue_user_name(hue_bridge_ip)
        if 'error' in response_data:
            print('-----> True')
            if response_data[0]['error']['description'] == 'link button not pressed':
                print('Please press the link button')
                time.sleep(10)
                start_increment += 10
            else:
                print(f"Error: {response_data[0]['error']['description']}")
                exit()
        elif 'success' in response_data:
            user_name = response_data[0]['success']['username']
            print(f"API key (usename) successfully generated {user_name}")
            return user_name
        else:
            print('unknown response format.')
            return None



if __name__ == "__main__":
    my_hue_bridge_ip = discover()
    print(f'------> {my_hue_bridge_ip}')
    # print(push_hue_bridge_button(my_hue_bridge_ip))
    # get_hue_user_name()
    ## TODO: Setup 1password API to hold key and other creds