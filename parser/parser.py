import os

import deep_translator
import lxml
from bs4 import BeautifulSoup
import requests
from icecream import ic


# def parse_img(
#         url="https://i.redd.it/me-everyone-that-post-those-would-u-let-misato-in-a-damn-v0-pml7c8chu5lb1.jpg?s=b8873b74a381217a55f29cff749f691cfbd617cc"):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'lxml')
#     ic(soup)
# response = soup.find('meta', property='og:image')
# print(str(response).split('"'))
# response = str(response).split('"')[1]
# img = requests.get(response)
# with open('response.jpg', 'wb') as f:
#     f.write(img.content)


def parse(url='https://www.reddit.com/r/evangelionmemes/'):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    responses = soup.find_all('article')
    i = 1
    for response in responses:
        text = str(response.find('a', slot='title')).split('slot="title">')[1].split('<')[0]
        img = requests.get(str(response).split('content-href=')[1].split('"')[1])
        with open(f"{os.getcwd()}\\{deep_translator.GoogleTranslator('auto', 'ru').translate(text)}.jpg",
                  'wb') as f:
            f.write(img.content)
        i += 1


parse()
