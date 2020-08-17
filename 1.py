import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36 SLBrowser/6.0.1.6181"
}
url = 'https://www.oneindia.com/search/results.html?q=gandi&tab=oneindia'
repose = requests.get(url=url,headers=headers).content
# repose.encoding = 'utf-8'
# re_txt = repose.content
tree = etree.HTML(repose)
zong = tree.xpath('//*[@class="search-m__section-container__23f3n"]')
for i in zong:

   print(title)
#https://www.oneindia.com/india/17th-lok-sabha-live-amit-shah-jk-recognisation-bill-in-lok-sabha-2905657.html?utm_source=/india/17th-lok-sabha-live-amit-shah-jk-recognisation-bill-in-lok-sabha-2905657.html&utm_medium=search_page&utm_campaign=elastic_search

