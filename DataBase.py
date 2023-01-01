import sqlite3
import re
import requests
from PyQt5.QtWidgets import QMessageBox, QApplication
# 日志维护相关
import inspect
import logging
import time

logging.basicConfig(filename="log.txt", level=logging.INFO, format='%(asctime)s:%(message)s')


# DeBug: 用于获取当前函数名
def current_function_name():
    return inspect.stack()[1][3]


def check(query_word):
    try:
        # 连接数据库
        conn = sqlite3.connect("database.db")
        # 创建游标
        cursor = conn.cursor()
        # 执行查询语句
        cursor.execute(
            "SELECT word, meaning,pronunciation, pos, otherforms, collocations, example FROM words WHERE word=?",
            (query_word,))
        # 获取查询结果
        result = cursor.fetchone()
        # 如果查询结果为空，则返回一个包含 7 个字符 "null" 的列表
        if result is None:
            # data = ["null", "null", "null", "null", "null", "null", "null"]
            logging.info("{}: {}: [WARNING]本地数据库没有所需要查询的单词，尝试从互联网数据库中查询...".format(
                time.strftime("%Y-%m-%d %H:%M:%S"), current_function_name()))
            try:
                data = get_database(query_word)
                # print(data)
            except:
                logging.info("{}: {}: [ERROR]返回数据到UI界面时出错...".format(
                    time.strftime("%Y-%m-%d %H:%M:%S"), current_function_name()))
        else:
            # 将查询结果储存至列表 data 中
            logging.info(
                "{}: {}: [INFO]本地数据库检索成功！".format(time.strftime("%Y-%m-%d %H:%M:%S"), current_function_name()))
            data = list(result)
            # print(data)
        return data
        # 关闭数据库连接
        conn.close()
        logging.info("{}: {}: [INFO]Succeed".format(time.strftime("%Y-%m-%d %H:%M:%S"), current_function_name()))
    except:
        logging.info("{}: {}: [ERROR]FAILED".format(time.strftime("%Y-%m-%d %H:%M:%S"), current_function_name()))


def get_database(query_word):
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
        params = {'word': '%s' % word, 'lang': 'en'}
        response = requests.get('https://www.youdao.com/result', params=params, cookies=cookies, headers=headers).text
        pronunciation = re.findall('<div class="per-phone".*?>.*?>(.*?)<.*?<span class="phonetic".*?>(.*?)<', response)
        tarslation = re.findall('<span class="pos" .*?>(.*?)<.*?<span class="trans".*?>(.*?)<', response)
        transformation = re.findall(
            '<span class="wfs-name".*?>(.*?)<.*?<span class="wfs-splice".*?>.*?><.*?<span class="transformation".*?>(.*?)<',
            response)
        phrase = re.findall('<a class="point".*?>(.*?)<', response)
        example_sentence = re.findall('sentence:"(.*?)"', response)
        logging.info("{}: {}: [INFO]成功连接上互联网数据库接口...".format(time.strftime("%Y-%m-%d %H:%M:%S"),
                                                                          current_function_name()))
        data = [word, pronunciation, tarslation, transformation, phrase, example_sentence]
        try:
            # print("发音是：", pronunciation, type(pronunciation), "\n这个单词的意思是：", tarslation, "\n各种变换形式：",
            #       transformation, "\n短语:", phrase, "\n例句：", example_sentence)
            data = analyze(data, query_word)
            logging.info("{}: {}: [Succeed]数据分析成功！".format(time.strftime("%Y-%m-%d %H:%M:%S"),
                                                                 current_function_name()))
            # print(data)
            return data
        except:
            logging.info("{}: {}: [ERROR]取得数据后尝试分解数据时出错了...".format(time.strftime("%Y-%m-%d %H:%M:%S"),
                                                                                   current_function_name()))
        # print("发音是：", pronunciation, type(pronunciation), "\n这个单词的意思是：", tarslation, "\n各种变换形式：",
        #       transformation, "\n短语:", phrase, "\n例句：", example_sentence)
        # pronunciation = str(pronunciation[0] + pronunciation[1])
        # print(pronunciation, type(pronunciation))
        # data = ["1", "1", "1", "1", "1", "1"]

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
        logging.info("{}: {}: [ERROR]FAILED:无法与互联网数据库取得联系...".format(time.strftime("%Y-%m-%d %H:%M:%S"),
                                                                                  current_function_name()))
        data = ["null", "null", "null", "null", "null", "null", "null"]
    return data


