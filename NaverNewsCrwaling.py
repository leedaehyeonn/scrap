###############실시간 뉴스 가져오기############
#############################################
import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://finance.naver.com/news/news_list.naver?mode=LSS2D&section_id=101&section_id2=258")
result = BeautifulSoup(webpage.content, "html.parser") #크롤링하려는 사이트의 개발자도구를 가져오는것

newshead = result.select('dd.articleSubject')
newssummary = result.select('dd.articleSummary')
for ii, i in enumerate(newshead):
        print(i.text.strip())
        print(re.sub('\s{2,}','', newssummary[ii].text.strip()))
        print("")


#방법1
print(result.dd.text)
#방법2 dd테그 안에있는 a테그만 가져오고 텍스트만 추출
print(result.dd.find_all('a'))
for i in result.dd.find_all('a'):
    print(i.text.strip())

###############################################
##############특정 종목 기사 가져오기###########
###############################################
import requests
from bs4 import BeautifulSoup
from urllib import parse #url 인코딩 형식을 바꿔야할 때

name = '진에어'
name_encoding = parse.quote_plus(name, encoding='euc-kr')
name_encoding

webpage = requests.get("https://finance.naver.com/news/news_search.naver?rcdate=&q="+name_encoding)
result = BeautifulSoup(webpage.content, "html.parser")
newslist = result.select_one('dl.newsList') #div 안에 있는 클래스 하나 가져오기
headline = newslist.select('.articleSubject')
for i in headline:
    print(i.text.strip())


###############################################
##############상세조건 기사 가져오기###########
###############################################
import requests
from bs4 import BeautifulSoup
from urllib import parse

corp_name = "네이버"
corp_encoding = parse.quote_plus(corp_name, encoding='euc-kr')
webpage = requests.get('https://finance.naver.com/news/news_search.naver?rcdate=&q='+corp_encoding+'&sm=title.basic&pd=3&stDateStart=2024-01-01&stDateEnd=2024-01-08') # 따옴표 하나로 하니까 되네,,
result = BeautifulSoup(webpage.content, 'html.parser')

newslist = result.select_one('dl.newsList')
articlesubject = newslist.select('.articleSubject')
articlesummary = newslist.select('.articleSummary')


for i in articlesubject:
    print(i.text.strip())
for i in articlesummary:
    print(i.text.strip())



articlesummary[0].text.strip() # 이걸 좀 보기 편하게 바꾸자.
import re

for ii, i in enumerate(articlesubject):
        print(i.text.strip())
        print(re.sub('\s{2,}','', articlesummary[ii].text.strip()))
        print("")



###############################################
####### href 레퍼런스로 기사 내용가져오기########
###############################################
import requests
from bs4 import BeautifulSoup
from urllib import parse

corp_name = "네이버"
corp_encoding = parse.quote_plus(corp_name, encoding='euc-kr')
webpage = requests.get('https://finance.naver.com/news/news_search.naver?rcdate=&q='+corp_encoding+'&sm=title.basic&pd=3&stDateStart=2024-01-01&stDateEnd=2024-01-08') # 따옴표 하나로 하니까 되네,,
result = BeautifulSoup(webpage.content, 'html.parser')

newslist = result.select_one('dl.newsList')
articlesubject = newslist.select('.articleSubject')
articlesummary = newslist.select('.articleSummary')
print(articlesubject[0]) #기사제목 구성요소 분석.. href
print(articlesubject[0].a.get('href')) # a테그에서 href 빼오기

url_base = "https://finance.naver.com/"+articlesubject[0].a.get('href')
webpage = requests.get(url_base)
result = BeautifulSoup(webpage.text, 'html.parser')
content = result.select_one('')
content = result.select_one('newsct_article _article_body')
result

