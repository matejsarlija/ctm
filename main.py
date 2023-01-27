import requests
from bs4 import BeautifulSoup
from datetime import date
from calendar import monthrange

# todays date info
today = date.today()

# number for todays date
today_num = today.day
# so this will work until months are single digit for now :)
today_month_num = today.month

# get year
today_year_num = today.year

# programmatically get the number of days in current month
days_in_this_month = monthrange(today_year_num, today_month_num)[1]

#if today_num > days_in_this_month:

url = f'https://www.hep.hr/ods/bez-struje/19?dp=rijeka&el=RI&datum={today_num}.0{today_month_num}.2023'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

street_divs = soup.find_all('div', class_='ulica')

for div in street_divs:
    print(div.text)

myStreet = "Kumičićeva"

if myStreet in div.text:
    print(myStreet + " je bez struje danas")
