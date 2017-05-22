# Python program to implement client side of chat room.
import socket
import select
import time
import json
import pigpio
import sys

file = open("pi_name", "r")
pi_name = file.readline(1)
NAME = "PI_" + pi_name

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print "Correct usage: script, IP address, port number"
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))


def pattern():
    pigpio(81, 23, 52)
    time.sleep(1)
    pigpio(0, 0, 0)


def sendSequence(message):
    if message == NAME:
        print(message)
        pattern()


while True:
    sockets_list = [sys.stdin, server]
    read_sockets, write_socket, error_socket = select.select(sockets_list,[],[])

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            server.send(NAME + " received message")
            sendSequence(message)


server.close()
