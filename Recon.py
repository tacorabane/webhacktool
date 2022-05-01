import socket


class Recon:
    def __init__(self, host=None, port=None):
        self._host = host
        self._port = port
        self._is_open = False

    def set_host(self, host):
        if host is None:
            self._host = input('The host is not correct. Type it again : ')
        else:
            self._host = host

    def get_host(self):
        return self._host

    def set_port(self, port):
        if port is None:
            self._port = input('The port is not correct. Type it again : ')
        else:
            self._port = port

    def get_port(self):
        return self._port

    def set_is_open(self, is_open):
        if is_open is None:
            self._is_open = False
        else:
            self._is_open = True

    def get_is_open(self):
        return self._is_open

    def scan(self):
        if self._host is not None and self._port is not None:
            print(f"Scan on {self.get_host()}:{self.get_port()} started...")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                if s.type == socket.SOCK_STREAM:
                    if s.connect_ex((self.get_host(), self.get_port())) == 0:
                        print(f"{self.get_port()}/TCP\tOPEN\t")
                        self.set_is_open(True)
                    else:
                        print(f"{self.get_port()}/TCP\tCLOSED")
                        self.set_is_open(None)
                elif s.type == socket.SOCK_DGRAM:
                    if s.connect_ex((self.get_host(), self.get_port())) == 0:
                        print(f"{self.get_port()}/UDP\tOPEN")
                        self.set_is_open(True)
                    else:
                        print(f"{self.get_port()}/TCP\tCLOSED")
                        self.set_is_open(None)