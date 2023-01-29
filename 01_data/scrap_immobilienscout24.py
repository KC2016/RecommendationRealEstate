import requests
headers= {
    'content-type': 'application/json',
    'x-requested-with': 'XMLHttpRequest'
   }

api_url = "https://www.immobilienscout24.de/Suche/de/berlin/berlin/wohnung-kaufen?pagenumber=1"

jsonData = requests.post(api_url).json()

for item in jsonData['searchResponseModel']['resultlist.resultlist']['resultlistEntries'][0]['resultlistEntry']:
    value=item['attributes'][0]['attribute'][0]['value'].replace('€','').replace('.',',')
    print(value)

# import requests
# from bs4 import BeautifulSoup
# import random

# headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 ("
#                          "KHTML, like Gecko) Version/4.0 Safari/534.30 , 'Accept-Language': 'en-US,en;q=0.5'"}


# url = "https://www.immobilienscout24.de/Suche/de/berlin/berlin/wohnung-kaufen?enteredFrom=one_step_search"

# response = requests.get(url, cookies={'required_cookie': 'reese84=xxx'} ,headers=headers)
# webpage = response.content
# print(response.status_code)

# soup = BeautifulSoup(webpage, "html.parser")
# print(soup.prettify)