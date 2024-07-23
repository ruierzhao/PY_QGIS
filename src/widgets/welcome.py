# -*- encoding: utf-8 -*-
"""
@File    :   wel.py
@Contact :   2656537241@qq.com
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/9 15:40   Ruier      1.0         None
"""
import cgitb
cgitb.enable(format="text")

from qgis.PyQt.QtCore import QEasingCurve, QPropertyAnimation
from qgis.PyQt.QtWidgets import QMainWindow, QPushButton
from qgis.PyQt.QtCore import Qt

from src.ui import Ui_welcomForm
from .mainwindow import MainWindow
print("2rueir")

class Settings():
    # APP SETTINGS
    ENABLE_CUSTOM_TITLE_BAR = False
    MENU_WIDTH = 240
    LEFT_BOX_WIDTH = 240
    RIGHT_BOX_WIDTH = 240
    TIME_ANIMATION = 500

    # BTNS LEFT AND RIGHT BOX COLORS
    BTN_LEFT_BOX_COLOR = "background-color: rgb(44, 49, 58);"
    BTN_RIGHT_BOX_COLOR = "background-color: #ff79c6;"

    # MENU SELECTED STYLESHEET
    MENU_SELECTED_STYLESHEET = """
    border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
    background-color: rgb(40, 44, 52);
    """


class WelcomeForm(QMainWindow, Ui_welcomForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 设置窗口无默认边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.bind()

    def bind(self):
        # 关闭按钮
        self.closeAppBtn.clicked.connect(lambda: self.close())
        # 最小化
        self.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())
        # 左边栏切换
        self.toggleButton.clicked.connect(lambda: self.toggleMenu())
        # 打开主窗口
        self.pbNewKongbai_2.clicked.connect(lambda: self.toMainWin())
        # 左侧按钮
        self.btn_home.clicked.connect(self.buttonClick)
        self.btn_new.clicked.connect(self.buttonClick)
        self.btn_recent.clicked.connect(self.buttonClick)

    # ######################################## 左侧按钮切换 #################################################
    def selectMenu(self, getStyle):
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select

    def deselectMenu(self, getStyle):
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    def resetStyle(self, widget):
        for w in self.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(self.deselectMenu(w.styleSheet()))

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            self.stackedWidget.setCurrentWidget(self.home)
            self.resetStyle(btnName)
            btn.setStyleSheet(self.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_recent":
            self.stackedWidget.setCurrentWidget(self.widgets)
            self.resetStyle(btnName)
            btn.setStyleSheet(self.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            self.stackedWidget.setCurrentWidget(self.new_page)  # SET PAGE
            self.resetStyle(btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(self.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_save":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # ####################################################################################

    def toMainWin(self):
        # TODO 可以加一个加载提示
        self.mainWin = MainWindow(self)
        self.mainWin.show()
        self.hide()

    def toggleMenu(self):
        """ 左侧边栏切换 """
        # GET WIDTH
        width = self.leftMenuBg.width()
        maxExtend = Settings.MENU_WIDTH
        standard = 60
        # SET MAX WIDTH
        if width == 60:
            widthExtended = maxExtend
        else:
            widthExtended = standard

        # ANIMATION
        self.animation = QPropertyAnimation(self.leftMenuBg, b"minimumWidth")
        self.animation.setDuration(Settings.TIME_ANIMATION)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    welcomForm = WelcomeForm()
    welcomForm.show()
    app.exec_()
    sys.exit()
