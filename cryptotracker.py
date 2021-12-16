import requests
import bs4
from bs4 import BeautifulSoup
import smtplib

url = "https://coinmarketcap.com/currencies/bitcoin/markets/"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}

from_email="shreyasshettigar34@gmail.com"

to_email = "shreyasfreefire1925@gmail.com"

password="shreyas123#"

#creating functions

def getPrice():
    r=requests.get("https://coinmarketcap.com/currencies/bitcoin/markets/",headers=headers)

    soup = bs4.BeautifulSoup(r.content,"html.parser")
    
    title = soup.find('div',{'class':"sc-16r8icm-0 gpRPnR nameHeader"}).find('h2').text.strip()
    
    img = soup.find('div',{'class':"sc-16r8icm-0 gpRPnR nameHeader"}).find('img')["src"]
    
    print(img)

    #price = soup.find('div',{'class':"sc-16r8icm-0 kjciSH priceTitle"}).find('span').text
    
    print(title)

if __name__ == "__main__":
    getPrice()
