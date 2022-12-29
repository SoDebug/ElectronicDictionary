from PyQt5.QtWidgets import QLineEdit, QHBoxLayout, QMessageBox
# 拟实现多页面
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QPushButton, QLabel


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
            self.lineedit.setGeometry(50,100,40,20)
            self.button.setGeometry(140, 180, 40, 20)
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
        # 设置布局管理器为可选选项，
        # 如果self.option_Box == 0，则使用 self.lineedit.move 管理布局；
        # 如果 self.option_Box == 1 则使用布局管理器管理布局
        # 如果 self.option_Box = -1 则使用 setGeometry 管理布局
        self.option_Box = 0
        self.initUI()

    def initUI(self):
        result = ["1","2","3","4","5"]
        # # 创建 QVBoxLayout 布局管理器
        # layout = QVBoxLayout()
        # 创建第一个 QLabel 组件
        # 查询的单词本身
        self.word = QLabel()
        self.word.setText(result[0])
        # 查询的发音
        self.pronunciation = QLabel()
        self.pronunciation.setText(result[1])
        # 查询的词性
        self.pos = QLabel()
        self.pos.setText(result[2])
        # 查询的常用搭配
        self.collocations = QLabel()
        self.collocations.setText(result[3])
        # 查询的例句
        self.example = QLabel()
        self.example.setText(result[4])

        if self.option_Box == 1:
            # 创建 QVBoxLayout 布局管理器
            layout = QVBoxLayout()
            layout.addWidget(self.word)
            # 将第一个 QLabel 组件添加到布局管理器中
            layout.addWidget(self.pronunciation)
            # 将第二个 QLabel 组件添加到布局管理器中
            layout.addWidget(self.pos)
            # 将第三个 QLabel 组件添加到布局管理器中
            layout.addWidget(self.collocations)
            # 将第四个 QLabel 组件添加到布局管理器中
            layout.addWidget(self.example)
            # 设置小部件的布局管理器
            self.setLayout(layout)
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
    def closeEvent(self, event):
        # 在这里添加你想要在关闭窗口时执行的代码
        # 比如将stacked_widget的当前小部件设为第一页
        stacked_widget.setCurrentIndex(0)
        event.accept()

    def setQueryWord(self, query_word):
        self.query_word = query_word
        # Set the application name to "你输入的单词是：[query_word]"
        self.parent().setWindowTitle("Dictionary - " + query_word)


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
