# !/usr/bin/python3.10
from test_gen import select_file, user_dict_and_container, recpy_callback
import os

directory = os.getcwd()
file = select_file()

with open(file, 'r') as rfile:
    read_file = rfile.read()

importpy = '#importpy'

active_body = read_file
while True:
    if importpy in active_body:
        str_remove, container, user_dict = user_dict_and_container(active_body, importpy)

        import_str = recpy_callback(container,active_body)

        active_body = active_body.replace(str_remove, import_str)

    else:
        break

with open(file, 'w') as wfile:
    wfile.write(active_body)
