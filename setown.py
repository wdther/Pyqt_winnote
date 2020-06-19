import sys

from PyQt5.QtCore import Qt
#from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_set import Ui_MainWindow as Ui_set # 【UI】指的是UI文件的文件名
from Ui_chicken import Ui_MainWindow as Ui_chicken
from Ui_wjkblue import Ui_MainWindow as Ui_wjkblue
from Ui_wjkpink import Ui_MainWindow as Ui_wjkpink
from Ui_hxd import Ui_MainWindow as Ui_hxd
from Ui_ssm import Ui_MainWindow as Ui_ssm
from Ui_wlq import Ui_MainWindow as Ui_wlq




class PyQtLogic_set(QMainWindow, Ui_set):  # 构造函数，QMainWindows来自于 from

    def __init__(self):
        super(PyQtLogic_set, self).__init__()  # #首先找到子类（my转成QWidget的对象，然后被转化的self调用自己的init函数
        self.setupUi(self)  # #直接继承界面类，调用类的setupUi方法
    def choosepattern(self):
        parts=self.pattern.currentText()
        print(parts)
        if parts=='小鸡':
            self.chickenwindow = PyQtLogic_chicken() #注意此处要用self.xx 属性，不能用临时变量xx
            self.chickenwindow.show()
        elif parts=='王俊凯-蓝色':
            self.wjk1window = PyQtLogic_wjk1()
            self.wjk1window.show()
        elif parts=='王俊凯-红色':
            self.wjk2window = PyQtLogic_wjk2()
            self.wjk2window.show()
            print(parts)
        elif parts=='伍六七':
            self.wlqwindow = PyQtLogic_wlq()
            self.wlqwindow.show()
            print(parts)
        elif parts=='红小豆举牌':
            self.hxdwindow = PyQtLogic_hxd()
            self.hxdwindow.show()
            print(parts)
        elif parts=='少司命':
            self.ssmwindow = PyQtLogic_ssm()
            self.ssmwindow.show()
            print(parts)


class PyQtLogic_chicken(QMainWindow, Ui_chicken):  # 构造函数，QMainWindows来自于 from

    def __init__(self):
        super(PyQtLogic_chicken, self).__init__()  # #首先找到子类（my转成QWidget的对象，然后被转化的self调用自己的init函数
        self.setupUi(self)  # #直接继承界面类，调用类的setupUi方法


        # 这样的置顶窗口不会处于全屏窗口的上方，如果需要真正的置顶，
        #self.setWindowFlags(Qt.X11BypassWindowManagerHint)  # 可无视这个规则，但这样不会出现任务栏等，
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 让窗口一直置顶，并且这行代码要在透明代码的前面

        self.setAttribute(Qt.WA_TranslucentBackground)  # 透明效果
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框


        self.prev_pos = None
        self.ActionInit()
    def SetPattern(self):
        self.setwindow = PyQtLogic_set()  # 实例化类
        self.setwindow.show()
    def ActionInit(self):
        self.label.addAction(self.closeui)
        self.label.addAction(self.ontop)
        self.label.addAction(self.set)
        self.label_2.addAction(self.closeui)
        print('设置右键菜单')

    def WinOnTop(self,bool):
        if bool:
            print('窗口置顶')
            self.setAttribute(Qt.WA_TranslucentBackground)  # 透明效果
            # self.setWindowFlags(Qt.WindowStaysOnTopHint) #置顶
            #
            # self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
            self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint) #同时实现

            self.show()
        else:
            print('取消窗口置顶')
            self.setWindowFlags(self.windowFlags()) #取消置顶
            self.setAttribute(Qt.WA_TranslucentBackground)  # 透明效果
            self.setWindowFlags(Qt.FramelessWindowHint)  #
            self.show()
        print('窗口置顶')



    def mousePressEvent(self, e):
        self.prev_pos = e.globalPos()
    def mouseMoveEvent(self, e):
        if self.prev_pos:
            delta = e.globalPos() - self.prev_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.prev_pos = e.globalPos()
