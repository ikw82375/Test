import json

max_price=float('-inf')
min_price=float('inf')

kosuu=0
with open('catalog.json', 'r') as file:
    catalog_data=json.load(file)
    for item in catalog_data:
        if item['name']=='jacket':
            kosuu+= 1
            price_data=item['price']
            if max_price<price_data:
                max_price=price_data
            if min_price>price_data:
                min_price = price_data
print("Jacketの個数=",kosuu)
print("最高価格=",max_price)
print("最低価格=",min_price)