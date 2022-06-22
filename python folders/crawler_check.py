from itertools import product
from tabnanny import check
import requests
import lxml
from bs4 import BeautifulSoup
import time,random

def check_price(store, category_id, product_id):
  if(category_id == 1 and product_id == 1): return 9999999
  url = "https://almaty.instashop.kz/store/" + store + "/" + str(category_id) + "/"
  headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
  }
  f = requests.get(url, headers = headers)
  num=0
  found = False
  discount = False
  rr = ""
  soup = BeautifulSoup(f.content, 'lxml')
  for item in soup.find_all(attrs={"data-id": product_id}):
      if(found == True): break
      #Without discount
      if(len(item.findChild("div", class_="b-product-list__price"))==3):
        for i in item.findChild("div", class_="b-product-list__price"):
          #print(num,i)
          if(num == 0):
            for j in i:
              if(j >= '0' and j <= '9'): rr += str(j)
            found = True
            break
          num += 1
      #With discount
      else:
        for i in item.findChild("div", class_="b-product-list__price"):
          #print(num,i)
          if(num == 1):
            for j in i:
              if(j >= '0' and j <= '9'): rr += str(j)
            found = True
            discount = True
            break
          num += 1
  if(discount): return int(rr.strip()[:-3].replace(' ',''))
  if(found): return int(rr.strip())
  cur_page = 1
  while(cur_page != 12):
    time.sleep(random.randint(1,5))
    url = "https://almaty.instashop.kz/store/" + store + "/" + str(category_id) + "/" + "?&ajax=Y&PAGEN_1=" + str(cur_page) + "/"
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    f = requests.get(url, headers = headers)
    num=0
    found = False
    discount = False
    rr = ""
    soup = BeautifulSoup(f.content, 'lxml')
    for item in soup.find_all(attrs={"data-id": product_id}):
        if(found == True): break
        #Without discount
        if(len(item.findChild("div", class_="b-product-list__price"))==3):
          for i in item.findChild("div", class_="b-product-list__price"):
            #print(num,i)
            if(num == 0):
              for j in i:
                if(j >= '0' and j <= '9'): rr += str(j)
              found = True
              break
            num += 1
        #With discount
        else:
          for i in item.findChild("div", class_="b-product-list__price"):
            #print(num,i)
            if(num == 1):
              for j in i:
                if(j >= '0' and j <= '9'): rr += str(j)
              found = True
              discount = True
              break
            num += 1
    if(discount): return int(rr.strip()[:-3].replace(' ',''))
    if(found): return int(rr.strip())
    cur_page += 1
  return 9999999
  

#Starting from A-Store to Metro

#Model products: Name, category, shop, price
# category: Name
# shop: name

#Milk comparing
products = ['Lactel 2,5%', 'Adal 2,5%', 'Domik v derevne 2,5%', 'Spaghetti Sultan 1,6 kg', 'Spiral Sultan 1,6 kg', 'Rice Astyq 800g', 'Oat flakes "Hercules", King, 400 gr','Sunflower oil Masterpiece 1 liter', 'Sunflower oil Masterpiece 5 liters', 'Wheat flour premium TESNA 5 kg', 'Wheat flour premium TESNA 10 kg', 'Coca-Cola 1 liter', "PIALA| GOLD Kenyan granulated tea 500 gr.", "Mayonnaise Provencal 3 wishes 380 gr","Ketchup HEINZ Tomato, 1000g", 'Eggs Kazger-Kus premium 10 pack']

all_categories = {'Lactel 2,5%':"Milk", "Adal 2,5%":"Milk", "Domik v derevne 2,5%":"Milk", 'Spaghetti Sultan 1,6 kg':"Grocery", 'Spiral Sultan 1,6 kg':"Grocery", 'Rice Astyq 800g':"Grocery", 'Oat flakes "Hercules", King, 400 gr':"Grocery",'Sunflower oil Masterpiece 1 liter':"Grocery", 'Sunflower oil Masterpiece 5 liters':"Grocery", 'Wheat flour premium TESNA 5 kg':"Grocery", 'Wheat flour premium TESNA 10 kg':"Grocery",'Coca-Cola 1 liter':"Drink", "PIALA| GOLD Kenyan granulated tea 500 gr.":"Tea", "Mayonnaise Provencal 3 wishes 380 gr":"Sauce","Ketchup HEINZ Tomato, 1000g":"Sauce", 'Eggs Kazger-Kus premium 10 pack':"Eggs"}

