import sqlite3


def sample():
    conn = sqlite3.connect("dictionary.db")
    cursor = conn.cursor()
    # cursor.execute("CREATE TABLE words (word text, definition text, pos text, collocations text, examples text)")
    cursor.execute(
        "INSERT INTO words VALUES ('make', 'to create or produce something', 'verb', 'make a mistake, make a difference, make a fortune', 'I need to make a phone call. She made a cake for her friend.')")
    cursor.execute(
        "INSERT INTO words VALUES ('book', 'a written or printed work consisting of pages bound together', 'noun', 'book a flight, book a hotel room, book a table', 'Can you book a table for two at 8 pm?')")
    # 提交事务。
    conn.commit()


def check(word):
    # 首先，你需要使用 sqlite3.connect() 函数打开一个连接。
    # 你需要提供数据库文件的路径作为参数。
    conn = sqlite3.connect("dictionary.db")
    # 然后，你可以使用 conn.cursor() 函数创建一个游标对象。
    cursor = conn.cursor()
    # 现在你可以使用游标对象来执行 SQL 语句。
    # 例如，你可以使用 cursor.execute() 函数执行一条 SELECT 语句，
    # 并使用 cursor.fetchall() 函数获取结果。
    cursor.execute("SELECT * FROM words WHERE word")
    results = cursor.fetchall()
    return results

    # 最后，记得关闭连接和游标对象。
    conn.close()
    cursor.close()

    # 现在你可以在 results 变量中使用结果了。
