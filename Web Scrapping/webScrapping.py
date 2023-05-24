import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
}

url = 'https://www.flipkart.com/asus-vivobook-15-core-i3-11th-gen-8-gb-512-gb-ssd-windows-11-home-x515ea-ej322ws-thin-light-laptop/p/itmc6461360364e0?pid=COMGA5TUCZAV4HGH&lid=LSTCOMGA5TUCZAV4HGHWM8PS0&marketplace=FLIPKART&q=laptop&store=6bo%2Fb5g&spotlightTagId=FkPickId_6bo%2Fb5g&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&fm=search-autosuggest&iid=2193c180-bb20-432c-9da5-80c1f1cca69d.COMGA5TUCZAV4HGH.SEARCH&ppt=sp&ppn=sp&ssid=gia417yd000000001684081988769&qH=312f91285e048e09'

def get_reviews(url):
    reviews = []
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    review_containers = soup.find_all('div', {'class': '_1AtVbE'})

    for container in review_containers:
        divs = container.findAll('div', {'class': 't-ZTKy'})
        if(divs):
            for div in divs:
                reviews.append(div.text)

    return reviews


reviews = get_reviews(url)
for review in reviews:
    print(review)
    print('---')