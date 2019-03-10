import argparse
import socketserver
from server.server import MyTCPHandler
from telegram import Bot

def start_server():
    parser = argparse.ArgumentParser('Telegram server')
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--port', type=int, default=9876)
    parser.add_argument('token', type=str, help='telegram bot token')
    parser.add_argument('id', type=str, help='receiver telegram id')
    args = parser.parse_args()

    bot = Bot(args.token)
    handler = MyTCPHandler
    handler.bot = bot
    handler.chat_id = args.id

    with socketserver.TCPServer((args.host, args.port), handler) as server:
        server.serve_forever()

start_server()