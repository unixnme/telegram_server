# telegram_server

## Install
python setup.py install

## Tutorial
### 1. Run the server
> $ python -m server TOKEN CHAT_ID <br>

where TOKEN is the telegram bot token and CHAT_ID is the receiver's id

### 2a. Send the message from terminal
> $ python -m client 'hello'

### 2b. Send a message from code
> from client.client import Client <br>
> client = Client() <br>
> client.send("hello")
