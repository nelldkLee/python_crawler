from bs4 import BeautifulSoup

html = '''<table class="shopTable">
<tr>
<td>
<div class="shopInfo">
<div class="shopIconBox">

<span class=""></span>
</div>
<div class="shopName">강원춘천시퇴계점</div>
<div class="shopAdd">강원 춘천시 춘주로</div>
</div>
</td>
<td width='50'>
<div class="shopCall tooltip">
<a href="tel:033-242-8119"><br>전화</a>
<span class="tooltiptext">033-242-8119</span>
</div>
</td>
<td width='50'>
<div class="shopMap"><a href="JAVASCRIPT:codeAddress('강원도춘천시춘주로187번길20-4');"><br>지도보기</a></div>
</td>
</tr>
</table>
'''
bs = BeautifulSoup(html, 'html.parser')
shoptables = bs.findAll('table', attrs={'class': 'shopTable'})
for idx, shoptable in enumerate(shoptables):
    shopname = shoptable.find('div', attrs={'class': 'shopName'}).string
    shopaddress = shoptable.find('div', attrs={'class': 'shopAdd'}).string
    print(shoptable.a['href'].split('tel:')[1])
    print(idx+1, shopname, shopaddress, sep=':')
