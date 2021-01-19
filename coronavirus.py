#!/usr/bin/python3
import requests
import urllib.request
from datetime import datetime
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/country/italy/"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

cases = soup.find('div', class_='maincounter-number')
now = datetime.now()
casi = cases.text.strip() + " data: " + now.strftime("%d/%m/%Y %H:%M:%S")
