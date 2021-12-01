# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:27:25 2021

@author: weenf
"""
import json
from database import hobbies
from socket import socket, AF_INET, SOCK_STREAM
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("localhost", 54321))
server_socket.listen()



client, address = server_socket.accept()
data = client.recv(1000)

print(f"client sent us {data}")
f = open("website.html", "rb")
html = f.read()
client.send(b"HTTP/1.1 200 OK\n\n")
client.send(html)
f.close()
#client.send(b"<h1> hello</h1>")
#client.send(b"<input type='text' />")
#client.send(b"<input type='submit' label='button' /> ")
#hobbies_json = json.dumps(hobbies)
#client.send(bytes(hobbies_json.encode()))
client.close()
server_socket.close()
print("exiting")
