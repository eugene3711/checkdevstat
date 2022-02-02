
#div class="cta-block-stage__title"
#'cta-block-header__group' - new status selector


import requests
from bs4 import BeautifulSoup

testurl = 'https://www.mccarthyandstone.co.uk/retirement-properties-for-sale/balshaw-court/'

def get_status(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        stage = soup.find('div', class_='cta-block-header__group').get_text()
    except:
        
        try:
            stage = soup.find('div', class_ = 'cta-block-stage__footer').get_text()
            
        except:
            stage = 'n/a'

    return stage


camp = 'https://www.mccarthyandstone.co.uk/retirement-properties-for-sale/campbell-house-weybridge/'

print(get_status(testurl))
print(get_status(camp))
