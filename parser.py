from bs4 import BeautifulSoup
import requests
import re
import json

walmart_toilet_url = 'https://www.walmart.com/ip/2-Ply-Toilet-Paper-Roll-4-Count/122080977'

# 'product-fulfillment-table'
data = {'zip-code-input': '12345'}
# response = requests.post(url=walmart_toilet_url, data=data)


response = requests.get(walmart_toilet_url)  # to remove


soup = BeautifulSoup(response.content, 'html.parser')


data = soup.findAll(
    'script', attrs={'type': 'application/json', 'id': 'item'})[0].contents

item_data = json.loads(data[0])  # convert to dict

item_location_data = item_data['item']['product']['buyBox']['products'][0]['pickupOptions']

all_stores = []
for store in item_location_data:
    STORE_OBJECT = {}
    STORE_OBJECT['store_name'] = store['storeName']
    STORE_OBJECT['store_address'] = store['storeAddress']
    STORE_OBJECT['store_state'] = store['storeStateOrProvinceCode']
    STORE_OBJECT['store_postal_code'] = store['storePostalCode']
    STORE_OBJECT['store_availability'] = store['availability']
    STORE_OBJECT['store_city'] = store['storeCity']
    all_stores.append(STORE_OBJECT)

print(all_stores)

# <script id="item" type="application/json">
