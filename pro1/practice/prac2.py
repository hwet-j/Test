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
driver = webdriver.Chrome("C:/work/chromedriver")
driver.get("https://www.imagefap.com//photo/950430626/?pgid=&amp;gid=9264812&amp;page=0")
time.sleep(5)

req = driver.page_source
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(req, 'html.parser')

image_link = soup.select(".advance-link > img")
print(image_link)

# #\33 49027312 > table > tbody > tr:nth-child(1) > td > a
# page = "https://www.imagefap.com/"
# 파일저장을 위한 값
i = 1
for thumbnail in image_link:
    img = thumbnail['src']
    dload.save(img, f'images/{i}.jpg')
    i += 1
'''
for link in image_link:
        # print(link)
        # print(str(link).find('/photo'), ' ', str(link).find('html'))
        urls = str(link)[str(link).find('https://'):str(link).find('width') - 2]
        # fname = str(link)[str(link).find('image')+5:str(link).find('.html')]
        # fname = page + urls
        print(urls)
        pic_link = Request(urls + ".jpg" ,headers={'User-Agent': 'Mozilla/5.0'})
        #print(pic_link)
        with req.urlopen(pic_link) as f:
            with open('./images/' + str(n)+'.jpg','wb') as h: # w - write b - binary
                img = f.read()
                h.write(img)
        n += 1
        
        time.sleep(0.3)
   ''' 
driver.quit() # 끝나면 닫아주기