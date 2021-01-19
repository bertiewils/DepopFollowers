#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup

if sys.argv[1][0] == '-':
	flag = sys.argv[1]
	username = sys.argv[2]
else:
	flag = ' '
	username = sys.argv[1]


response = requests.get('https://www.depop.com/' + username)

soup = BeautifulSoup(response.text, 'html.parser')

followers = soup.find(class_='styles__StatsValue-sc-9h44if-0 DtCMM').text

if flag in ('-s', '--short'):
	print(followers)
else:
	print(username + " has " + followers + " followers!")
