from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QHBoxLayout, QApplication, QWidget, QStackedWidget, QVBoxLayout, QPushButton, QLabel
import sys
import DataBase

# 定义第一页面的主要属性和初始化
class Page1(QWidget):
    def __init__(self):
        super().__init__()
        # 设置布局管理器为可选选项，
        # 如果self.option_Box = 0，则使用 self.lineedit.move 管理布局；
        # 如果 self.option_Box = 1 则使用布局管理器管理布局
        # 如果 self.option_Box = -1 则使用 setGeometry 管理布局
        self.option_Box = -1
        self.initUI()

# 按钮以及输入框的相关属性设置
    def initUI(self):
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
        if self.option_Box == 1:
            # 创建 QVBoxLayout 布局管理器
            layout = QHBoxLayout()
            # 创建 QV
            vbox = QVBoxLayout()
            # 插入伸展空间
            layout.insertStretch(0)
            # 将输入框插入布局管理器的第一个位置
            layout.insertWidget(2, self.lineedit)
            # 插入伸展空间
            layout.insertStretch(1)
            # 将按钮插入布局管理器的第三个位置
            layout.insertWidget(3, self.button)
            # 插入伸展空间
            layout.insertStretch(4)
            # 设置小部件的布局管理器
            self.setLayout(layout)
        elif self.option_Box == 0:
            self.lineedit.move(90, 150)
            self.button.move(180,200)
        elif self.option_Box == -1:
            # setGeometry(x,y,width,height)
            self.lineedit.setGeometry(50,120,40,20)
            self.button.setGeometry(140, 220, 40, 20)
            # 连接信号和槽函数
        self.button.clicked.connect(self.onButtonClicked)

    # 添加第一页按钮触发、输入框内容获取函数
    def onButtonClicked(self):
        # 获取输入的内容
        query_word = self.lineedit.text()
        # 设置当前显示的小部件为第二页
        stacked_widget.setCurrentIndex(1)
        # 将输入的内容传递到第二页
        page2.setQueryWord(query_word)
        # self.line_edit.clear()
        return query_word


