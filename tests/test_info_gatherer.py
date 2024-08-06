

from unittest.mock import patch, Mock
import unittest
from info_gatherer import InfoGatherer

class TestInfoGatherer(unittest.TestCase):
    @patch('info_gatherer.requests.get')
    def test_gather_info(self, mock_get):
        mock_response = Mock()
        mock_response.headers = {'Content-Type': 'text/html'}
        mock_get.return_value = mock_response

        gatherer = InfoGatherer('example.com')
        info = gatherer.gather_info()
        self.assertIsInstance(info, dict)
        self.assertEqual(info['Content-Type'], 'text/html')

if __name__ == '__main__':
    unittest.main()
