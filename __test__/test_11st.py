# http://books.11st.co.kr/booksmall/BooksAction.tmall?method=&viewType=L&pageNum=1&pageRows=10&pageSize=240&kwd=&researchFlag=false&researchChkFlag=N&sortType=&sortCd=BPD&prdTab=T&lCtgrNo=0&mCtgrNo=0&sCtgrNo=0&dCtgrNo=0&dispCtgrNo=67177&dispCtgrCd=++&xzone=&minPrice=0&maxPrice=0&selMthdCd=&custBenefit=&dlvType=&buySatisfy=&goodsType=&kwdInCondition=&exceptKwdInCondition=&researchFlag=false&ctgrNo=67177&srCtgrNo=67177&clearAll=&schFrom=&referMethod=&naviAnchor=&ctgrType=&currCtgrTyp=#navi
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

keywords= ['파이썬', '자바스크립트', '리눅스','속 깊은']

request = Request('http://books.11st.co.kr/booksmall/BooksAction.tmall?method=&viewType=L&pageNum=1&pageRows=10&pageSize=240&kwd=&researchFlag=false&researchChkFlag=N&sortType=&sortCd=BPD&prdTab=T&lCtgrNo=0&mCtgrNo=0&sCtgrNo=0&dCtgrNo=0&dispCtgrNo=67177&dispCtgrCd=++&xzone=&minPrice=0&maxPrice=0&selMthdCd=&custBenefit=&dlvType=&buySatisfy=&goodsType=&kwdInCondition=&exceptKwdInCondition=&researchFlag=false&ctgrNo=67177&srCtgrNo=67177&clearAll=&schFrom=&referMethod=&naviAnchor=&ctgrType=&currCtgrTyp=#navi')
response = urlopen(request)
html = response.read().decode('cp949')
bs = BeautifulSoup(html, 'html.parser')
bookinfos = bs.findAll('div', attrs="pup_title")
for idx,bookinfo in enumerate(bookinfos):
    bookname = bookinfo.a.string.split()
    for keyword in keywords:
        if keyword in bookname:
            print(idx, bookname, sep=":")

