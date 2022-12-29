import sqlite3


def check(query_word):
    # 连接数据库
    conn = sqlite3.connect('database.db')
    # 创建游标
    cursor = conn.cursor()
    # 执行查询语句
    cursor.execute("SELECT word, pronunciation, pos, collocations, examole FROM test WHERE word=?", (query_word,))
    # 获取查询结果
    result = cursor.fetchone()
    # 如果查询结果为空，则返回一个包含 5 个字符 "null" 的列表
    if result is None:
        data = ["null", "null", "null", "null", "null"]
    else:
        # 将查询结果储存至列表 data 中
        data = list(result)
    # 关闭数据库连接
    conn.close()

