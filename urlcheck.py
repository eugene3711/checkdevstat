
#div class="cta-block-stage__title"
#'cta-block-header__group' - new status selector


import requests
from bs4 import BeautifulSoup

testurl = 'https://www.mccarthyandstone.co.uk/retirement-properties-for-sale/balshaw-court/'

def get_status(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    stage = soup.find('div', class_='cta-block-stage__title')

    return stage.get_text()
