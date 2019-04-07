import argparse
import sys
from client.client import Client

def main():
    parser = argparse.ArgumentParser('Telegram client')
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--port', type=int, default=9876)
    parser.add_argument('msg', type=str, help='msg to send')
    args = parser.parse_args()

    client = Client(args.host, args.port)
    client.send(args.msg)

main()
