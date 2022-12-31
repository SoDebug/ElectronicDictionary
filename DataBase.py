import sqlite3
import re
import requests
from PyQt5.QtWidgets import QMessageBox, QApplication


def check(query_word):
    # 连接数据库
    conn = sqlite3.connect("database.db")
    # 创建游标
    cursor = conn.cursor()
    # 执行查询语句
    cursor.execute("SELECT word, pronunciation, pos, otherforms, collocations, example FROM words WHERE word=?",
                   (query_word,))
    # 获取查询结果
    result = cursor.fetchone()
    # 如果查询结果为空，则返回一个包含 6 个字符 "null" 的列表
    if result is None:
        # data = ["null", "null", "null", "null", "null", "null"]
        data = get_database(query_word)
    else:
        # 将查询结果储存至列表 data 中
        data = list(result)
    return data
    # 关闭数据库连接
    conn.close()


def get_database(query_word):
    print("正在尝试从互联网中读取数据...")
    try:
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
        word = query_word
        print("请等待一下，你查询的是%s" % word)
        params = {'word': '%s' % word, 'lang': 'en'}
        response = requests.get('https://www.youdao.com/result', params=params, cookies=cookies, headers=headers).text
        pronunciation = re.findall('<div class="per-phone".*?>.*?>(.*?)<.*?<span class="phonetic".*?>(.*?)<', response)
        tarslation = re.findall('<span class="pos" .*?>(.*?)<.*?<span class="trans".*?>(.*?)<', response)
        transformation = re.findall(
            '<span class="wfs-name".*?>(.*?)<.*?<span class="wfs-splice".*?>.*?><.*?<span class="transformation".*?>(.*?)<',
            response)
        phrase = re.findall('<a class="point".*?>(.*?)<', response)
        example_sentence = re.findall('sentence:"(.*?)"', response)
        print("发音是：", pronunciation, type(pronunciation[0]), "\n这个单词的意思是：", tarslation, "\n各种变换形式：",
              transformation, "\n短语:", phrase, "\n例句：", example_sentence)
        pronunciation = str(pronunciation[0] + pronunciation[1])
        print(pronunciation, type(pronunciation))
        data = ["1", "1", "1", "1", "1", "1"]
    except:
        # response = QMessageBox.question(None, '程序故障', '程序似乎无法连接到远程数据库，请检查网络！',
        #                                 QMessageBox.Yes | QMessageBox.No,
        #                                 QMessageBox.No)
        #
        # if response == QMessageBox.Yes:
        #     print('User clicked "Yes"')
        # else:
        #     print('User clicked "No"')
        QMessageBox.warning(None, '程序故障', '似乎无法连接到远程数据库？请检查网络后重试！')
        data = ["null", "null", "null", "null", "null", "null"]
    return data
