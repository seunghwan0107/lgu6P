products = [
    {
        "category": "Electronics",
        "items": [
            {"name": "Laptop", "price": 1200, "stock": 5},
            {"name": "Smartphone", "price": 800, "stock": 10}
        ]
    },
    {
        "category": "Home Appliances",
        "items": [
            {"name": "Vacuum Cleaner", "price": 150, "stock": 7},
            {"name": "Air Conditioner", "price": 500, "stock": 3}
        ]
    }
]

# result = {
#     "Laptop": {"price": 1200, "stock": 5},
#     "Smartphone": {"price": 800, "stock": 10},
#     "Vacuum Cleaner": {"price": 150, "stock": 7},
#     "Air Conditioner": {"price": 500, "stock": 3}
# }


# def convert_data(products):
#     dic = {}
#     for cataegory in products:
#      for it in cataegory["items"]:
#          dic[it["name"]] = {"price": it["price"], "stock": it["stock"]}
#      return dic
    
# dic = convert_data(products)
# print(dic)

def convert_data(products):
    result = {}
    for category in products:
        for item in category['items']:
        #item: {}
        #방법 1
        #  name = item['name']
        #  del item['name'] , pop도있는데 지우고반환
        #  result[name] = item

        #방법2
         result[item['name']] = {
            'price':item['price'],
            'price':item['price']
        }
    return result

item = convert_data(products)
print(item)

import json
print(json.dumps(item,indent=2))
