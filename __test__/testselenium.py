import time

import selenium
from selenium import webdriver

wd = webdriver.Chrome('D:/cafe24/chromedriver_win32/chromedriver.exe')
wd.get('http://goobne.co.kr/store/search_store.jsp')
time.sleep(2)
wd.execute_script('javascript:store.getList(\'%d\');' % (3))
time.sleep(2)
html = wd.page_source
print(html)

wd.quit()