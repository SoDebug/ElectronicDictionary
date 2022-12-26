from PyQt5 import QtGui, QtWidgets, QtCore
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

# 创建应用
app = QtWidgets.QApplication(sys.argv)

# 创建窗口
Main_Window = QtWidgets.QWidget()
Main_Window.setWindowTitle('Material Input Field')


# 创建大标题
hello_words = QtWidgets.QLabel('知道你在努力...')
# 设置大标题的字体
font = QtGui.QFont()
font.setPointSize(18)
font.setBold(True)
hello_words.setFont(font)
# 设置大标题的颜色
palette = QtGui.QPalette()
palette.setColor(QtGui.QPalette.Foreground, QtGui.QColor(0, 0, 0))
hello_words.setPalette(palette)

# 创建布局管理器(QVBoxLayout：垂直)
layout = QtWidgets.QVBoxLayout()

# 创建文本框
text_field = QtWidgets.QLineEdit()
text_field.setPlaceholderText('键入你想要查询的单词...')
# 设置输入框的最小宽高
text_field.setMinimumSize(100, 40)

# 设置文本框的颜色
palette = QtGui.QPalette()
palette.setColor(QtGui.QPalette.Base, QtGui.QColor(255, 255, 255))
text_field.setPalette(palette)

# 创建按钮
user_submit = QtWidgets.QPushButton('查询')

# 设置按钮的颜色
palette = QtGui.QPalette()
palette.setColor(QtGui.QPalette.Button, QtGui.QColor(0, 150, 136))
user_submit.setPalette(palette)

# 将文本框和按钮添加到布局管理器中
layout.addWidget(hello_words, alignment=Qt.AlignCenter)
layout.addWidget(text_field)
layout.addWidget(user_submit)

# 将布局管理器设置到窗口中
Main_Window.setLayout(layout)

# 设置窗口大小
Main_Window.resize(400, 300)
# 显示窗口
Main_Window.show()

sys.exit(app.exec_())
