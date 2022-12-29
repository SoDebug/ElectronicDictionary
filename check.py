import sqlite3
# 开始与数据库建立连接
# 如果数据库不存在，将会自动创建一个
connect = sqlite3.connect('database.db')
#
cursor = connect.cursor()
cursor.execute('SELECT pronunciation, pos, collocations, example FROM words WHERE word="make"')
result = cursor.fetchone()
pronunciation, pos, collocations, example = result
