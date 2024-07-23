# -*- encoding: utf-8 -*-
"""
@File    :   test_xlwt.py
@Contact :   2656537241@qq.com
@License :   (C)Copyright 2018-2021
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/7 18:27   Ruier      1.0         None
"""
import sys

from qgis.PyQt.QtWidgets import QApplication
from qgis.PyQt.QtCore import Qt
from qgis.core import QgsApplication

from src.widgets.mainwindow import MainWindow

def qtapp():
    app = QApplication(sys.argv)
    mainwWD = MainWindow()
    mainwWD.show()
    sys.exit(app.exec_())

def qgisapp():
    QgsApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QgsApplication([],True,platformName="desktop")
    app.initQgis()
    app.setStyle("Cividis")

    mainWD = MainWindow()
    mainWD.show()
    app.exitQgis()
    app.exec_()
    print("正常退出")

def load_spatiallite():
    import sqlite3 as sqlite
    with sqlite.connect("test.sqlite")as conn:
        conn.enable_load_extension(True)
        conn.execute("SELECT load_extension('mod_spatialite')")

        print("Loading spatialite finish")

        cursor = conn.cursor()
        # cursor.execute('''CREATE TABLE test(id INTEGER PRIMARY KEY, name TEXT, geom BLOB);''')
        # cursor.execute('''SELECT AddGeometryColumn('test', 'geom', 4326, 'Point', 'XY');''')

        # 插入一些数据
        cursor.execute('''INSERT INTO test(name, geom) VALUES(?, ?)''', ('foo', 'POINT (10 20)'))  # 可以替换为你的数据和坐标
        cursor.execute('''INSERT INTO test(name, geom) VALUES(?, ?)''', ('bar', 'POINT (30 40)'))  # 可以替换为你的数据和坐标

        # 提交事务以保存更改
        conn.commit()
        # cursor.close()
        # conn.close()


if __name__ == '__main__':
    # qgisapp()
    load_spatiallite()