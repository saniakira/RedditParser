import os
from time import sleep

import deep_translator
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

"""{os.getcwd()}\\{deep_translator.GoogleTranslator('en', 'ru').translate(text)}"""


def parse(soup):
    responses = soup.find_all('shreddit-post')
    i = 1
    if not os.path.exists('images'):
        os.mkdir('images')
    for response in responses:
        try:
            text = str(response.find('a', slot='title')).split('slot="title">')[1].split('<')[0]
            img = requests.get(str(response).split('content-href=')[1].split('"')[1])
            with open(f"{os.getcwd()}\\images\\{i} {deep_translator.GoogleTranslator('auto', 'ru').translate(text)}.jpg",
                      'wb') as f:
                f.write(img.content)
            i += 1
        except:
            pass


def selenium_parse(path=os.getcwd(), count=5):
    url = "https://www.reddit.com/r/evangelionmemes/"
    driver = webdriver.Edge(f'{path}/msedgedriver.exe')
    driver.get(url)
    last_height = driver.execute_script("return document.body.scrollHeight")
    for _ in range(count):
        # Прокрутка вниз
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Пауза, пока загрузится страница.
        sleep(2)
        # Вычисляем новую высоту прокрутки и сравниваем с последней высотой прокрутки.
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
    html = driver.page_source
    driver.close()
    soup = BeautifulSoup(html, "lxml")
    parse(soup)


selenium_parse()
