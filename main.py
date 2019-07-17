import requests
from bs4 import BeautifulSoup

url = "https://www.williams-sonoma.com/products/williams-sonoma-organic-spice-pizza-seasoning/"
#url = "https://www.williams-sonoma.com/products/pizza-seasoning/"
#url = "https://www.williams-sonoma.com/products/candy-corn-cake/"

response = requests.get(url)
html = response.text

#target example, full price: 
#<span class="price-amount">7.95</span>

#target example, sale price:
#<span class="price-state price-special">
#<span class="price-sale-label">
#Our Price
#</span>
#<span class="currency currencyUSD ">
#<span class="currency-symbol">$</span><span class="price-amount">41.96</span></span>
#</span>

soup = BeautifulSoup(html, "html.parser")
#print(soup)

#check for a sale price
is_on_sale = False
price_special = soup.findAll('span', {'class' : 'price-special'})
#print(price_special[0])

#if there isn't a sale price then look for the regular price
if price_special:
  #yay, a sale!  Dig down into span to grab sale price
  soup2 = BeautifulSoup(str(price_special), "html.parser")
  price_amount = soup2.findAll('span', {'class' : 'price-amount'})
  price = price_amount
  is_on_sale = True
else:
  #no active sale going on. Grab regular price.
  price_amount = soup.findAll('span', {'class' : 'price-amount'})
  price = price_amount

#strip off the tags to get raw price value
price = price[0].contents[0]

if is_on_sale:
    print(price)


