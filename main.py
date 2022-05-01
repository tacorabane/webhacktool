import sys
import argparse
import Recon


def start(args):
    if args is None:
        raise Exception('Issue with args !')
    else:
        print("Start...")
        r = Recon.Recon(args.host, args.port)
        r.scan()


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
    if args.port is None:
        raise Exception('You should specify a target IP address or URL')
    sys.exit(start(args))


if __name__ == '__main__':
    sys.exit()
