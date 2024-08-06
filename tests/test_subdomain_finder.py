import unittest
from subdomain_finder import SubdomainFinder

class TestSubdomainFinder(unittest.TestCase):
    def test_find_subdomains(self):
        finder = SubdomainFinder('example.com')
        subdomains = finder.find_subdomains()
        self.assertIsInstance(subdomains, list)

if __name__ == '__main__':
    unittest.main()
