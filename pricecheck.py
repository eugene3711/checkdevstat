import requests
from bs4 import BeautifulSoup

testurl = 'https://www.andrewgeoghegan.com/product/cannele-twist-diamond/'

def get_status(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find('span', class_='woocommerce-Price-amount')
    price = int(price.get_text()[1:-3].replace(',',''))
    return price

