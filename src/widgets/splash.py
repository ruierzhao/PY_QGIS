# -*- encoding: utf-8 -*-
"""
@File    :   splash.py   
@Contact :   eMac.li@cloudminds.com
@License :   (C)Copyright 2018-2021
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/7 18:24   Ruier     1.0         None
"""
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QPixmap
from qgis.PyQt.QtWidgets import QSplashScreen


class SplashScreen(QSplashScreen):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.setPixmap(QPixmap('./images/splash.png'))

    def mousePressEvent(self, event):
        pass
    def wheelEvent(self):
        super().wheelEvent()

    def tipMessage(self,msg:str):
        self.showMessage(msg,Qt.AlignHCenter|Qt.AlignBottom,Qt.white)



