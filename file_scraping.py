from requests import Session
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"}

work = Session()

work.get("http://quotes.toscrape.com/", headers=headers)

response = work.get("http://quotes.toscrape.com/login", headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

token = soup.find('form').find('input').get('value')
data = {'csrf_token': token, 'username': 'noname', 'password': 'password'}
result = work.post("http://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True)

response_page = work.get("http://quotes.toscrape.com/page/1/", headers=headers)
soup_page = BeautifulSoup(response_page.text, 'lxml')
data_div_all = soup_page.find_all('div', class_='quote')


def all_blog(list_blogs):
    for i in list_blogs:
        text = i.find('span', class_="text").text
        author = i.find('small', class_="author").text
        aa = i.find_all('a')[1].get('href')

        print(text + '\n' + author + '\n' + aa + '\n\n')


all_blog(data_div_all)
