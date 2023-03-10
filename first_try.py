from bs4 import BeautifulSoup
import requests

#scrape data
url = "https://store.opel.fr/trim/configurable/corsa-citadine"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

#id = ""
market = ""
brand = ""
model = soup.find('div', class_="sc-dMSCXF").find('h3').get_text()
entity = ""
engine = ""
price = 0
horsepower = ""
bodystyle = ""
serie = ""
fuel = ""
consumption = ""
emission_co2 = ""
transmission = ""
transmission_type = ""
driveline = ""
reaerstring = ""
matchstring = ""
datasource = ""
datum = ""

# WE DON'T NEED THIS FILE ANIMORE. DELETE IT!