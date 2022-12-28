# from PyQt5 import QtGui, QtWidgets, QtCore
# import sys
# import DataBase
#
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
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QPushButton, QLabel


# 拟实现多页面
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QPushButton, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建 QStackedWidget 对象。
        stacked_widget = QStackedWidget(self)

        # 创建第一个窗口页面，包含一个按钮。
        page1 = QWidget()
        button = QPushButton("Go to page 2", page1)
        button.clicked.connect(self.goToPage2)

        # 创建第二个窗口页面，包含一个文本标签。
        page2 = QWidget()
        label = QLabel("This is page 2", page2)

        # 将两个窗口页面添加到 QStackedWidget 中。
        stacked_widget.addWidget(page1)
        stacked_widget.addWidget(page2)

        # 设置第一个窗口页面为当前显示的窗口页面。
        stacked_widget.setCurrentIndex(0)

        # 创建布局并添加 QStackedWidget。
        layout = QVBoxLayout()
        layout.addWidget(stacked_widget)
        self.setLayout(layout)

    def goToPage2(self):
        # 获取 QStackedWidget 对象。
        stacked_widget = self.layout().itemAt(0).widget()
        # 设置第二个窗口页面为当前显示的窗口页面。
        stacked_widget.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())