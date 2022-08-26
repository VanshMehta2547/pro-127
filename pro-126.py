from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import csv
import pandas as pd
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/vansh/OneDrive/Desktop/WhiteHat/c-126/chromedriver.exe")
browser.get(START_URL)
time.sleep(2)
headers = ["Name", "Distance", "Mass", "Radius"]
stars_data = []
temp_list = []
def scrape():
    try:
        page = requests.get(START_URL)
        soup = BeautifulSoup(page.content,"html.parser")
        
        star_table = soup.find('table') 
        temp_list= [] 
        table_rows = star_table.find_all('tr') 
        for tr in table_rows: 
            td = tr.find_all('td') 
        row = [i.text.rstrip() for i in td] 
        temp_list.append(row)
        
    except:
        time.sleep(1)
        scrape()

scrape()

Star_names = [] 
Distance =[] 
Mass = [] 
Radius =[]  
print(len(temp_list))
for i in range(1,len(temp_list)): 
    Star_names.append(temp_list[i][1]) 
    Distance.append(temp_list[i][3]) 
    Mass.append(temp_list[i][5]) 
    Radius.append(temp_list[i][6]) 

df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius']) 
print(df2) 
df2.to_csv('bright_stars.csv')