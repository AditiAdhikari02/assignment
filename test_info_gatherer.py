import unittest
from unittest.mock import patch, Mock
from your_module import InfoGatherer  # replace 'your_module' with the actual module name

class TestInfoGatherer(unittest.TestCase):
    
    @patch('your_module.requests.get')  # replace 'your_module' with the actual module name
    def test_gather_info_success(self, mock_get):
        # Setup mock response
        mock_response = Mock()
        mock_response.headers = {'Content-Type': 'application/json'}
        mock_get.return_value = mock_response
        
        # Create instance of InfoGatherer
        target = 'example.com'
        info_gatherer = InfoGatherer(target)
        
        # Call the method
        result = info_gatherer.gather_info()
        
        # Assert the result
        self.assertEqual(result, {'Content-Type': 'application/json'})
        mock_get.assert_called_once_with(f"http://{target}")
    
    @patch('your_module.requests.get')  # replace 'your_module' with the actual module name
    def test_gather_info_failure(self, mock_get):
        # Setup mock to raise a ConnectionError
        mock_get.side_effect = requests.ConnectionError
        
        # Create instance of InfoGatherer
        target = 'example.com'
        info_gatherer = InfoGatherer(target)
        
        # Call the method
        result = info_gatherer.gather_info()
        
        # Assert the result
        self.assertEqual(result, "Unable to gather information")
        mock_get.assert_called_once_with(f"http://{target}")

if __name__ == '__main__':
    unittest.main()
