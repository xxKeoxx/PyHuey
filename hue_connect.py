import requests
import json
import os
app_name = (os.path.basename(__file__)).rstrip('.py')

{'ip': "", 'user_name': ""}

    def discover(self):
        response = requests.get("https://discovery.meethue.com")
        self.config['ip'] = json.loads(response.text)[0]['internalipaddress']

    def get_hue_user_name(self):
        registration_url = f'http://{hue_bridge_paring.config['ip']}/api'
        data = {"devicetype": {app_name}}

        response = requests.post(registration_url, json=data)
        return response.json()


    # def wait_for_button_push(event):
    #     if 'error' in response_data


        return "foo"

if __name__ == "__main__":
    my_hue_bridge = hue_bridge_paring()
    my_hue_bridge.discover()
    print(my_hue_bridge.get_hue_user_name())
    ## TODO: Setup 1password API to hold key and other creds