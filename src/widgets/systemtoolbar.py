# -*- encoding: utf-8 -*-
"""
@File    :   systemtoolbar.py   
@Contact :   2656537241@qq.com
@License :   (C)Copyright 2018-2021
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/9/18 15:58   Ruier      1.0         None
"""
from PyQt5.QtWidgets import QSystemTrayIcon,QMenu,QAction
from PyQt5.QtGui import QIcon


class SystemTray:
    def __init__(self,image):
        self.trayIcon = QSystemTrayIcon(QIcon(image))

        self.menu = QMenu()

        self.init()

    def addMenuAction(self,menuAction):
        self.menu.addAction(menuAction)

    def init(self):
        actionTuichu = QAction("退出", self.menu)
        self.menu.addAction(actionTuichu)

        self.trayIcon.setContextMenu(self.menu)
        self.trayIcon.show()
    # 点击右键菜单项的处理函数
    def on_menu_action(self,action):
        if action == self.actionTuichu:
            # 处理“Show”菜单项的操作
            pass
        elif action == actionTuichu:
            # 处理“Quit”菜单项的操作
            pass

def loadSysToolBarIcon(app,w,image:str):
    trayIcon = QSystemTrayIcon(w)

    trayIcon.setIcon(QIcon(image))

    # 设置右键菜单
    menu = QMenu()
    actionTuichu = QAction("退出",menu)
    menu.addAction(actionTuichu)

    # 设置右键菜单
    trayIcon.setContextMenu(menu)

    def act(reason):
        # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
        if reason == 2 or reason == 3:
            w.show()
        print("系统托盘的图标被点击了",reason)
    trayIcon.activated.connect(act)

    # 显示右键菜单
    trayIcon.show()




