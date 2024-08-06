import unittest
from web_enumeration import WebEnumeration

class TestWebEnumeration(unittest.TestCase):
    def test_run(self):
        tool = WebEnumeration('example.com')
        tool.run()
        # Assert that no exception is raised

if __name__ == '__main__':
    unittest.main()
