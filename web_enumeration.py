import argparse
from port_scanner import PortScanner
from subdomain_finder import SubdomainFinder
from info_gatherer import InfoGatherer

class WebEnumeration:
    def __init__(self, target):
        self.target = target

    def run(self):
        self.enumerate_ports()
        self.enumerate_subdomains()
        self.gather_info()

    def enumerate_ports(self):
        scanner = PortScanner(self.target)
        open_ports = scanner.scan_ports()
        print(f"Open ports for {self.target}: {open_ports}")

    def enumerate_subdomains(self):
        finder = SubdomainFinder(self.target)
        subdomains = finder.find_subdomains()
        print(f"Discovered subdomains for {self.target}: {subdomains}")

    def gather_info(self):
        gatherer = InfoGatherer(self.target)
        info = gatherer.gather_info()
        print(f"Information about {self.target}: {info}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Web Enumeration Tool')
    parser.add_argument('target', help='Target domain or IP address')
    # args = parser.parse_args()
    target = input("Enter target website: ")
    tool = WebEnumeration(target)
    tool.run()
