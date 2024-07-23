from PyQt5.QtWidgets import QMainWindow, QMessageBox
from qgis.core import QgsVectorLayer,QgsProject
from qgis.PyQt.QtGui import QIcon


from src.ui import Ui_mainWindow
from .showByAttrFrame import ShowByAttrsForm


class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self,welWid):
        super().__init__()
        self.setupUi(self)
        self.showTuCengAction.setChecked(True)

        self.sbaForm = ShowByAttrsForm()
        self.bind()
        self.setWindowIcon(QIcon(":/icos/app.ico"))

        # 初始化完成销毁欢迎页面
        welWid.close()
        welWid.deleteLater()
        del welWid

    def bind(self):
        # 显示图层管理dock
        self.showTuCengAction.triggered.connect(self.showTuCengManager)
        # 显示地图展示子窗口
        self.mbShowByAttrs.triggered.connect(self.showFormapByArrts)
        # 加载矢量数据
        self.openShpAction.triggered.connect(self.onClickLoadVector)
        # 加载影像数据
        self.openRasterAction.triggered.connect(self.onClickLoadRaster)
        # 加载geojson数据
        self.openGeojsonAction.triggered.connect(self.onClickLoadGeojson)

    def onClickLoadVector(self):
        # TODO
        # self.welcomeForm.show()
        print("load vector")

    def onClickLoadRaster(self):
        # TODO
        print("load raster")

    def onClickLoadGeojson(self):
        # TODO
        print("load Geojson")

    def showTuCengManager(self):
        ischecked = self.showTuCengAction.isChecked()
        self.showTuCengAction.setChecked(ischecked)
        if ischecked:
            # 被勾选
            self.dockWidget.show()
        else:
            # 取消勾选
            self.dockWidget.hide()

    def showFormapByArrts(self):
        print("显示子窗口，显示加载按钮,清空fields")
        self.sbaForm.show()
        self.sbaForm.pbLoadFile.show()
        self.sbaForm.cbFields.addItems([])

    # 添加一个退出的提示事件
    # def closeEvent(self, event):
    #     # TODO 是否保存项目提示框
    #     reply = QMessageBox.question(self, 'Message', "确认关闭吗?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #     # 判断返回值，如果点击的是Yes按钮，我们就关闭组件和应用，否则就忽略关闭事件
    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()

