import sys
from client.client import Client

def main():
    msg = sys.argv[1]
    client = Client()
    client.send(msg)

main()