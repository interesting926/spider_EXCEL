from urllib.request import urlopen
from bs4 import BeautifulSoup
from io import StringIO
import csv
import requests

# html = urlopen("http://www.chongzuo.gov.cn/bsfw/bmlqfw/jypx/t69598.shtml")
session = requests.Session()
headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate'
        }
url=input("输入网址:")
# url = "http://www.liuzhou.gov.cn/bsfw/msxg/jyky/xqjy/202008/t20200814_1915987.shtml"
req = session.get(url, headers=headers)
req.encoding = req.apparent_encoding
print(req)
bsObj =BeautifulSoup(req.text)
# bsObj = BeautifulSoup(html)
nameList = bsObj.findAll("tr")
name=input("请输入名字:")
with open("./柳州市/"+name+"初中.csv","w",encoding="utf-8",newline="") as fp:
    writer = csv.writer(fp)
    for name in nameList:
        cvsRow=[]
        for cell in name.findAll(["td","th"]):
            cvsRow.append(cell.get_text())
        writer.writerow(cvsRow)
    print(name.get_text())
    