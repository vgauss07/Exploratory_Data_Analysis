#!/usr/bin/env/ python3
import requests
# To check whether the local host is correctly configured
import socket


def check_localhost(localhost):
    # This functions checks whether local host is correctly configured
    localhost = socket.gethostbyname('localhost')
    if localhost == '127.0.0.1':
        return True
    else:
        return False


def check_connectivity():
    request = requests.get("http://www.google.com")
    if request == '200':
        return True
    else:
        return False
