from PyQt5 import QtGui, QtWidgets, QtCore
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

# 创建应用
app = QtWidgets.QApplication(sys.argv)

# 创建窗口
window = QtWidgets.QWidget()
window.setWindowTitle('Material Input Field')


# 创建大标题
title = QtWidgets.QLabel('知道你在努力...')
# 设置大标题的字体
font = QtGui.QFont()
font.setPointSize(20)
font.setBold(True)
title.setFont(font)
# 设置大标题的颜色
palette = QtGui.QPalette()
palette.setColor(QtGui.QPalette.Foreground, QtGui.QColor(0, 0, 0))
title.setPalette(palette)

# 创建布局管理器(QVBoxLayout：垂直)
layout = QtWidgets.QVBoxLayout()

# 创建文本框
text_field = QtWidgets.QLineEdit()
text_field.setPlaceholderText('键入你想要查询的单词...')
# 设置输入框的最小宽高
text_field.setMinimumSize(100, 50)

# 设置文本框的颜色
palette = QtGui.QPalette()
palette.setColor(QtGui.QPalette.Base, QtGui.QColor(255, 255, 255))
text_field.setPalette(palette)

# 创建按钮
button = QtWidgets.QPushButton('查询')

# 设置按钮的颜色
palette = QtGui.QPalette()
palette.setColor(QtGui.QPalette.Button, QtGui.QColor(0, 150, 136))
button.setPalette(palette)

# 将文本框和按钮添加到布局管理器中
layout.addWidget(title, alignment=Qt.AlignCenter)
layout.addWidget(text_field)
layout.addWidget(button)

# 将布局管理器设置到窗口中
window.setLayout(layout)

# 设置窗口大小
window.resize(400, 300)
# 显示窗口
window.show()

sys.exit(app.exec_())
