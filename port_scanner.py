import socket

class PortScanner:
    def __init__(self, target):
        self.target = target
        self.ports = [80, 443, 22, 21, 25, 110, 8080]

    def scan_ports(self):
        open_ports = []
        for port in self.ports:
            if self.is_port_open(port):
                open_ports.append(port)
        return open_ports

    def is_port_open(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target, port))
            sock.close()
            return result == 0
        except socket.error:
            return False
