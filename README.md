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
## 软件界面UI展示
第一页

 ![Page1](https://github.com/SoDebug/ElectronicDictionary/blob/master/res/Page1.png)
 
第二页

 ![Page2](https://github.com/SoDebug/ElectronicDictionary/blob/master/res/Page2.png)
 
## 软件打包
- 使用`pyinstaller`打包，运行命令`pip install pyinstaller`以安装`pyinstaller`
- 打包命令```pyinstaller -F -w main.py --add-data database.db;.```
- 注意事项：本软件需要从外部访问数据库`database.db`,如果软件运行目录下无该数据库可能会引发闪退，因为目前暂未完善从网络中获取查询结果