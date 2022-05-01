import sys
import socket


HOST = "192.168.119.141"
PORT = 3000


def test():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        result = s.connect_ex((HOST, PORT))
        if result == 0:
            print("Port open")
        else:
            print("Port closed")


if __name__ == '__main__':
    sys.exit(test())

