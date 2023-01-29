import requests
from bs4 import BeautifulSoup

URL = 'https://sonnenaufgang.online/sun/berlin'

response = requests.get(URL)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
sunrise_data = soup.find('div',{'data-name':'sunrise'})
sunrise_data = sunrise_data.text
sunrise_data = sunrise_data[:-3]
print(f'The sunrise today is at {sunrise_data} hs')