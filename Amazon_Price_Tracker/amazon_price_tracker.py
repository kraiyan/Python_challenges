import requests
from bs4 import BeautifulSoup
# you need to install requests, bs4 and lxml
# URL holds the link of the amazon product you want to track
URL ='https://www.amazon.in/HP-Processor-14-inch-Windows-14s-er0002TU/dp/B08LBJN122/ref=sr_1_1?dchild=1&hvadid=73048917514199&hvbmt=bb&hvdev=c&hvqmt=b&keywords=hp+14ser0002tu&qid=1610265323&sr=8-1&tag=msndeskstdin-21'
# you'll need to provide your own User-Agent, by simply going to google and search for "my User-Agent"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

#requests gets the content of the URL and saves it in our page variable
page = requests.get(URL,headers = headers)

# we are using Beautiful Soup to parse the content
soup = BeautifulSoup(page.text,'lxml') #make sure you use "lxml' or "html5lib" parser instead of "html.parser"
price_text = soup.find(id="bundle-v2-btf-price").get_text(strip = True).replace('₹','').replace(',','')
price=float(price_text)
print("price = "+str(price))

if price < 20000:
	print ("Hey, the price is low, and the price is: "+ str(price))
else:
	print("get yourself some fuckin money nigga")
