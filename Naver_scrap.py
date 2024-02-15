import requests
from bs4 import BeautifulSoup
import re
import datetime as dt
from urllib import parse
import pandas as pd

def newsflash():
    """뉴스속보 받아오는 함수"""
    webpage = requests.get("https://finance.naver.com/news/news_list.naver?mode=LSS2D&section_id=101&section_id2=258")
    result = BeautifulSoup(webpage.content, "html.parser")

    newshead = result.select('dd.articleSubject')
    newssummary = result.select('dd.articleSummary')
    for ii, i in enumerate(newshead):
            print(i.text.strip())
            print(re.sub('\s{2,}','', newssummary[ii].text.strip()))
            print("")
    return

def targetnews(corp_name, startdate, enddate):
    """corp_name에 원하는 주제 넣으면 기사 긁어오는 함수"""
    corp_encoding = parse.quote_plus(corp_name, encoding='euc-kr')
    webpage = requests.get('https://finance.naver.com/news/news_search.naver?rcdate=&q='+corp_encoding+'&sm=title.basic&pd=3&stDateStart='+startdate+'&stDateEnd='+enddate) 
    result = BeautifulSoup(webpage.content, 'html.parser')

    newslist = result.select_one('dl.newsList')
    articlesubject = newslist.select('.articleSubject')
    articlesummary = newslist.select('.articleSummary')
    temp = []
    for ii, i in enumerate(articlesubject):
            temp.append(i.text.strip())
            # print(re.sub('\s{2,}','', articlesummary[ii].text.strip()))
            # print("")
    return temp


def newslink(corp_name, startdate, enddate):
    """corp_name에 원하는 주제 넣으면 기사 링크 긁어오는 함수"""
    corp_encoding = parse.quote_plus(corp_name, encoding='euc-kr')
    webpage = requests.get('https://finance.naver.com/news/news_search.naver?rcdate=&q='+corp_encoding+'&sm=title.basic&pd=3&stDateStart='+startdate+'&stDateEnd='+enddate) 
    result = BeautifulSoup(webpage.content, 'html.parser')
    newslist = result.select_one('dl.newsList')
    articlesubject = newslist.select('.articleSubject')
    articlesummary = newslist.select('.articleSummary')
    
    # url_base = "https://finance.naver.com/"+articlesubject[0].a.get('href')

    url_base_list = []
    for i in range(0, len(articlesubject)):
          url_base = "https://finance.naver.com/"+articlesubject[i].a.get('href')
          url_base_list.append(url_base)
    return url_base_list

enddate = dt.datetime.today()
startdate = enddate - dt.timedelta(days=30)
enddate = dt.datetime.strftime(enddate,'%Y-%m-%d')
startdate = dt.datetime.strftime(startdate,'%Y-%m-%d')

newshead, newslinks = targetnews('기준금리', startdate, enddate), newslink('기준금리',startdate, enddate)
combined_data = list(zip(newshead, newslinks))
df = pd.DataFrame(combined_data, columns=['News_Headline', 'News_Link'])

df


# df.to_excel('scrap.xlsx')