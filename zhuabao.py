import requests
import parsel

#1.确定URL地址
word=input("请输入你需要查询的单词：")
url = 'https://www.youdao.com/result'
print("请等待一下，你查询的是%s" % word)
params = {'word': '%s'%word ,'lang': 'en' }
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}


#2.发送请求
response = requests.get(url=url, params=params, headers=headers)
#print(response.request.headers)
html_data = response.text
#print(html_data)

#3.解析数据
#3.1转化数据类型（将html_data 转化成一个对象）
selector = parsel.Selector(html_data)
#3.2解析数据
lis = selector.xpath('//ul[@class="basic"]')
for li in lis:
    translation = li.xpath('//ul[@class="basic"]/li//span[@class="trans"]/text()').get()
    print("查询到的意思是:",translation)