categories_A_Store = {'Lactel 2,5%':33320, 'Adal 2,5%': 33320, 'Domik v derevne 2,5%' : 33320, 'Spaghetti Sultan 1,6 kg' : 33180, 'Spiral Sultan 1,6 kg':33180, 'Rice Astyq 800g':33226, 'Oat flakes "Hercules", King, 400 gr':33191,'Sunflower oil Masterpiece 1 liter':1,'Sunflower oil Masterpiece 5 liters':33260, 'Wheat flour premium TESNA 5 kg':33254, 'Wheat flour premium TESNA 10 kg':33254, 'Coca-Cola 1 liter':33174, "PIALA| GOLD Kenyan granulated tea 500 gr.":33127, "Mayonnaise Provencal 3 wishes 380 gr":33231,"Ketchup HEINZ Tomato, 1000g":33275, 'Eggs Kazger-Kus premium 10 pack':1}
product_id_A_Store = {'Lactel 2,5%': 1954600, 'Adal 2,5%': 1954685, 'Domik v derevne 2,5%':2069290, 'Spaghetti Sultan 1,6 kg' : 1953127, 'Spiral Sultan 1,6 kg':1953129, 'Rice Astyq 800g':1948068, 'Oat flakes "Hercules", King, 400 gr':1976900,'Sunflower oil Masterpiece 1 liter':1,'Sunflower oil Masterpiece 5 liters':1953996, 'Wheat flour premium TESNA 5 kg':1955326, 'Wheat flour premium TESNA 10 kg':1955328, 'Coca-Cola 1 liter':1957975, "PIALA| GOLD Kenyan granulated tea 500 gr.":1977415, "Mayonnaise Provencal 3 wishes 380 gr":1952946,"Ketchup HEINZ Tomato, 1000g":1942809, 'Eggs Kazger-Kus premium 10 pack':1}

categories_Metro = {'Lactel 2,5%':34081, 'Adal 2,5%': 34081, 'Domik v derevne 2,5%' : 34081, 'Spaghetti Sultan 1,6 kg' : 34109, 'Spiral Sultan 1,6 kg': 34109, 'Rice Astyq 800g':34127, 'Oat flakes "Hercules", King, 400 gr':34033,'Sunflower oil Masterpiece 1 liter':1,'Sunflower oil Masterpiece 5 liters':1, 'Wheat flour premium TESNA 5 kg':34212, 'Wheat flour premium TESNA 10 kg':34212, 'Coca-Cola 1 liter':34152, "PIALA| GOLD Kenyan granulated tea 500 gr.":34025, "Mayonnaise Provencal 3 wishes 380 gr":34173,"Ketchup HEINZ Tomato, 1000g":34140, 'Eggs Kazger-Kus premium 10 pack':34281}
product_id_Metro = {'Lactel 2,5%': 239606, 'Adal 2,5%': 262500, 'Domik v derevne 2,5%':249000, 'Spaghetti Sultan 1,6 kg' : 263214, 'Spiral Sultan 1,6 kg': 247651, 'Rice Astyq 800g':258095, 'Oat flakes "Hercules", King, 400 gr':267224,'Sunflower oil Masterpiece 1 liter':1,'Sunflower oil Masterpiece 5 liters':1, 'Wheat flour premium TESNA 5 kg':243781, 'Wheat flour premium TESNA 10 kg':243780, 'Coca-Cola 1 liter':246983, "PIALA| GOLD Kenyan granulated tea 500 gr.":239604, "Mayonnaise Provencal 3 wishes 380 gr":256847,"Ketchup HEINZ Tomato, 1000g":276915, 'Eggs Kazger-Kus premium 10 pack':283513}

categories_Carefood = {'Lactel 2,5%':32438, 'Adal 2,5%': 32438, 'Domik v derevne 2,5%' : 32438, 'Spaghetti Sultan 1,6 kg' : 32338, 'Spiral Sultan 1,6 kg':1, 'Rice Astyq 800g':1, 'Oat flakes "Hercules", King, 400 gr':1,'Sunflower oil Masterpiece 1 liter':32349,'Sunflower oil Masterpiece 5 liters':32349, 'Wheat flour premium TESNA 5 kg':32452, 'Wheat flour premium TESNA 10 kg':32452, 'Coca-Cola 1 liter':32328, "PIALA| GOLD Kenyan granulated tea 500 gr.":32293, "Mayonnaise Provencal 3 wishes 380 gr":32347,"Ketchup HEINZ Tomato, 1000g":32372, 'Eggs Kazger-Kus premium 10 pack':32466}
product_id_Carefood = {'Lactel 2,5%': 1535920, 'Adal 2,5%': 1512603, 'Domik v derevne 2,5%':1506394, 'Spaghetti Sultan 1,6 kg':1503683, 'Spiral Sultan 1,6 kg':1, 'Rice Astyq 800g':1, 'Oat flakes "Hercules", King, 400 gr':1,'Sunflower oil Masterpiece 1 liter':1526848,'Sunflower oil Masterpiece 5 liters':1505500, 'Wheat flour premium TESNA 5 kg':1499141, 'Wheat flour premium TESNA 10 kg':1526852, 'Coca-Cola 1 liter':1515742, "PIALA| GOLD Kenyan granulated tea 500 gr.":1496492, "Mayonnaise Provencal 3 wishes 380 gr":1537045,"Ketchup HEINZ Tomato, 1000g":1508399, 'Eggs Kazger-Kus premium 10 pack':1507045}
file_writer = open('todays_update.txt', 'w')

for i in products:
  a_store = check_price('a-store', categories_A_Store[i], product_id_A_Store[i])
  metro = check_price('metro', categories_Metro[i], product_id_Metro[i])
  carefood = check_price('carefood',categories_Carefood[i], product_id_Carefood[i])
  print(f"{i}")
  print(f"A-Store: {a_store}")
  print(f"Metro: {metro}")
  print(f"Carefood: {carefood}")
