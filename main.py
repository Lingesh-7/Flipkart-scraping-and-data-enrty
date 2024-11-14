from bs4 import BeautifulSoup
import requests
import lxml
import csv

header={

    "Accept-Language":"en-US,en;q=0.9",

    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

}

response=requests.get(url="https://www.trulia.com/IL/Chicago/",headers=header)
print(response)
# print(response.text)

soup=BeautifulSoup(response.text,"lxml")   
print(soup.title.getText()) 


price=soup.find_all(name="div",class_="textStyle_subHeader fw_bold d_block white-space_nowrap ov_hidden tov_ellipsis")
prices_=[a.getText() for a in price]
print(prices_)

bed=soup.find_all(name='div',class_="textStyle_body d_block")
bedroom=[a.getText().replace('bd','') for a in bed if a.getText().endswith('bd')]
print(bedroom)
bathroom=[a.getText().replace('ba','') for a in bed if a.getText().endswith('ba')]
print(bathroom)



sq=soup.find_all(name='div', class_="textStyle_body d_block white-space_nowrap ov_hidden tov_ellipsis")
sqs_=[s.getText() for s in sq]
print(sqs_)

add=soup.find_all(name='div', class_="c_grey.900 textStyle_body d_block white-space_nowrap ov_hidden tov_ellipsis")
addre_=[a.getText().replace(',','') for a in add]
print(addre_)

for i in range(len(bedroom)):
    with open("House_rent_new_york.csv","a") as f:
        w=csv.writer(f)
        w.writerow([i+1,prices_[i],bedroom[i],bathroom[i],addre_[i]])