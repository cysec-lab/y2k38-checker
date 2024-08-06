import json

import urllib.request


class Client:
    def __init__(self):
        pass

    def send_to_server(self, json_data: str):
        url = "http://example.com/api"
        data = json.dumps(json_data).encode('utf-8')
        headers = {'Content-Type': 'application/json'}
        req = urllib.request.Request(url, data=data, headers=headers)
        response = urllib.request.urlopen(req).read().decode('utf-8')
        print(response)
        return response
