#!/usr/bin/python
# Python program to implement client side of chat room.
import socket
import select
import time
import pigpio
import sys

if len(sys.argv) != 3:
    print "Correct usage: script, IP address, port number"
    exit()

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])

file = open("/home/pi/pi_name", "r")
pi_name = file.readline(1)
pi = pigpio.pi()

NAME = "PI_" + pi_name
RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 24

bright = 255
r = 255.0
g = 0.0
b = 0.0

def setLights(pin, brightness):
    realBrightness = int(int(brightness) * (float(bright) / 255.0))
    pi.set_PWM_dutycycle(pin, realBrightness)


def setLed(newR, newG, newB):
    setLights(RED_PIN, newR)
    setLights(GREEN_PIN, newG)
    setLights(BLUE_PIN, newB)


def sendSequence(message):
    if message == NAME:
        print(message)
        setLed(81.0, 23.0, 52.0)
        time.sleep(0.5)
        setLed(22.0, 123.0, 83.0)
        time.sleep(0.5)
        setLed(0, 0, 0)


setLed(255.0, 255.0, 255.0)
time.sleep(0.2)
setLed(0, 0, 0)
time.sleep(10)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((IP_address, Port))

while True:
    sockets_list = [sys.stdin, server]
    read_sockets, write_socket, error_socket = select.select(sockets_list,[],[])

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            server.send(NAME + " received message")
            sendSequence(message)


server.close()