def analyze(data, query_word):
    logging.info("{}: {}: [INFO]已取得互联网查询结果，尝试解析数据...".format(time.strftime("%Y-%m-%d %H:%M:%S"),
                                                                             current_function_name()))
    word, pronunciation, pos, otherforms, collocations, example = data
    # print("这个单词的意思是：", pos, "\n发音是：", pronunciation, type(pronunciation), "\n各种变换形式：",
    #       otherforms, "\n短语:", collocations, "\n例句：", example)
    # print(type(data))
    try:
        try:
            word = query_word
            meaning = get_meaning(pos)
            pronunciation = get_pronunciation(pronunciation)
            pos = get_pos(pos)
            otherforms = get_otherforms(otherforms)
            collocations = get_collocations(collocations)
            example = get_example(example)
        except:
            logging.info("{}: {}: [ERROR]FAILED:细节分析失败...".format(time.strftime("%Y-%m-%d %H:%M:%S"),
                                                                        current_function_name()))
        try:
            try:
                if not pronunciation:
                    pronunciation = "null"
                add_data(word, meaning, pronunciation, pos, otherforms, collocations, example)
                data = [word, meaning, pronunciation, pos, otherforms, collocations, example]
                return data
                # data = [word, pronunciation, pos, otherforms, collocations, example]
            except:
                logging.info("{}: {}: [ERROR]尝试为数据库刷新数据时出错...".format(time.strftime("%Y-%m-%d %H:%M:%S"),
                                                                                   current_function_name()))
        except:
            logging.info("{}: {}: [ERROR]FAILED:汇总数据时出错...".format(time.strftime("%Y-%m-%d %H:%M:%S"),
                                                                          current_function_name()))

    except:
        logging.info("{}: {}: [ERROR]FAILED:尝试进一步解析时出错...".format(time.strftime("%Y-%m-%d %H:%M:%S"),
                                                                            current_function_name()))
    return data


# 转用于分析数据的函数群

def get_pos(pos):
    result = []
    # 使用正则表达式获取词性
    for item in pos:
        if re.match(r'(n\.|adj\.|v\.|adv\.|prep\.|conj\.)', item[0]):
            result.append(item[0] + '/ ')
    pos = ''.join(result)[:-1]
    if not pos:
        pos = "null"
    # print(pos)
    return pos


def get_meaning(word):
    try:
        # print(word)
        result = []
        pattern = '(.+?)；'
        for t in word:
            match = re.match(pattern, t[1])
            if match:
                if match:
                    result.append(list(match.groups()))
        result = '、'.join([''.join(x) for x in result])
        # print(result)
        if not result:
            result = "null"
        return result

    except:
        logging.info("{}: {}: [ERROR]FAILED:解析函数内部出错...".format(time.strftime("%Y-%m-%d %H:%M:%S"),
                                                                        current_function_name()))


def get_pronunciation(pronunciation):
    # print("pronunciation:%s" % pronunciation)
    # print(type(pronunciation[1]))
    # print(pronunciation[1][1])
    try:
        temp = []
        result = []
        for item in pronunciation:
            for i in item:
                temp.append(i)
        if len(temp) > 2:
            result.append(temp[0] + ": " + temp[1])
            result.append(temp[2] + ": " + temp[3])
        elif len(temp) < 3:
            result.append(temp[0] + ": " + temp[1])
        result = '  '.join(result)
        # print(result)
        if len(result) == 0:
            result = "null"
        return result
    except:
        logging.info("{}: {}: [ERROR]FAILED:解析函数内部出错...".format(time.strftime("%Y-%m-%d %H:%M:%S"),
                                                                        current_function_name()))


def get_otherforms(otherforms):
    try:
        # print(otherforms)
        temp = []
        for item in otherforms:
            for i in item:
                temp.append(i)
        temp = temp[1::2]
        result = '|'.join(temp)
        # print(result)
        if not result:
            result = "null"
        return result
        # if len(otherforms)
    except:
        logging.info("{}: {}: [ERROR]FAILED:解析函数内部出错...".format(time.strftime("%Y-%m-%d %H:%M:%S"),
                                                                        current_function_name()))


def get_collocations(collocations):
    try:
        result = '|'.join(collocations)
        if len(result) == 0:
            result = "null"
        return result
        # print(result)
    except:
        logging.info("{}: {}: [ERROR]FAILED:解析函数内部出错...".format(time.strftime("%Y-%m-%d %H:%M:%S"),
                                                                        current_function_name()))


def get_example(example):
    try:
        result = '\n'.join(example)
        # print(result)
        if not result:
            result = "null"
        return result
    except:
        logging.info("{}: {}: [ERROR]FAILED:解析函数内部出错...".format(time.strftime("%Y-%m-%d %H:%M:%S"),
                                                                        current_function_name()))


def add_data(word, meaning, pronunciation, pos, otherforms, collocations, example):
    # Connect to the database
    conn = sqlite3.connect('database.db')

    # Create a cursor
    cursor = conn.cursor()

    # Verify data
    if not pronunciation:
        pronunciation = "null"

    # Insert the values into the table
    cursor.execute(
        "INSERT INTO words (word, meaning, pronunciation, pos, otherforms, collocations, example) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (word, meaning, pronunciation, pos, otherforms, collocations, example))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

# get_database("make")

# check("snake")

# add_data("蛇、蛇行，蜿蜒前进","英: / sneɪk /  美: / sneɪk /","n./ v./","snakes|snakes|snaking|snaked|snaked","grass snake|tiger snake|Snake River|snake venom|snake charmer|green snake","The snake slowly uncoiled.")
