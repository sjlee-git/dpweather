import os
from typing import Text
from bs4 import BeautifulSoup
import urllib.request as req

def naver():
    url = "https://weather.naver.com/"
    res = req.urlopen(url)
    soup = BeautifulSoup(res,"html.parser", from_encoding='euc-kr')

    
    temp = soup.select('strong.current')
    weather = soup.select('p.summary')
    weather2 = soup.select('dl.summary_list')
    lowest = soup.select('span.data.lowest')
    highest = soup.select('span.data.highest')
    finedust = soup.select('div.ttl_area > em.level_text')

    tempStr = str(temp)
    temp1 = tempStr.replace('[<strong class="current">','')
    temp2 = temp1.replace('<span class="blind">현재 온도</span>','')
    temp3 = temp2.replace('<span class="degree">°</span></strong>]','')

    lowestStr = str(lowest)
    lowest1 = lowestStr.replace('[<span class="data lowest">','')
    lowest2 = lowest1.replace('<span class="blind">평균기온</span>','')
    lowest3 = lowest2.replace('<span class="degree">°</span></span>]','')

    highestStr = str(highest)
    highest1 = highestStr.replace('[<span class="data highest">','')
    highest2 = highest1.replace('<span class="blind">평균기온</span>','')
    highest3 = highest2.replace('<span class="degree">°</span></span>]','')


    i = 0
    tags = []
    
    try:
        tags.append(temp3)
        tags.append(weather[i].text)
        tags.append(weather2[i].text)
        tags.append(lowest3)
        tags.append(highest3)
        tags.append(finedust[i].text)      

        keywords = [tag for tag in tags]

        i += 1
    except IndexError:
        pass
    return keywords