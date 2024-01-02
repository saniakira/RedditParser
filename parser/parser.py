import lxml
from bs4 import BeautifulSoup
import requests
from icecream import ic


def parse_img(
        url="https://www.reddit.com/media?url=https%3A%2F%2Fi.redd.it%2Fhmm-hmmhmmm-v0-t3djq4rqin9c1.jpeg%3Fs%3D3bb62593a4cb3f4bfea7c2bc58287c976eb36bdc"):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    response = soup.find('meta', property='og:image')
    response = str(response).split('"')[1]
    img = requests.get(response)
    with open('response.jpg', 'wb') as f:
        f.write(img.content)


def parse(url='https://www.reddit.com/r/evangelion/'):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    response = soup.find_all('article')
    ic(len(response))

