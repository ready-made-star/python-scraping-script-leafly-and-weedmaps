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
indica_page_per_take=1  #18

sativa_page_num=0 #411
sativa_page_per_take=1

productList_slug=[]

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
        try:
            if(y<8): 
                productList_slug.append(driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div[2]/div[3]/section[1]/div[{}]/article/a".format(y+1)).get_attribute("href"))
            elif(y>=8 and y<12): 
                productList_slug.append(driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div[2]/div[3]/section[1]/div[{}]/article/a".format(y+2)).get_attribute("href"))
            elif(y>=12): 
                productList_slug.append(driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div[2]/div[3]/section[1]/div[{}]/article/a".format(y+3)).get_attribute("href"))
        except:
            continue
productList_name=[]
productList_url=[]
productList_strain_name=[]
productList_kind=[]
productList_thc=[]
productList_cbd=[]
productList_rating=[]
productList_strain_rating=[]
productList_desc=[]
productList_strain_desc=[]
productList_feelings=[]
productList_negatives=[]
productList_helpwith=[]
productList_brand_name=[]
productList_brand_url=[]
productList_brand_desc=[]

for pi in productList_slug:
    driver.get(pi)
    try:
        productList_name=driver.find_element(By.XPATH, "/html/body/div/div[15]/main/div[1]/div[2]/div[2]/div/div[1]/h1").text
    except:
        productList_name.append('')
    try:
        productList_url=driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/ul/li[1]/div/div/picture/source[1]').get_attribute('srcset')
    except:
        productList_url.append('')
    try:
        productList_strain_name=driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[4]/div/div[1]/div[1]/div/div[2]/a').text
    except:
        productList_strain_name.append('')   
    try:
        productList_kind=driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[1]/span[1]').text
    except:
        productList_kind.append('')
    try:
        productList_thc=driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[1]/span[2]').text
    except:
        productList_thc.append('')
    try:
        productList_cbd=driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[1]/span[3]').text
    except:
        productList_cbd.append('')
    try:
        productList_rating=driver.find_element(By.XPATH, '//div[@class="mb-xs"]//span[@class="pr-xs"]').text

    except:
        productList_rating.append('')
    try:
        productList_strain_rating=driver.find_element(By.XPATH, '//div[@class="mb-sm"]//span[@class="pr-xs"]').text
        
    except:
        productList_strain_rating.append('')
    try:
        productList_desc=driver.find_element(By.XPATH, '/html/body/div/div[15]/main/div[1]/div[2]/div[3]/div/div/div/div/div/div').text
    except:
        productList_desc.append('')
    try:
        productList_strain_desc=driver.find_element(By.XPATH, '//div[@class="mb-xxl"]//p').text
    except:
        productList_strain_desc.append('')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    try: 
        productList_feelings = soup.find(
                'div', {'class': 'react-tabs-padding'}).find_next({'div'}).find_next({'div'}).find_all({'div'})[1]
        productList_feelings = productList_feelings.text
        
    except Exception as E:
        print('err', E)
        productList_feelings.append('')
    try:    
        productList_negatives = soup.find(
                'div', {'class': 'react-tabs-padding'}).find_all({'div'})[16]
        productList_negatives = productList_negatives.text
    except:
        productList_negatives.append('')
    try: 
        productList_helpwith = soup.find(
                'div', {'class': 'react-tabs-padding'}).find_all({'div'})[29]
        productList_helpwith = productList_helpwith.text
    except:
        productList_helpwith.append('')
    try:
        productList_brand_desc = soup.find('div', {'data-testid': 'about-brand' }).find_next({'div'}).find_next({'div'}).find_next({'div'}).find_all({'div'})[3]
        productList_brand_desc=productList_brand_desc.text
    except Exception as E:
        print('err', E)
        productList_brand_desc.append('')
    try:
        productList_brand_name = soup.find('div', {'data-testid': 'about-brand' }).find_next({'div'}).find_all({'div'})[9]
        productList_brand_name=productList_brand_name.text
    except Exception as E:
        print('err', E)
        productList_brand_name.append('')
    try:    
        productList_brand_url=soup.find('div', {'data-testid': 'about-brand' }).find_all({'img'})
        productList_brand_url=productList_brand_url[0].get('data-srcset')
    except Exception as E:
        print('err', E)
        productList_brand_url.append('')
    
    row = [productList_name, productList_url, productList_strain_name, productList_kind, productList_thc, productList_cbd, productList_rating,
        productList_strain_rating, productList_desc, productList_strain_desc, productList_feelings, productList_negatives,
        productList_helpwith,
        productList_brand_name,
        productList_brand_url,
        productList_brand_desc]
    # print(row)
    with open('event3.csv', 'a', encoding='utf-8', newline='') as f_object:
 
        product_row = writer(f_object)
 
        product_row.writerow(row)
 
        f_object.close()