class PyQtLogic_wjk1(QMainWindow, Ui_wjkblue):  # 构造函数，QMainWindows来自于 from

    def __init__(self):
        super(PyQtLogic_wjk1, self).__init__()  # #首先找到子类（my转成QWidget的对象，然后被转化的self调用自己的init函数
        self.setupUi(self)  # #直接继承界面类，调用类的setupUi方法


        # 这样的置顶窗口不会处于全屏窗口的上方，如果需要真正的置顶，
        #self.setWindowFlags(Qt.X11BypassWindowManagerHint)  # 可无视这个规则，但这样不会出现任务栏等，
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 让窗口一直置顶，并且这行代码要在透明代码的前面

        self.setAttribute(Qt.WA_TranslucentBackground)  # 透明效果
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框


        self.prev_pos = None
        self.ActionInit()

    def SetPattern(self):
        self.setwindow = PyQtLogic_set()  # 实例化类
        self.setwindow.show()
    def ActionInit(self):
        self.label.addAction(self.closeui)
        self.label.addAction(self.ontop)
        self.label.addAction(self.set)
        self.label_2.addAction(self.closeui)
    def WinOnTop(self,bool):
        if bool:
            print('窗口置顶')
            self.setAttribute(Qt.WA_TranslucentBackground)  # 透明效果
            # self.setWindowFlags(Qt.WindowStaysOnTopHint) #置顶
            #
            # self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
            self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint) #同时实现

            self.show()
        else:
            print('取消窗口置顶')
            self.setWindowFlags(self.windowFlags()) #取消置顶
            self.setAttribute(Qt.WA_TranslucentBackground)  # 透明效果
            self.setWindowFlags(Qt.FramelessWindowHint)  #
            self.show()
        print('窗口置顶')



    def mousePressEvent(self, e):
        self.prev_pos = e.globalPos()
    def mouseMoveEvent(self, e):
        if self.prev_pos:
            delta = e.globalPos() - self.prev_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.prev_pos = e.globalPos()
class PyQtLogic_wjk2(QMainWindow, Ui_wjkpink):  # 构造函数，QMainWindows来自于 from

    def __init__(self):
        super(PyQtLogic_wjk2, self).__init__()  # #首先找到子类（my转成QWidget的对象，然后被转化的self调用自己的init函数
        self.setupUi(self)  # #直接继承界面类，调用类的setupUi方法


        # 这样的置顶窗口不会处于全屏窗口的上方，如果需要真正的置顶，
        #self.setWindowFlags(Qt.X11BypassWindowManagerHint)  # 可无视这个规则，但这样不会出现任务栏等，
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 让窗口一直置顶，并且这行代码要在透明代码的前面

        self.setAttribute(Qt.WA_TranslucentBackground)  # 透明效果
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框


        self.prev_pos = None
        self.ActionInit()

    def SetPattern(self):
        self.setwindow = PyQtLogic_set()  # 实例化类
        self.setwindow.show()
    def ActionInit(self):
        self.label.addAction(self.closeui)
        self.label.addAction(self.ontop)
        self.label.addAction(self.set)
        self.label_2.addAction(self.closeui)
    def WinOnTop(self,bool):
        if bool:
            print('窗口置顶')
            self.setAttribute(Qt.WA_TranslucentBackground)  # 透明效果
            # self.setWindowFlags(Qt.WindowStaysOnTopHint) #置顶
            #
            # self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
            self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint) #同时实现

            self.show()
        else:
            print('取消窗口置顶')
            self.setWindowFlags(self.windowFlags()) #取消置顶
            self.setAttribute(Qt.WA_TranslucentBackground)  # 透明效果
            self.setWindowFlags(Qt.FramelessWindowHint)  #
            self.show()
        print('窗口置顶')



    def mousePressEvent(self, e):
        self.prev_pos = e.globalPos()
    def mouseMoveEvent(self, e):
        if self.prev_pos:
            delta = e.globalPos() - self.prev_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.prev_pos = e.globalPos()
class PyQtLogic_hxd(QMainWindow, Ui_hxd):  # 构造函数，QMainWindows来自于 from

    def __init__(self):
        super(PyQtLogic_hxd, self).__init__()  # #首先找到子类（my转成QWidget的对象，然后被转化的self调用自己的init函数
        self.setupUi(self)  # #直接继承界面类，调用类的setupUi方法


        # 这样的置顶窗口不会处于全屏窗口的上方，如果需要真正的置顶，
        #self.setWindowFlags(Qt.X11BypassWindowManagerHint)  # 可无视这个规则，但这样不会出现任务栏等，
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 让窗口一直置顶，并且这行代码要在透明代码的前面

        self.setAttribute(Qt.WA_TranslucentBackground)  # 透明效果
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框


        self.prev_pos = None
        self.ActionInit()

    def SetPattern(self):
        self.setwindow = PyQtLogic_set()  # 实例化类
        self.setwindow.show()
    def ActionInit(self):
        self.label.addAction(self.closeui)
        self.label.addAction(self.ontop)
        self.label.addAction(self.set)
        self.label_2.addAction(self.closeui)
    def WinOnTop(self,bool):
        if bool:
            print('窗口置顶')
            self.setAttribute(Qt.WA_TranslucentBackground)  # 透明效果
            # self.setWindowFlags(Qt.WindowStaysOnTopHint) #置顶
            #
            # self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
            self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint) #同时实现

            self.show()
        else:
            print('取消窗口置顶')
            self.setWindowFlags(self.windowFlags()) #取消置顶
            self.setAttribute(Qt.WA_TranslucentBackground)  # 透明效果
            self.setWindowFlags(Qt.FramelessWindowHint)  #
            self.show()
        print('窗口置顶')



    def mousePressEvent(self, e):
        self.prev_pos = e.globalPos()
    def mouseMoveEvent(self, e):
        if self.prev_pos:
            delta = e.globalPos() - self.prev_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.prev_pos = e.globalPos()
