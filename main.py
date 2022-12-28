from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import DataBase

# # 创建主进程
# app = QtWidgets.QApplication(sys.argv)
# # 创建主窗口
# Main_Window = QtWidgets.QWidget()
# Main_Window.setWindowTitle('Material Input Field')
# # 创建布局管理器(QVBoxLayout：垂直)
# layout = QtWidgets.QVBoxLayout()
#
# # 使用表单数据管理器而不是简单的文本框
# form_layout = QtWidgets.QFormLayout()
# user_submit = QtWidgets.QLineEdit()
# form_layout.addRow('', user_submit)
# user_submit.setPlaceholderText('键入你想要查询的单词...')
# layout.addLayout(form_layout)
# # 创建查询提交按钮
# submit_button = QtWidgets.QPushButton('查询')
#
#
# # 获取输入内容,这部分代码是测试用的代码
# # def get_raw():
# #     submit_words = user_submit.text()
# #     if submit_words == 'admin':
# #         QtWidgets.QMessageBox.information(Main_Window, '提示', '你查询的单词是admin，测试通过')
# #     else:
# #         QtWidgets.QMessageBox.critical(Main_Window, '错误', '输入字符非测试内容，或者提取字符出错')
#
# def check_raw():
#     # DataBase.sample()
#     content = DataBase.check()
#     judge = 0
#     if judge == 0:
#         QtWidgets.QMessageBox.information(Main_Window, '提示', str(content))
#     else:
#         QtWidgets.QMessageBox.critical(Main_Window, '错误', '输入字符非测试内容，或者提取字符出错')
#
#
# # submit_button.clicked.connect(check_raw)
# submit_button.clicked.connect(check_raw)
# layout.addWidget(submit_button)
#
# # 将布局管理器设置到窗口中
# Main_Window.setLayout(layout)
#
# # 设置窗口大小
# Main_Window.resize(400, 300)
# # 显示窗口
# Main_Window.show()
#
# sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit

# 拟实现多页面
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QPushButton, QLabel


# 定义第一页面的主要属性和初始化
class Page1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

# 按钮以及输入框的相关属性设置
    def initUI(self):
        # 使用 QVBoxLayout 布局管理器来管理控件的布局
        layout = QVBoxLayout()
        # 创建输入框
        self.lineedit = QLineEdit(self)
        self.lineedit.setPlaceholderText("键入所需查询单词...")
        # 设置输入框的宽度
        self.lineedit.setFixedWidth(300)
        # 设置输入框的高度
        self.lineedit.setFixedHeight(30)
        # 创建按钮
        self.button = QPushButton("查询", self)
        # 设置按钮的宽度
        self.button.setFixedWidth(100)
        # 设置按钮的高度
        self.button.setFixedHeight(30)
        # 将输入框和按钮添加到布局管理器中
        # # 并在输入框和按钮之间添加了伸展空间，使用输入框垂直居中，按钮紧靠底部
        # layout.addStretch()
        layout.addWidget(self.lineedit)
        # layout.addStretch()
        layout.addWidget(self.button)
        # 设置小部件的布局管理器
        self.setLayout(layout)
        # 连接信号和槽函数
        self.button.clicked.connect(self.onButtonClicked)

    def onButtonClicked(self):
        # 获取输入的内容
        query_word = self.lineedit.text()
        # 设置当前显示的小部件为第二页
        stacked_widget.setCurrentIndex(1)
        # 将输入的内容传递到第二页
        page2.setQueryWord(query_word)


class Page2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)

    def setQueryWord(self, query_word):
        # 在第二页中使用输入的内容
        self.label.setText("你输入的单词是：" + query_word)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()
    page1 = Page1()
    page2 = Page2()
    stacked_widget.addWidget(page1)
    stacked_widget.addWidget(page2)
    # 设置窗口大小
    stacked_widget.resize(400, 300)
    stacked_widget.show()
    sys.exit(app.exec_())
