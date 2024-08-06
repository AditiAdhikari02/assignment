import requests

class SubdomainFinder:
    def __init__(self, target):
        self.target = target
        self.subdomains = ['www', 'mail', 'ftp', 'blog', 'dev']

    def find_subdomains(self):
        discovered_subdomains = []
        for subdomain in self.subdomains:
            url = f"http://{subdomain}.{self.target}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    discovered_subdomains.append(url)
            except requests.ConnectionError:
                continue
        return discovered_subdomains
