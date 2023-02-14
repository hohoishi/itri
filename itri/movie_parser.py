# -*- coding: utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime
min_time = 9999999999999999999
result = ""
res_home = requests.get("https://www.vscinemas.com.tw/ShowTimes/")
soup = BeautifulSoup(res_home.text, 'html.parser')
movie_theather_dict = dict()
for movie_theather in soup.find("select",{"id":"CinemaNameTWInfoF"}).find_all('option'):
    if len(movie_theather['value']) > 0:
        movie_theather_dict[movie_theather['value']] = movie_theather.text
cinema_codes = movie_theather_dict.keys()#['TP','MU','MUC','QS','BQ','GM','LK','LKMP','TY','HS','HSGC','BC','TF','TZ','TT01','TT02','MM','TN','FC','NF','NFGC','KS','KSGC','HL']



for cinema_code in cinema_codes:
    #print(f"========{cinema_code}========")
    payload = {
    "CinemaCode":cinema_code,
    }

    #https://www.vscinemas.com.tw/ShowTimes//ShowTimes/GetShowTimes
    response_theather = requests.post("https://www.vscinemas.com.tw/ShowTimes//ShowTimes/GetShowTimes", data = payload)
    #print(response_theather)
    
    soup_theather = BeautifulSoup(response_theather.text, 'html.parser')
    #print(soup_theather.prettify())
    
    for movie in soup_theather.find_all(class_="col-xs-12"):
        movie_name_str = None
        movie_date_str = None
        movie_time_str = None
        try:
            movie_name = movie.find(class_="col-xs-12 LangTW MovieName")
            if movie_name:
                movie_name_str = movie_name.text.strip()
            movie_date_time_list = movie.find_all(class_="col-xs-12 LangTW RealShowDate")
            if len(movie_date_time_list) > 0:
                movie_date_time = movie_date_time_list[0]
                movie_date_str = movie_date_time.text.strip()
            movie_time_list = movie.find(class_="col-xs-12 SessionTimeInfo")
            if movie_date_time_list:
                movie_time = movie_time_list.find(class_="col-xs-0")
                movie_time_str = movie_time.text.strip()
            if movie_name_str and movie_date_str and movie_time_str:
                print(movie_name_str, movie_date_str, movie_time_str)
        except Exception as e:
            print("====fail====")
            
            print(e)
print(result)

    
