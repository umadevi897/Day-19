import requests
import pandas as pd
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/search?q=iqoo+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=iqoo+mobile%7CMobiles&requestId=a63956be-397a-4160-81f8-ad1af2638646&as-searchtext=iqoo")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_="_VU-ZEz")
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
prices=soup.find_all('div',class_="_Nx9bqj CxhGGd")
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
rate=soup.find_all('div',class_="_Rza2QY")
rate=[]
for i in rates[0:20]:
    d=i.get_text()
    rate.append(float(d))
images=soup.find_all('img',class_="_DByuf4")
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)
links=soup.find_all('a',class_="_yiggsN O5Fpg8")
link=[]
for i in links[0:20]:
    d="https://www.flipkart.com"+i['href']
    link.append(d)


df=pd.DataFrame() # row columns
df["Names"]=name
df["Prices"]=price
df["Ratings"]=rate
df["Images"]=image
df["Links"]=link

df.to_csv("Mobiles.csv")