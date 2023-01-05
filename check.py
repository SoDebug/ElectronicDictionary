import sqlite3
import requests
from bs4 import BeautifulSoup

def check(query_word):
    # 连接数据库
    conn = sqlite3.connect('database.db')
    # 创建游标
    cursor = conn.cursor()
    # 执行查询语句
    cursor.execute("SELECT word, pronunciation, pos, collocations, example FROM words WHERE word=?", (query_word,))
    # 获取查询结果
    result = cursor.fetchone()
    # 如果查询结果为空，则返回一个包含 5 个字符 "null" 的列表
    if result is None:
        data = ["null", "null", "null", "null", "null"]
    else:
        # 将查询结果储存至列表 data 中
        data = list(result)
    return data
    # 关闭数据库连接
    conn.close()

# 获取发音音频文件,并以二进制形式的音频文件作为返回值
def get_audio(key_word):
    key = 'http://dict.youdao.com/dictvoice?type=0&audio=' + key_word
    response = requests.get(key)
    # 将音频文件写入文件
    with open('cache.mp3', 'wb') as f:
        f.write(response.content)
    # 读取音频文件的内容
    with open('cache.mp3', 'rb') as f:
        audio = f.read()
    return audio