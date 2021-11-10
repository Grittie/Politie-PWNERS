import re
import time
import json

from requests.auth import HTTPBasicAuth
import requests

with open('data.txt') as file:
    for line in file:
        text_line = line.rstrip()
        spl = ":"
        email = text_line.partition(spl)[0]

        method = "get"
        url =  'https://haveibeenpwned.com/api/v3/breachedaccount/' + email
        header = { 
            'hibp-api-key' :'ADD_KEY_HERE'
        }

        rsp = requests.request(method, url, headers=header)
        json_data = rsp.content

        json_array = json.loads(json_data)
        store_list = []

        print(email + " has been pwned by:")
        for item in json_array:            
            item = json.dumps(item)
            
            name = item.partition(spl)[2]
            print(name[:-1])
        
        print()
        time.sleep(2)