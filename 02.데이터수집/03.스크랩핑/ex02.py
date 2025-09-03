import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

#[Top종목]-[거래상위]
tbody = soup.find('tbody', attrs={'id':'_topItems1'})
trs = tbody.find_all('tr')

list = []
for idx, tr in enumerate (trs):
    up_down = tr['class']
    name = tr.a.getText()
    tds = tr.find_all('td')
    price = tds[0].getText()
    up_down_price=tds[1].getText()
    # print(idx+1, name, price, up_down[0], up_down_price)
    list.append(f'{idx+1},{name},{price},{up_down[0]},{up_down_price}')
print(list)

file_name = 'data/거래상위.txt'
with open(file_name, 'a',encoding='utf-8')as file:
    for line in list:
        file.write(line + '\n')





