'''
Password strength as a Service
PSaaS

A user can send a password and we tell them whether it is a good password or not.
User can also send a word and we give them the MD5 hash.

TODO: Check password against list of common passwords.
TODO: Create a log file of clients who connected.

'''

import hashlib
import socket
import random
import time

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket
server_socket.bind(("localhost", 12345))

# Listen on the port
server_socket.listen()

# Clients must send data
print("Waiting for connection...")

# Accept connection from client
(client, addr) = server_socket.accept()
print("Client connected\n", addr)

# Receive data
input_data = client.recv(1024)

# hash = hashlib.md5(b'password').hexdigest()

# Hash the data using MD5
# Send the response back
client.send(b'input data received')

# Close the client socket
client.close()
# Close the server socket
server_socket.close()

# End the program
