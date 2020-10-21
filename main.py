import requests
from bs4 import BeautifulSoup

username = 'emrata'

response = requests.get('https://www.depop.com/' + username)

soup = BeautifulSoup(response.text, 'html.parser')

followers = soup.find(class_='styles__StatsValue-sc-9h44if-0 DtCMM').text

print(username + " has " + followers + " followers!")