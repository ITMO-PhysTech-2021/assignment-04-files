import json
import sys
import multiprocessing
import socket
import time

HOST = '127.0.0.1'
PORT = 65432


def run_receiver():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            ...
    ...


def run_sender(obj):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        ...
