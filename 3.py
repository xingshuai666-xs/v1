#https://www.freepressjournal.in/api/v1/search?q=fbl&offset=20&limit=10
# https://www.freepressjournal.in/api/v1/search?q=fbl&offset=30&limit=10
import requests
from lxml import etree
import datetime

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36 SLBrowser/6.0.1.6181"
}
url = 'https://www.freepressjournal.in/api/v1/search?q=gandis&offset=0&limit=30'
repose = requests.get(url=url,headers=headers).json()
print(repose)
for i in repose['results']['stories']:
    #标题
    print(i['headline'])
    #标题连接
    print('https://www.freepressjournal.in/'+i['slug'])
    # #时间
    print(datetime.datetime.fromtimestamp(int(i['last-published-at']/ 1000)))
    #摘要
    print(i['hero-image-caption'])
    # # 图片
    print('https://gumlet.assettype.com/'+i['hero-image-s3-key'])
#https://gumlet.assettype.com/freepressjournal/import/2018/09/Brett-Kavanaugh-US-CASE.jpg
# url = 'https://www.freepressjournal.in/route-data.json?path=%2Fsearch&q=fbi'
# repose = requests.get(url=url,headers=headers).json()
# print(repose)