from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QLineEdit, QHBoxLayout

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
        # 创建 QVBoxLayout 布局管理器
        layout = QHBoxLayout()
        # 创建 QV
        vbox = QVBoxLayout()
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
        # 插入伸展空间
        layout.insertStretch(0)
        # 将输入框插入布局管理器的第一个位置
        layout.insertWidget(2, self.lineedit)
        # 插入伸展空间
        # layout.insertStretch(1)
        # 将按钮插入布局管理器的第三个位置
        layout.insertWidget(3, self.button)
        # 插入伸展空间
        layout.insertStretch(4)
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
        # 创建 QVBoxLayout 布局管理器
        layout = QVBoxLayout()
        # 创建第一个 QLabel 组件
        self.label1 = QLabel("词性：动词")
        self.label1.setFixedHeight(20)
        # 创建第二个 QLabel 组件
        self.label2 = QLabel("意思：制作、建立、使成为")
        self.label2.setFixedHeight(20)
        # 创建第三个 QLabel 组件
        self.label3 = QLabel("常用搭配：make a mistake, make a point, make a difference")
        self.label3.setFixedHeight(20)
        # 创建第四个 QLabel 组件
        self.label4 = QLabel("例句：I'm going to make a cake for my mother's birthday.")
        self.label4.setFixedHeight(20)
        # 将第一个 QLabel 组件添加到布局管理器中
        layout.addWidget(self.label1)
        # 将第二个 QLabel 组件添加到布局管理器中
        layout.addWidget(self.label2)
        # 将第三个 QLabel 组件添加到布局管理器中
        layout.addWidget(self.label3)
        # 将第四个 QLabel 组件添加到布局管理器中
        layout.addWidget(self.label4)
        # 设置小部件的布局管理器
        self.setLayout(layout)

    def setQueryWord(self, query_word):
        # Set the application name to "你输入的单词是：[query_word]"
        QApplication.instance().setApplicationName(query_word)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()
    page1 = Page1()
    page2 = Page2()
    stacked_widget.addWidget(page1)
    stacked_widget.addWidget(page2)
    # 设置窗口大小
    stacked_widget.resize(400, 400)
    stacked_widget.show()
    sys.exit(app.exec_())
