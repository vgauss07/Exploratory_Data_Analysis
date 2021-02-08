import requests
from bs4 import BeautifulSoup

username = input("Enter Instagram Username: ")

fetch_info = requests.get('http://instagram.com/' + username)
soup_data = BeautifulSoup(fetch_info.text, 'html.parser')
userInfo = soup_data.find("meta", property="og:description")

print(userInfo.attrs['content'][:40])