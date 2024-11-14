from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_option)
driver.get("https://www.flipkart.com/search?q=laptops&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_4_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_4_0_na_na_na&as-pos=4&as-type=TRENDING&suggestionId=laptops&requestId=04ec4935-dc8c-4f6f-84fd-84cbdd9c00d6&page=1")


def writing(hast,name,r,pr):
    with open("tariq_laptops.csv","a",encoding="utf-8") as f:
        w=csv.writer(f)
        for i in range(len(name)):
            w.writerow([name[i],r[i],pr[i]])


i=1
while True:
    
    name=driver.find_elements(By.CLASS_NAME,value='KzDlHZ')
    name_=[i.text for i in name]
    # print(name_)
    print(len(name_))

    rating=driver.find_elements(By.CLASS_NAME,value='XQDdHH')
    ratings=[i.text for i in rating]
    # print(ratings)


    Price=driver.find_elements(By.CSS_SELECTOR,value='.hl05eU div')
    price_=[i.text for i in Price if i.text.startswith('₹')]
    # print(price_)

    # processor=driver.find_elements(By.CLASS_NAME,value="G4BRas")
    # processor_=[i.text for i in processor]
    # print(processor_)

    writing(i+1,name_,ratings,price_)


    page_end=driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div[1]/div[2]/div[25]')  
    driver.execute_script("arguments[0].scrollIntoView()", page_end)

    time.sleep(3)

    next_page=driver.find_element(By.XPATH,value=f"//*[@id='container']/div/div[3]/div[1]/div[2]/div[26]/div/div/nav/a[{i+1}]")
    time.sleep(3)

    next_page.click()

    time.sleep(7)
    i+=1







