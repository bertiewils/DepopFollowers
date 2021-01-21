#!/usr/bin/env python3

import argparse
import requests
from bs4 import BeautifulSoup


parser = argparse.ArgumentParser(description='Retrieve follower count for a user on Depop')
parser.add_argument('username', help='username of the user')
parser.add_argument('-s', '--short', action='store_true', help='print just the follower count')
args = parser.parse_args()


response = requests.get('https://www.depop.com/' + args.username)

soup = BeautifulSoup(response.text, 'html.parser')

followers = soup.find(class_='styles__StatsValue-sc-9h44if-0 DtCMM').text

if args.short:
	print(followers)
else:
	print(args.username + " has " + followers + " followers!")
