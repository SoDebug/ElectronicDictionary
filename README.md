# 项目介绍说明
## 软件环境
- `PyQt5`
- `Anaconda Python 3.8.15`
- `SQLite`
- `Pycharm 2022`
## 项目贡献者
- [李锦川](https://github.com/SoDebug)
- [项宇星](https://github.com/lamfls)
- [黄志杰](https://github.com/jazz6699)
- [王倩](https://github.com/7Kuku7)
## 项目实现框图
 ![程序框图](https://github.com/SoDebug/ElectronicDictionary/blob/master/res/%E7%A8%8B%E5%BA%8F%E6%A1%86%E5%9B%BE.jpg)

## 各部分模块详解
### 主程序【`main.py`】

- `UI`结构

    1) 使用 `PyQt5` 中的 `QStackedWidget` 容器窗口的特殊性，可以在其中堆叠多个小部件，不过只能显示其中一个小部件。 实现多页面功能（Page1和Page2）
    2) 其中`Page1`包含输入框和查询按钮，`Page2`包含查询的结果。

- `Page1`实现内容

    1) 输入框使用 QLineEdit 类创建:```self.lineedit = QLineEdit(self)```

    2) 按钮使用 QPushButton 类创建:```self.button = QPushButton("查询", self)```

    3) 为按钮设置点击信号和槽函数,同时捕获用户的输入，传递到`Page2`

    ```
    def onButtonClicked(self):
        # 获取输入的内容
        query_word = self.lineedit.text()
        # 设置当前显示的小部件为第二页
        stacked_widget.setCurrentIndex(1)
        # 将输入的内容传递到第二页
        page2.setQueryWord(query_word)
    ```
  
- `Page2`实现内容,并将应用名改变
    1) 接收来自`Page1`的输入字符:

    ```
    def setQueryWord(self, query_word):
        self.query_word = query_word
        self.parent().setWindowTitle("Dictionary - " + query_word)
    ```

    2) 将`Page1`查询结果刻化为不同的部件，显示在`Page2`中(使用`QV/QH`布局管理器管理)
    ```
    def setQueryWord(self, query_word):
        word, pronunciation, pos, otherforms, collocations, example = data 
        self.word = QLabel()
        self.word.setText("【单词】：" + word)
        ...            
        layout = QVBoxLayout()
        layout.addWidget(self.word)
    ```

- 布局管理器`QHBoxLayout()&QVBoxLayout()`

    1) `QVBoxLayout()`竖直布局管理器，在其中的控件均以铅锤（纵向）方式排列

    ```
    # 创建 QVBoxLayout 布局管理器
    layout_v = QVBoxLayout()
    # 将控件word加入QVBoxLayout布局管理器中
    layout_v.addWidget(self.word)
    # 使布局管理器显示在Page的布局中
    self.setLayout(layout_v)
    ```
    
    2) `QHBoxLayout()`水平布局管理器，在其中的控件均以水平（横向）方式排列

    ```
    # 创建 QHBoxLayout 布局管理器
    layout_h = QHBoxLayout()
    # 将控件word加入QHBoxLayout布局管理器中
    h_layout.addWidget(self.button)
    # QHBoxLayout 布局管理器 放入 QVBoxLayout 布局管理器 中
    layout.addLayout(h_layout)
    ```
  
- 控件位置设置

    1) 使用`move(x,y)`控制控件显示位置
    
    ```
    self.lineedit.move(90, 150)
    ```

    2) 使用`QHBoxLayout()/QVBoxLayout()`控制控件显示位置
    
    ```
    # 创建 QVBoxLayout 布局管理器
    layout_v = QVBoxLayout()
    # 将控件word加入QVBoxLayout布局管理器中
    layout_v.addWidget(self.word)
    # 使布局管理器显示在Page的布局中
    self.setLayout(layout_v)
    ```

    3) 使用`setGeometry(x,y,w,h)`控制控件显示位置    

    ```
    self.lineedit.setGeometry(50,120,40,20)
    ```

