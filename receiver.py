#!/usr/bin/env python
import socket
import numpy as np
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument(
    "-src",
    type=str,
    help=
    "IP address of the computer performing the object detection ex: 192.169.0.1"
)
args = vars(ap.parse_args())

host = args["src"]
#IP address of computer that is broadcasting
port = 10000
buf = 1024
addr = (host, port)
fName = 'img.jpg'
timeOut = 0.05


def foo():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('', port))
        f = open(fName, 'wb')

        data, address = s.recvfrom(buf)
        try:
            while (data):
                f.write(data)
                s.settimeout(timeOut)
                data, address = s.recvfrom(buf)
        except:
            f.close()
            s.close()


if __name__ == '__main__':
    foo()