class PyQtLogic_ssm(QMainWindow, Ui_ssm):  # 构造函数，QMainWindows来自于 from

    def __init__(self):
        super(PyQtLogic_ssm, self).__init__()  # #首先找到子类（my转成QWidget的对象，然后被转化的self调用自己的init函数
        self.setupUi(self)  # #直接继承界面类，调用类的setupUi方法


        # 这样的置顶窗口不会处于全屏窗口的上方，如果需要真正的置顶，
        #self.setWindowFlags(Qt.X11BypassWindowManagerHint)  # 可无视这个规则，但这样不会出现任务栏等，
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 让窗口一直置顶，并且这行代码要在透明代码的前面

        self.setAttribute(Qt.WA_TranslucentBackground)  # 透明效果
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框


        self.prev_pos = None
        self.ActionInit()

    def SetPattern(self):
        self.setwindow = PyQtLogic_set()  # 实例化类
        self.setwindow.show()
    def ActionInit(self):
        self.label.addAction(self.closeui)
        self.label.addAction(self.ontop)
        self.label.addAction(self.set)
        self.label_2.addAction(self.closeui)
    def WinOnTop(self,bool):
        if bool:
            print('窗口置顶')
            self.setAttribute(Qt.WA_TranslucentBackground)  # 透明效果
            # self.setWindowFlags(Qt.WindowStaysOnTopHint) #置顶
            #
            # self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
            self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint) #同时实现

            self.show()
        else:
            print('取消窗口置顶')
            self.setWindowFlags(self.windowFlags()) #取消置顶
            self.setAttribute(Qt.WA_TranslucentBackground)  # 透明效果
            self.setWindowFlags(Qt.FramelessWindowHint)  #
            self.show()
        print('窗口置顶')



    def mousePressEvent(self, e):
        self.prev_pos = e.globalPos()
    def mouseMoveEvent(self, e):
        if self.prev_pos:
            delta = e.globalPos() - self.prev_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.prev_pos = e.globalPos()
class PyQtLogic_wlq(QMainWindow, Ui_wlq):  # 构造函数，QMainWindows来自于 from

    def __init__(self):
        super(PyQtLogic_wlq, self).__init__()  # #首先找到子类（my转成QWidget的对象，然后被转化的self调用自己的init函数
        self.setupUi(self)  # #直接继承界面类，调用类的setupUi方法


        # 这样的置顶窗口不会处于全屏窗口的上方，如果需要真正的置顶，
        #self.setWindowFlags(Qt.X11BypassWindowManagerHint)  # 可无视这个规则，但这样不会出现任务栏等，
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 让窗口一直置顶，并且这行代码要在透明代码的前面

        self.setAttribute(Qt.WA_TranslucentBackground)  # 透明效果
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框


        self.prev_pos = None
        self.ActionInit()

    def SetPattern(self):
        self.setwindow = PyQtLogic_set()  # 实例化类
        self.setwindow.show()
    def ActionInit(self):
        self.label.addAction(self.closeui)
        self.label.addAction(self.ontop)
        self.label.addAction(self.set)
        self.label_2.addAction(self.closeui)
    def WinOnTop(self,bool):
        if bool:
            print('窗口置顶')
            self.setAttribute(Qt.WA_TranslucentBackground)  # 透明效果
            # self.setWindowFlags(Qt.WindowStaysOnTopHint) #置顶
            #
            # self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
            self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint) #同时实现

            self.show()
        else:
            print('取消窗口置顶')
            self.setWindowFlags(self.windowFlags()) #取消置顶
            self.setAttribute(Qt.WA_TranslucentBackground)  # 透明效果
            self.setWindowFlags(Qt.FramelessWindowHint)  #
            self.show()
        print('窗口置顶')



    def mousePressEvent(self, e):
        self.prev_pos = e.globalPos()
    def mouseMoveEvent(self, e):
        if self.prev_pos:
            delta = e.globalPos() - self.prev_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.prev_pos = e.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)  # pyqt窗口必须在QApplication方法中使用
    window = PyQtLogic_set()  # 实例化类

    #window.show()  # windows调用show方法
    window.show()
    sys.exit(app.exec_())  # #消息结束的时候，结束进程，并返回0，接着调用sys.exit(0)退出程序
