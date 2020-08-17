import requests
from bs4 import BeautifulSoup as bs
import json
import random
import os.path

insta_url = 'https://www.instagram.com'
inta_username = input('enter username of instagram : ')

response = requests.get(f"{insta_url}/{inta_username}/")

s = bs(response.text,"html.parser")
u= s.find("meta", property="og:image")
url = u.attrs['content']

with open(inta_username+'.jpg', "wb") as pic:
    binary = requests.get(url).content
    pic.write(binary)