import requests

class InfoGatherer:
    def __init__(self, target):
        self.target = target

    def gather_info(self):
        try:
            response = requests.get(f"http://{self.target}")
            headers = response.headers
            return headers
        except requests.ConnectionError:
            return "Unable to gather information"
