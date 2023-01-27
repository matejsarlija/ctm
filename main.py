import requests
from bs4 import BeautifulSoup
from datetime import date
from calendar import monthrange

today = date.today()
today_num = today.day
#print(today.day)

if (today_num + 5) < 30:


url = f'https://www.hep.hr/ods/bez-struje/19?dp=rijeka&el=RI&datum=26.01.2023'
response = requests.get(url)



soup = BeautifulSoup(response.text, 'html.parser')

ulica_divs = soup.find_all('div', class_='ulica')

for div in ulica_divs:
    print(div.text)

myStreet = "Kumičićeva"

if myStreet in div.text:
    print(myStreet + " je bez struje danas")
