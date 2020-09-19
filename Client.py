import requests

class Client:
    def get(self, url):
        response = requests.get(url)

        if(response.status_code == 200):
            return response

