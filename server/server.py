import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    bot = None
    chat_id = None

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print(self.data)

        self.bot.send_message(chat_id=self.chat_id, text=self.data.decode())

        # just send back the same data, but upper-cased
        self.request.sendall(str.encode("ok"))