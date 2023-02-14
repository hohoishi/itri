#t-mobile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import datetime
parse_yr = (2018, 2019, 2020, 2021, 2022)
parse_month = [m for m in range(1,13)]
print(parse_month)
driver = webdriver.Firefox()
parsed_set = set()
base_link = "https://www.t-mobile.com"
def get_content_date():
    html = driver.page_source
    soup = BeautifulSoup(html)
def get_content():
    ret_list = list()
    html = driver.page_source
    soup = BeautifulSoup(html)
    div = soup.find("div", {"class": "card-grid"})
    children = div.findChildren("article", class_="card-grid-item", recursive=False)
    for child in children:
        #time = child.find("div", class_="published-date").getText().replace("|","")
        #time_un = datetime.datetime.strptime(time, '%m.%d.%Y')
        title = child.find("h3", class_="card-grid-item__title").getText()
        link = child.find("a", class_="card-grid-item__link").get('href')
        if link not in parsed_set:
            print(f"Parse {title}-{link}")
            ret_list.append(['', title, base_link + link])
            parsed_set.add(link)
        #elif time_un.year <=2017:
        #    return ret_list,False
    return ret_list,True
    
    
try:
    parsed_data_list = list()
    parseURL = f"https://www.t-mobile.com/news/press"
    driver.get(parseURL)
    data_list, _ = get_content()
    parsed_data_list.extend(data_list)
    
    next_btn = driver.find_elements_by_class_name("pagination-old")[0]
    while next_btn:
        next_btn.click()
        data_list, is_need_parse = get_content()
        parsed_data_list.extend(data_list)
        if not is_need_parse:
            raise Exception()
        next_btn = driver.find_elements_by_class_name("pagination-old")
        if len(next_btn)>0:
            next_btn = next_btn[0]
            time.sleep(0.5)
    
except Exception as e:
    print(e)
finally:
    driver.close()
