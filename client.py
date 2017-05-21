# Python program to implement client side of chat room.
import socket
import select
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


def sendSequence(message):
    m = message.split("-")
    name = m[0]
    if name == NAME:
        seq = m[1].split(",")
        print name
        print seq


while True:
    sockets_list = [sys.stdin, server]
    read_sockets, write_socket, error_socket = select.select(sockets_list,[],[])

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            sendSequence(message)


server.close()
