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
        # 最外层的水平布局，包含两部分：存储和下载
        container = QHBoxLayout()
        self.storeContainer(container=container)
        self.downloadContainer(container=container)

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

    def downloadContainer(self, container):
        """创建下载栏"""
        # 尝试创建新的组和布局
        download_box = QGroupBox()
        download_layout = QVBoxLayout()

        # 创建网址输入框
        download_label = QLabel("BiliBili视频网址：")
        download_url_edit = QLineEdit()
        download_url_edit.setPlaceholderText("请输入需要下载的视频网址")

        #创建水平布局器
        download_btn_layout = QHBoxLayout()
        # 创建”下载“按键
        download_btn = QPushButton("下载")
        download_btn_layout.addStretch(1)  # 伸缩器
        download_btn_layout.addWidget(download_btn)
        #创建可以显示下载信息的label
        showInfo = QLabel("222222")
        showInfo.resize(300, 300)

        # 将控件添加到布局中
        download_layout.addWidget(download_label)
        download_layout.addWidget(download_url_edit)
        download_layout.addLayout(download_btn_layout)
        download_layout.addWidget(showInfo)
        # 将垂直布局添加到download_box中
        download_box.setLayout(download_layout)
        # 将控件添加最外层的布局中
        container.addWidget(download_box)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.setWindowTitle("BiliBili爬虫")
    w.show()
    app.exec()
