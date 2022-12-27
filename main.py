from PyQt5 import QtGui, QtWidgets, QtCore
import sys

# 创建主进程
app = QtWidgets.QApplication(sys.argv)
# 创建主窗口
Main_Window = QtWidgets.QWidget()
Main_Window.setWindowTitle('Material Input Field')

# 创建布局管理器(QVBoxLayout：垂直)
layout = QtWidgets.QVBoxLayout()

# 使用表单数据管理器而不是简单的文本框
form_layout = QtWidgets.QFormLayout()
user_submit = QtWidgets.QLineEdit()
form_layout.addRow('', user_submit)
user_submit.setPlaceholderText('键入你想要查询的单词...')

layout.addLayout(form_layout)

# 创建查询提交按钮
submit_button = QtWidgets.QPushButton('查询')


# 获取输入内容
def get_raw():
    submit_words = user_submit.text()
    if submit_words == 'admin':
        QtWidgets.QMessageBox.information(Main_Window, '提示', '你查询的单词是admin，测试通过')
    else:
        QtWidgets.QMessageBox.critical(Main_Window, '错误', '输入字符非测试内容，或者提取字符出错')


submit_button.clicked.connect(get_raw)
layout.addWidget(submit_button)

# 将布局管理器设置到窗口中
Main_Window.setLayout(layout)

# 设置窗口大小
Main_Window.resize(400, 300)
# 显示窗口
Main_Window.show()

sys.exit(app.exec_())
