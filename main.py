import sys
import argparse
import Recon


def start(args):
    if args is None:
        raise Exception('Issue with args !')
    else:
        print("Start...")
        r = Recon.Recon(args.url, args.port)
        r.scan()
        if r.get_is_open():
            # Starting the scanning of the web page
        else:
            print(f"Nothing to do with {args.url}:{args.port}")


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url',
                        type=str,
                        help='Specify the target host')
    parser.add_argument('-p', '--port',
                        type=int,
                        default=80,
                        help='Specify the port of the target host. 80 by default')
    args = parser.parse_args()
    if args.url is None:
        raise Exception('You should specify a target IP address or URL')
    sys.exit(start(args))


if __name__ == '__main__':
    sys.exit(run())