class Page2(QWidget):
    def __init__(self):
        super().__init__()
        # 设置布局管理器为可选选项，
        # 如果self.option_Box == 0，则使用 self.lineedit.move 管理布局；
        # 如果 self.option_Box == 1 则使用布局管理器管理布局
        # 如果 self.option_Box = -1 则使用 setGeometry 管理布局
        self.option_Box = 1
        # self.initUI()

    # def setQueryWord(self, query_word):
    #     self.query_word = query_word
    #     key = self.query_word
    #     # Set the application name to "你输入的单词是：[query_word]"
    #     self.parent().setWindowTitle("Dictionary - " + query_word)

    # def initUI(self, data):
    # 现在的 setQueryWord() 代替原方法 initUI() 的职能
    # setQueryWord()：
    # （1）替换应用名
    # （2）绘制第二页面
    def setQueryWord(self, query_word):
        self.query_word = query_word
        # Set the application name to "你输入的单词是：[query_word]"
        self.parent().setWindowTitle("Dictionary - " + query_word)
        # 传递过来的数据应当是名为 data 的列表
        data = DataBase.check(self.query_word)
        # data = check.check(self.query_word)
        print(data)
        word, meaning, pronunciation, pos, otherforms, collocations, example = data
        # word, pronunciation, pos, otherforms, collocations, example = data
        # word, pronunciation, pos, collocations, example = data
        # # 创建 QVBoxLayout 布局管理器
        # layout = QVBoxLayout()
        # 创建第一个 QLabel 组件
        # 查询的单词本身
        self.word = QLabel()
        self.word.setText("【单词】：" + word)
        # 查询的单词意思
        self.meaning= QLabel()
        self.meaning.setText("【意思】：" + meaning)
        # 查询的发音
        self.pronunciation = QLabel()
        self.pronunciation.setText("【发音】：" + pronunciation)
        # 查询的词性
        self.pos = QLabel()
        self.pos.setText("【词性】：" + pos)
        # 查询该单词的其它形式
        self.otherforms = QLabel()
        self.otherforms.setText("【其它形式】：" + otherforms)
        # 查询的常用搭配
        self.collocations = QLabel()
        self.collocations.setWordWrap(True)
        self.collocations.setText("【常用搭配】：" + collocations)
        # self.collocations.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # 查询的例句
        self.example = QLabel()
        self.example.setWordWrap(True)
        # self.example.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.example.setText("【例句学习】：" + example)
        # self.example.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # 创建按钮
        self.button = QPushButton("返回查询", self)
        # 设置按钮的宽度
        self.button.setFixedWidth(100)
        # 设置按钮的高度
        self.button.setFixedHeight(30)

        if self.option_Box == 1:
            # 创建 QVBoxLayout 布局管理器
            layout = QVBoxLayout()
            # 将word, pronunciation, pos, otherforms, collocations, example添加到布局管理器中
            layout.addWidget(self.word)
            layout.addWidget(self.meaning)
            layout.addWidget(self.pronunciation)
            layout.addWidget(self.pos)
            layout.addWidget(self.otherforms)
            layout.addWidget(self.collocations)
            layout.addWidget(self.example)
            # 创建水平布局管理器并使按钮居中显示
            h_layout = QHBoxLayout()
            h_layout.addStretch()
            h_layout.addWidget(self.button)
            h_layout.addStretch()
            layout.addLayout(h_layout)
            # 设置小部件的布局管理器
            self.setLayout(layout)
            # 连接信号和槽函数
            self.button.clicked.connect(self.onButtonClicked)
        elif self.option_Box == 0:
            # 此种布局管理办法在 page2 中无法生效
            # self.word.move(490, 150)
            # self.pronunciation.move(180,200)
            # self.pos.move(180, 200)
            # self.collocations.move(180, 200)
            # self.example.move(180, 200)
            print("你正在使用一种无效的布局管理办法，请切换回布局管理器来管理此页面布局")
        elif self.option_Box == -1:
            # 此种布局管理办法在 page2 中无法生效
            # # setGeometry(x,y,width,height)
            # self.word.setGeometry(800,1000,40,20)
            # self.pronunciation.setGeometry(100,200,40,20)
            # self.pos.setGeometry(200,300,40,20)
            # self.collocations.setGeometry(300,400,40,20)
            # self.example.setGeometry(400,500,40,20)
            print("你正在使用一种无效的布局管理办法，请切换回布局管理器来管理此页面布局")

    # 添加第二页按钮的作用：返回查询界面继续查询单词
    # 在返回第一页时应当删除第二页中的所有小部件和布局
    # 否则后续的查询结果均显示为第一次查询的结果（没有刷新）
    def onButtonClicked(self):
        # 检索Page2中的布局
        layout = self.layout()
        # 检索Page2中所有的小部件
        children = self.findChildren(QWidget)
        # 删除Page2中所有的小部件，防止后续查询出现重影
        for widget in children:
            widget.deleteLater()
        # 删除Page2中的布局
        if layout is not None:
            layout.deleteLater()
        # 跳转到Page1以继续查询
        self.parent().setWindowTitle("Dictionary")
        stacked_widget.setCurrentIndex(0)



    def closeEvent(self, event):
        # 在这里添加你想要在关闭窗口时执行的代码
        # 比如将stacked_widget的当前小部件设为第一页
        stacked_widget.setCurrentIndex(0)
        event.accept()

    # def setQueryWord(self, query_word):
    #     self.query_word = query_word
    #     # Set the application name to "你输入的单词是：[query_word]"
    #     self.parent().setWindowTitle("Dictionary - " + query_word)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Dictionary")
    stacked_widget = QStackedWidget()
    page1 = Page1()
    page2 = Page2()
    stacked_widget.addWidget(page1)
    stacked_widget.addWidget(page2)
    # 设置窗口大小
    stacked_widget.resize(450, 300)
    stacked_widget.show()
    sys.exit(app.exec_())
