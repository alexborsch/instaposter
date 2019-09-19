import os, shutil
from instapy_cli import client
import time, threading

username = 'login'
password = 'password'
image = 'images/post.jpg'

def instapost():
    with open('images/post.txt', 'r') as file:
        data = file.read().replace('\n', '')
    with client(username, password) as cli:
        cli.upload(image, data)
    shutil.move("images/post.jpg", "posted/post.jpg")
    shutil.move("images/post.txt", "posted/post.txt")
    


instapost()

