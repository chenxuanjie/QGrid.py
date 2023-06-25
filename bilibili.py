import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QVBoxLayout, QHBoxLayout, QRadioButton


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 最外层的垂直布局，包含两部分：爱好和性别
        container = QVBoxLayout()
        # 创建store组，将下载文件保存到本地
        storeBox = QGroupBox("保存到本地")
        #store组中用垂直布局
        storeBox_Vlayout = QVBoxLayout()
        btn1 = QRadioButton("默认")
        btn2 = QRadioButton("自定义下载目录")
        #将控件添加到layout中
        storeBox_Vlayout.addWidget(btn1)
        storeBox_Vlayout.addWidget(btn2)
        # 把v_layout添加到hobby_box中
        storeBox.setLayout(storeBox_Vlayout)

        #最后将所有组添加到最外层的布局中
        container.addWidget(storeBox)

        # 设置窗口显示的内容是最外层容器
        self.setLayout(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()