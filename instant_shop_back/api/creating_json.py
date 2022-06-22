import json
#Model products: Name, category, shop, price
f = open('todays_update.txt','r')
products = []
for i in f:
    curr = i.split(';')
    temp_d = {
        'name':curr[0],
        'shop':curr[1],
        'category':curr[2],
        'price': int(curr[3][:-1])
    }
    products.append(temp_d)
f.close()
with open('new_file.json', 'w') as f:
    json.dump(products, f, indent=2)
    print("New json file is created from data.json file")