import unittest
from port_scanner import PortScanner

class TestPortScanner(unittest.TestCase):
    def test_scan_ports(self):
        scanner = PortScanner('127.0.0.1')
        open_ports = scanner.scan_ports()
        self.assertIsInstance(open_ports, list)

if __name__ == '__main__':
    unittest.main()