- Page1逻辑框图呈现

```mermaid
flowchart TD

A[Page1:用户输入] -->|"产生参数:query_word"| B(点击查询)
B --> C{"onButtonClicked()"}
C -->|"Action1:页面切换"| D[Page2:呈现查询内容]
C -->|"Action2:参数传递"| E[DataBase.py:数据库响应]
E[DataBase.py:数据库响应] -->|"传递查询结果:data[8]"| D[Page2:接收Page1信号]
```

- Page2逻辑框图呈现

```mermaid
flowchart TD

A[Page2:接收Page1信号] --> C{"setQueryWord()"}
C -->|"Action1:改变应用名(包含查询字符)"| D[Page2:呈现查询内容]
C -->|"Action2:接收数据库传递参数：data[8]"| E[Qlabel:解析参数]
E[Qlabel:解析参数] -->|"BoxLayout():排列控件"| D[Page2:呈现查询内容]
D[Page2:呈现查询内容] -->|完成| F(点击返回查询)
F(点击返回查询) --> G{"onButtonClicked()"}
G{"onButtonClicked()"} --> |Action1:页面切换| H(Page1)
G{"onButtonClicked()"} --> |Action2:删除Page2控件| H(Page1)
G{"onButtonClicked()"} --> |Action3:恢复应用名| H(Page1)
```

- 数据库处理模块逻辑框图

```mermaid
flowchart TD
A["DataBase.py:接收Page1信号"] -->|来自Page1的参数:query_word| C{"check()"}
C{"check()"} -->|本地数据库中存在query_word| D["data[8]:返回数据到Page2"]
C{"check()"} -->|本地数据库不存在query_word| E["联网查询：get_database()"]
E["联网查询：get_database()"] -->|传递参数:query_word| F["网络数据处理模块"]
F["网络数据处理模块"] -->|查询成功| G["返回数据到check():data[8]"]
G["返回数据到check():data[8]"] --> D["data[8]:返回数据到Page2"]
```

- 网络数据处理模块(requests & re)逻辑框图

```mermaid
flowchart TD
A["get_database():接收来自check()的参数"] -->|"来自check()的参数:query_word"| B["获取互联网查询数据并使用正则表达式初步过滤"]
B -->|"将参数data[6]、query_word传递给深度分析函数"| C["analyze()"]
C --> D{"深度分析函数群/解析函数群"}
D -->|Action1传递参数:query_word| K["添加字word"]
D -->|Action2传递参数:pos| E["get_meaning():解析单词意思"]
D -->|Action3传递参数:pronunciation| F["get_pronunciation():解析单词发音"]
D -->|Action4传递参数:pos| G["get_pos():解析单词词性"]
D -->|Action5传递参数:otherforms| H["get_otherforms():解析单词其他形式"]
D -->|Action6传递参数:collocations| I["get_collocations():解析单词搭配"]
D -->|Action7传递参数:example| J["get_example():解析单词例句"]
D -->|Action8传递参数:audio| W["get_audio():解析单词音频十六进制数据"]
E --> L{"数据整合:data[8]"}
F --> L
G --> L
H --> L
I --> L
J --> L
K --> L
W --> L
L -->|"参数传递:data[8]"| M["add_data()"]
L -->|"参数传递:data[8]"| N["数据返回至Page2"]
M --> O["数据库储存数据"]
```


## 软件界面UI展示
第一页

 ![Page1](https://github.com/SoDebug/ElectronicDictionary/blob/master/res/Page1.png)
 
第二页

 ![Page2](https://github.com/SoDebug/ElectronicDictionary/blob/master/res/Page2.png)
 
## 软件打包
- 使用`pyinstaller`打包，运行命令`pip install pyinstaller`以安装`pyinstaller`
- 打包命令```pyinstaller -F -w main.py --add-data database.db;.```
- 注意事项：本软件需要从外部访问数据库`database.db`,如果软件运行目录下无该数据库可能会引发闪退，~~因为目前暂未完善从网络中获取查询结果~~