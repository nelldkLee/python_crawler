import os
import ssl
import sys
import time
from datetime import datetime
from itertools import count
from urllib.request import Request, urlopen

# import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

from collection import crawler


def crawling_pelicana():
    results = []

    for page in count(start=110):
        url = 'https://pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=&page=%d' % page
        html = crawler.crawling(url)
        bs = BeautifulSoup(html, 'html.parser')

        tag_table = bs.find('table', attrs={'class': 'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # 끝검출
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            sidogu = address.split()[:2]

            t = (name, address) + tuple(sidogu)
            results.append(t)

    # store
    #0,화명점,부산광역시 북구 화명동 1417-6,부산광역시,북구
    # table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    # table.to_csv('__results__/pelicana2.csv', encoding='utf-8', mode='w', index=True)


def crawling_nene():
    results = []
    overlapcheck = ''
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # for page in count(start=1):
    for page in range(1,5):
        stopcheck = False
        url = "https://nenechicken.com/17_new/sub_shop01.asp?page=%d&ex_select=1&ex_select2=&IndexSword=&GUBUN=A" % page
        try:
            request = Request(url)
            response = urlopen(request)
            receive = response.read()
            html = receive.decode('utf-8', errors='replace')
            print(f'{datetime.now()}: success for request [{url}]')
        except Exception as e:
            print(f'{e} : {datetime.now()}', file=sys.stderr)
            continue
        bs = BeautifulSoup(html, 'html.parser')
        shoptables = bs.findAll('table', attrs={'class': 'shopTable'})
        for idx, shoptable in enumerate(shoptables):
            shopname = shoptable.find('div',attrs={'class': 'shopName'}).string
            if idx == 0:
                if overlapcheck == shopname:
                    stopcheck = True
                    break
                else:
                    overlapcheck = shopname
            shopaddress = shoptable.find('div',attrs={'class': 'shopAdd'}).string
            sidogu = shopaddress.split()[:2]
            shoptel = shoptable.a['href'].split('tel:')[1]
            t = (shopname, shopaddress, shoptel) + tuple(sidogu)
            results.append(t)
        if stopcheck == True:
            break
    for result in results:
        print(result)
    # table = pd.DataFrame(results, columns=['name', 'address', 'telephone', 'sido', 'gugun'])
    #
    # table.to_csv('/root/crawling-results/nene.csv', encoding='utf-8', mode='w', index=True)


def crawling_kyochon():
    results = []
    for sido1 in range(1, 18):
        for sido2 in count(1):
            url='http://www.kyochon.com/shop/domestic.asp?sido1=%d&sido2=%d&txtsearch=' % (sido1, sido2)
            html = crawler.crawling(url)

            if html is None:
                break

            bs = BeautifulSoup(html, 'html.parser')
            tag_ul = bs.find('ul', attrs={'class': 'list'})
            tags_span = tag_ul.findAll('span', attrs={'class': 'store_item'})

            for tag_span in tags_span:
                strings = list(tag_span.strings)

                name = strings[1]
                address = strings[3].strip('\r\n\t')
                sidogu = address.split()[:2]

                results.append((name, address) + tuple(sidogu))

            # store
        # table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
        # table.to_csv('__results__/kyochon.csv', encoding='utf-8', mode='w', index=True)


def crawling_goobne():
    wd = webdriver.Chrome('/cafe24/chromedriver_win32/chromedriver.exe')
    wd.get('http://goobne.co.kr/store/search_store.jsp')
    time.sleep(3)
    results = []

    for page in count(1):
        # 자바스크립트 실행
        script = 'store.getList(%d)' % page
        wd.execute_script(script)
        print(f'{datetime.now()}: success for request [{script}]')
        time.sleep(1)

        # 실행결과 HTML(동적으로 랜더링 된 HTML) 가져오기
        html = wd.page_source
        bs = BeautifulSoup(html,'html.parser')
        tag_tbody = bs.find('tbody',attrs={'id': 'store_list'})
        tags_tr = tag_tbody.findAll('tr')

        # 마지막 페이지 검사
        if tags_tr[0].get('class') is None:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[6]
            sidogu = address.split()[:2]
            results.append((name, address) + tuple(sidogu))
    wd.quit()

    # table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    # table.to_csv('__results__/goobne.csv', encoding='utf-8', mode='w', index=True)
if __name__ == '__main__':
    # pelicana
    # crawling_pelicana()
    # crawling_kyochon()
    crawling_nene()
    # crawling_goobne()
