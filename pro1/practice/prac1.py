from bs4 import BeautifulSoup
import urllib.request as req
from urllib.request import Request
import re
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import dload


# html형식의 데이터를 가져올 홈페이지
url = Request("https://www.imagefap.com/pictures/9264812/Artgravia-VOL.162-Jang-joo",
               headers={'User-Agent': 'Mozilla/5.0'})
html_page = req.urlopen(url).read()
soup = BeautifulSoup(html_page, 'html.parser')
# print(html_page)

# class=col-md-3 col-sm-4 col-xs-12 안에 class=thumbnail의 데이터를 모두 가져옴 (select, select_one이면 하나만)
# id나 class명에 공백이 있다면 . 으로 대체하여 작성가능 
image_link = soup.select(".expp-container > form > table > tr > td > table > tr > td > a")
# print(image_link)

# #\33 49027312 > table > tbody > tr:nth-child(1) > td > a
page = "https://www.imagefap.com/"
# 파일저장을 위한 값
i = 1

for link in image_link:
        # print(link)
        # print(str(link).find('/photo'), ' ', str(link).find('html'))
        urls = str(link)[str(link).find('/photo'):str(link).find('name=') - 2]
        print(urls)
        
        driver = webdriver.Chrome("C:/work/chromedriver")
        driver.get(page+urls)
        time.sleep(5)
        
        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')
        
        image_link = soup.select(".advance-link > img")
        print(image_link)
        
        for thumbnail in image_link:
            img = thumbnail['src']
            dload.save(img, f'images/{i}.jpg')
            i += 1
        driver.quit() # 끝나면 닫아주기
        
        
        
