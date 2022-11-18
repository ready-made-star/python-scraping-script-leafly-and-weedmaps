from lib2to3.pgen2 import driver
from urllib import response
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from csv import writer
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.maximize_window()
indica_url="https://www.leafly.com/products/collections/indica?page={}"
sativa_url="https://www.leafly.com/products/collections/sativa?page={}"

indica_page_num=1  #534
indica_page_per_take=5  #18

sativa_page_num=0 #411
sativa_page_per_take=1

productList_slug=[]

# get product list slug
for x in range(indica_page_num):
    url=indica_url.format(x+1)
    driver.get(url)
    for y in range(indica_page_per_take):
        # print(y)
        try:
            if(y<8): 
                productList_slug.append(driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div[2]/div[3]/section[1]/div[{}]/article/a".format(y+1)).get_attribute("href"))
            elif(y>=8 and y<12): 
                productList_slug.append(driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div[2]/div[3]/section[1]/div[{}]/article/a".format(y+2)).get_attribute("href"))
            elif(y>=12): 
                productList_slug.append(driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div[2]/div[3]/section[1]/div[{}]/article/a".format(y+3)).get_attribute("href"))
        except:
            continue
for x in range(sativa_page_num):
    url=sativa_url.format(x+1)
    driver.get(url)
    for y in range(sativa_page_per_take):
        # print(y)
        try:
            if(y<8): 
                productList_slug.append(driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div[2]/div[3]/section[1]/div[{}]/article/a".format(y+1)).get_attribute("href"))
            elif(y>=8 and y<12): 
                productList_slug.append(driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div[2]/div[3]/section[1]/div[{}]/article/a".format(y+2)).get_attribute("href"))
            elif(y>=12): 
                productList_slug.append(driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div[2]/div[3]/section[1]/div[{}]/article/a".format(y+3)).get_attribute("href"))
        except:
            continue
# print(productList_slug)
price_url = ''
for pi in productList_slug:
    driver.get(pi)
    try:
        price_url=driver.find_element(By.XPATH, "//a[@class='button']").get_attribute("href")
        print('price', price_url)
    except:
        price_url = ''
    row = [price_url]
    # print(row)
    with open('price_list.csv', 'a', encoding='utf-8', newline='') as f_object:
 
        product_row = writer(f_object)
 
    # Pass the list as an argument into
    # the writerow()
        product_row.writerow(row)
 
    # Close the file object
        # f_object.close()
print('done')