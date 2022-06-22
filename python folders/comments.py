""" num = 0
soup = BeautifulSoup(f.content, 'lxml')
#price = soup.find_all('ul', class_="swiper-wrapper b-product-list insta-section b-product-list_full")
price = soup.find('ul', class_="swiper-wrapper b-product-list insta-section b-product-list_full")

for i in price:
    print(num, i, end="\n\n")
    num += 1
print(len(price)) """