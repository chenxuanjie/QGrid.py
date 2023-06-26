import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGroupBox, QVBoxLayout, QHBoxLayout,\
    QRadioButton, QLineEdit, QLabel, QPushButton


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("我是抽屉1要显示的内容", self)
        self.setStyleSheet("background-color:green;")


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()



    def init_ui(self):
        # 设置Widget大小以及固定宽高
        # self.setFixedSize(900, 900)
        self.createMenu()
        # 最外层的水平布局，包含两部分：存储和进度显示
        container = QHBoxLayout()
        self.storeContainer(container=container)

        #尝试创建新的组和布局
        test_box = QGroupBox()
        testContainer = QVBoxLayout()
        testbtn = QPushButton("按钮")
        # 创建显示的窗口，放在右边
        showWidget = QWidget()
        showWidget.resize(300, 300)

        testContainer.addWidget(showWidget)
        testContainer.addWidget(testbtn)
        test_box.setLayout(testContainer)

        #将控件添加最外层的布局中
        container.addWidget(test_box)
        #设置窗口为最外层
        widget = QWidget()
        # 设置窗口显示的内容是最外层容器
        widget.setLayout(container)
        self.setCentralWidget(widget)

    def createMenu(self):
        # 调用父类中的menuBar，从而对菜单栏进行操作
        menu = self.menuBar()
        # 设置菜单栏不与本地菜单栏合并
        menu.setNativeMenuBar(False)

        set_menu = menu.addMenu("设置")
        set_menu.addAction("高级")
        set_menu.addAction("打开")
        set_menu.addAction("保存")

    def storeContainer(self, container):
        """设置存储部分的布局"""
        # 创建store组，将下载文件保存到本地
        storeBox = QGroupBox("保存到本地")
        # store组中用垂直布局
        storeBox_Vlayout = QVBoxLayout()
        btn1 = QRadioButton("默认")
        btn2 = QRadioButton("自定义下载目录")
        edit_storePath = QLineEdit()
        edit_storePath.setPlaceholderText("请输入下载路径：")
        # 将控件添加到layout中
        storeBox_Vlayout.addWidget(btn1)
        storeBox_Vlayout.addWidget(btn2)
        storeBox_Vlayout.addWidget(edit_storePath)
        # 把v_layout添加到hobby_box中
        storeBox.setLayout(storeBox_Vlayout)

        # 最后将所有组添加到最外层的布局中
        container.addWidget(storeBox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.setWindowTitle("BiliBili爬虫")
    w.show()
    app.exec()
