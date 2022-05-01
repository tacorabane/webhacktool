import sys
import argparse


def start(args):
    if args is None:
        raise Exception('Issue with args !')
    else:
        print("Start...")


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('-h', '--host',
                        type=str,
                        help='Specify the target host')
    parser.add_argument('-p', '--port',
                        type=int,
                        default=80,
                        help='Specify the port of the target host. 80 by default')
    args = parser.parse_args()
    sys.exit(start(args))


if __name__ == '__main__':
    sys.exit()
