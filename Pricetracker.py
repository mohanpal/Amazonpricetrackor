import requests
from bs4 import BeautifulSoup
import smtplib
import time


headers = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

response = requests.get('https://www.amazon.com.au/Sony-Cancelling-Headphones-WF-1000XM3-WF1000XM3B/dp/B07V4BWVH1?pf_rd_p=1178aa86-2fb9-5ada-9c85-a73da4806e50&pf_rd_r=TVDPDMT1HW4V0VHJHFPH&pd_rd_wg=JRtZi&ref_=pd_gw_ri&pd_rd_w=1lCfC&pd_rd_r=98782f5f-e9f4-4cf9-883b-18ae5c557b3e', headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

converted_price = float(price[0:5])
  print(converted_price)
  if(converted_price < 20000):
    send_mail()

print(title.strip())

def check_price():
  title = soup.find(id= "productTitle").get_text()
  price = soup.find(id = "priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
  print(price)
  
  while(True):
  check_price()
  time.sleep(60 * 60)
