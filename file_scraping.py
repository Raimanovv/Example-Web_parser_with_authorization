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


def all_pages():
    i = 1
    while True:
        response_page = work.get(f"http://quotes.toscrape.com/page/{i}/", headers=headers)
        soup_page = BeautifulSoup(response_page.text, 'lxml')
        data_div_all = soup_page.find_all('div', class_='quote')
        if len(data_div_all) != 0:
            for j in data_div_all:
                yield j
        else:
            break
        i += 1


def array():
    for i in all_pages():
        text = i.find('span', class_="text").text
        author = i.find('small', class_="author").text
        author_link = i.find_all('a')[1].get('href')

        yield author, text, author_link
