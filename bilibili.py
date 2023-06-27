import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("我是抽屉1要显示的内容", self)
        self.setStyleSheet("background-color:green;")


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.name = 'undefined'
        self.storePath = None
        self.url = None

        self.init_ui()

    def init_ui(self):
        # 设置Widget大小以及固定宽高
        self.setFixedSize(974, 633)
        self.createMenu()
        # 最外层的水平布局，包含两部分：存储和下载
        container = QHBoxLayout()
        self.storeContainer(container=container)
        self.downloadContainer(container=container)

        # 设置窗口为最外层
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
        btn1.toggle()
        # 默认状态下，存储地址锁定
        btn1.clicked.connect(self.store_notDisplay)
        btn2 = QRadioButton("自定义下载目录")
        btn2.clicked.connect(self.store_enableWrite) # 可输入存储路径
        self.edit_storeName = QLineEdit()
        self.edit_storeName.setPlaceholderText("请输入视频名称：")
        self.edit_storeName.textChanged.connect(self.store_setStoreName)  # 当有文本输入时，更改视频名称
        self.edit_storePath = QLineEdit()
        self.edit_storePath.setPlaceholderText("请输入下载路径：")
        self.edit_storePath.textChanged.connect(self.store_setStorePath)    # 当有文本输入时，更改存储路径

        # 将控件添加到layout中
        storeBox_Vlayout.addWidget(btn1)
        storeBox_Vlayout.addWidget(btn2)
        storeBox_Vlayout.addWidget(self.edit_storeName)
        storeBox_Vlayout.addWidget(self.edit_storePath)
        storeBox_Vlayout.addStretch(1)  #添加伸缩器，将内容固定在上方
        # 把v_layout添加到hobby_box中
        storeBox.setLayout(storeBox_Vlayout)

        # 最后将所有组添加到最外层的布局中
        container.addWidget(storeBox)

    def downloadContainer(self, container):
        """创建下载栏"""
        # 尝试创建新的组和布局
        download_box = QGroupBox()
        download_layout = QVBoxLayout()

        # 创建网址输入框
        download_label = QLabel("BiliBili视频网址：")
        self.download_url_edit = QLineEdit()
        self.download_url_edit.setPlaceholderText("请输入需要下载的视频网址")

        # 创建水平布局器
        download_btn_layout = QHBoxLayout()
        # 创建”下载“按键
        download_btn = QPushButton("下载")
        download_btn.clicked.connect(self.get_downloadUrl)
        download_btn_layout.addStretch(1)  # 伸缩器
        download_btn_layout.addWidget(download_btn)
        # 创建可以显示下载信息的label
        showInfo = QLabel("222222")
        showInfo.resize(300, 300)

        # 将控件添加到布局中
        download_layout.addWidget(download_label)
        download_layout.addWidget(self.download_url_edit)
        download_layout.addLayout(download_btn_layout)
        download_layout.addStretch(1)  #添加伸缩器，将内容固定在上方
        download_layout.addWidget(showInfo)
        # 将垂直布局添加到download_box中
        download_box.setLayout(download_layout)
        # 将控件添加最外层的布局中
        container.addWidget(download_box)

    def get_downloadUrl(self):
        """存储即将爬虫的网址"""
        self.url = self.download_url_edit.displayText()
        print(self.url)

    def store_notDisplay(self):
        """存储栏中选择默认时，无法在输入框输入内容"""
        #设置默认名称
        self.name = 'undefined'
        self.edit_storeName.clear()
        self.edit_storeName.insert(self.name)
        self.edit_storeName.setReadOnly(True)
        #设置默认路径
        self.storePath = os.getcwd()
        self.edit_storePath.clear()
        self.edit_storePath.insert(self.storePath)
        self.edit_storePath.setReadOnly(True)

    def store_enableWrite(self):
        """存储栏中，选择自定义目录时，清空输入框内容"""
        self.edit_storePath.setReadOnly(False)
        self.edit_storeName.setReadOnly(False)
        #清空默认名称和路径
        self.edit_storeName.clear()
        self.edit_storePath.clear()

    def store_setStoreName(self):
        """存储栏中，设置存储路径"""
        self.name = self.edit_storeName.displayText()
        print(self.name)

    def store_setStorePath(self):
        """存储栏中，设置存储路径"""
        self.storePath = self.edit_storePath.displayText()
        print(self.storePath)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.setWindowTitle("BiliBili爬虫")
    w.show()
    app.exec()
