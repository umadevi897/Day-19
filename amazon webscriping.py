import requests
import pandas as pd
from bs4 import BeautifulSoup

response=requests.get("https://www.amazon.in/s?k=iqoo+mobiles+5g&i=electronics&crid=D24ATRUFPD0C&sprefix=iqomobiles%2Celectronics%2C316&ref=nb_sb_ss_ts-doa-p_2_10")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_="a-size-medium a-color-base a-text-normal")
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
prices=soup.find_all('div',class_="a-price-whole")
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
rates=soup.find_all('div',class_="a-size-base a-color-base")
rate=[]
for i in rates[0:20]:
    d=i.get_text()
    rate.append(float(d))
images=soup.find_all('img',class_="a-dynamic-image a-stretch-horizontal")
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)
links=soup.find_all('a',class_="ssf-share-trigger")
link=[]
for i in links[0:20]:
    d="https://www.amazon.in"+i['href']
    link.append(d)


df=pd.DataFrame() # row columns
df["Names"]=name
df["Prices"]=price
df["Ratings"]=rate
df["Images"]=image
df["Links"]=link

df.to_csv("Mobiles.csv")