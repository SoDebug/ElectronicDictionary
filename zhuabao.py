import re
import requests
import csv
cookies = {
    'OUTFOX_SEARCH_USER_ID_NCOO': '1714357408.355476',
    'OUTFOX_SEARCH_USER_ID': '-1916015634@10.110.96.160',
    '__yadk_uid': 'FC9ysTH0iQwNBBf498Mx8WOmevuveMMY',
    'UM_distinctid': '1855762c8bbccc-02a70722986a89-26021151-1fa400-1855762c8bce7a',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1714357408.355476; OUTFOX_SEARCH_USER_ID=-1916015634@10.110.96.160; __yadk_uid=FC9ysTH0iQwNBBf498Mx8WOmevuveMMY; UM_distinctid=1855762c8bbccc-02a70722986a89-26021151-1fa400-1855762c8bce7a',
    'Origin': 'https://www.youdao.com',
    'Referer': 'https://www.youdao.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
word=input("请输入你需要查询的单词：")
print("请等待一下，你查询的是%s" % word)
params = {'word': '%s'%word ,'lang': 'en' }
response = requests.get('https://www.youdao.com/result', params=params, cookies=cookies, headers=headers).text
pronunciation=re.findall('<div class="per-phone".*?>.*?>(.*?)<.*?<span class="phonetic".*?>(.*?)<',response)
tarslation = re.findall('<span class="pos" .*?>(.*?)<.*?<span class="trans".*?>(.*?)<',response)
transformation = re.findall('<span class="wfs-name".*?>(.*?)<.*?<span class="wfs-splice".*?>.*?><.*?<span class="transformation".*?>(.*?)<',response)
phrase = re.findall('<a class="point".*?>(.*?)<',response)
example_sentence = re.findall('sentence:"(.*?)"',response)
print("发音是：\n",pronunciation,"\n这个单词的意思是：\n",tarslation,"\n各种变换形式：\n",transformation,"\n短语:\n",phrase,"\n例句：\n",example_sentence)

with open('查询数据.csv', mode='a', encoding ='utf-8', newline="")as f:
    csv_write = csv.writer(f)
    csv_write.writerow([pronunciation,tarslation,transformation,phrase,example_sentence])
