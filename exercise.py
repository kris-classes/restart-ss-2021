'''
Password strength as a Service
PSaaS

A user can send a password and we tell them whether it is a good password or not.
User can also send a word and we give them the MD5 hash.

TODO: Check password against list of common passwords.
TODO: Create a log file of clients who connected.


Connect to it using netcat with the command:
    nc localhost 12345

'''

import hashlib
import socket
import random
import time

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to localhost and port 12345
server_socket.bind(("localhost", 12345))

# Listen on the port for incoming connections
server_socket.listen()

# Clients must now send data
print("Waiting for connections...")

# Accept connection from client
(client, addr) = server_socket.accept()
print("Client connected\n", addr)

# Receive data
input_data = client.recv(1024)
print(f'Received data: {input_data}')

# Hash the data using MD5
print('Hashing user input.')
password_hash = hashlib.md5(input_data)

# Get the hex digest of the password hash (returns a string)
password_hex_digest = password_hash.hexdigest()
print('Generated hash: ', password_hex_digest)

# Encode the password (defaults to UTF-8) before sending it as bytes.
password_hex_digest_encoded = password_hex_digest.encode()

# Convert it to bytes before sending it back to client
password_digest_as_bytes = bytes(password_hex_digest_encoded)

# Send the response back
print('Sending response')
client.send(password_digest_as_bytes)

# Close the client socket
print('Closing client socket')
client.close()

# Close the server socket
print('Closing server socket')
server_socket.close()

# End the program
print('Exiting')
