import cgitb


cgitb.enable(format="text")

from PyQt5.QtWidgets import QSlider, QWidget, QHBoxLayout, QFileDialog
from qgis.core import (
    QgsFeature,
    QgsCategorizedSymbolRenderer,
    QgsSymbol,
    QgsRendererCategory,
    QgsColorRamp,
    QgsMessageLog,
    QgsRandomColorRamp,
)
from qgis.gui import QgsMapCanvas,QgsAuthAuthoritiesEditor

from qgis.PyQt.QtGui import QColor

from src.ui import Ui_showByAttrsForm
from src.utils import addLayer2MapCnavas
from src.GIS.qgislayer import VectorLayerSHP

class ShowByAttrsForm(QWidget,Ui_showByAttrsForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.vlayer: VectorLayerSHP = None
        self.attrs = []
        self.fields = []

        # 初始化地图画布
        self.mapCanvas = QgsMapCanvas(self)
        hl = QHBoxLayout(self.wgMap)
        hl.setContentsMargins(0, 0, 0, 0)
        hl.addWidget(self.mapCanvas)

        self.bind()

    def bind(self):
        # 加载数据按钮
        self.pbLoadFile.clicked.connect(self.onClickPbLoadFile)
        # 修改combox
        self.cbFields.currentTextChanged.connect(self.onCbFieldsTextChange)
        # 滑条值改变事件
        self.sldShowByAttrs.valueChanged.connect(self.sldValueChange)

    def onClickPbLoadFile(self):
        # try:
        #     filename = QFileDialog.getOpenFileName(self, "请选择shp文件", "", "file(*.shp)")#('D:/ZRL/ynlh_GIS/data/fmyzt/cg_test.shp', 'files(*.shp)')
        # except:
        #     raise PyQtError(" QFileDialog选择文件出错！")
        # filename = ("D:\\ZRL\\ynlh_GIS\\data\\fmyzt\\cg_test.shp",".shp")
        filename = (r"D:\ZRL\ynlh_GIS\data\showByAttrs\Export_Output.shp",".shp")
        if filename[0] == "":
            print("未选择文件")
        else:
            print("选择的文件：", filename[0])
            # 隐藏加载按钮
            self.pbLoadFile.hide()
            # 读取shp文件
            try:
                _layer = QgsVectorLayer(filename[0])

                self.vlayer = ChangesLayer(_layer)
                # 读取属性数据
                layerFields = self.vlayer.fields()
                # 属性显示到界面
                self.cbFields.addItems(layerFields)

                self.vlayer.initRenderer(self.cbFields.currentText())
                self.vlayer.updateRenderer(self.cbFields.currentText())
                self.vlayer.add2MapConvas(self.mapCanvas)

            except Exception as e:
                print(e," >> 读取vector 数据错误 ")


    def onCbFieldsTextChange(self, currentfield):
        """根据 field 获取属性值
        修改 slider 显示
        """
        self.attrs = self.vlayer.getUniqueValues(currentfield)

        # 更新slider
        self.__setSliderStyle()


    def __setSliderStyle(self):
        if self.attrs and len(self.attrs) != 0:
            # 设置刻度值
            self.sldShowByAttrs.setMinimum(0)
            self.sldShowByAttrs.setMaximum(len(self.attrs)-1)

            # 更改提示信息
            self.sldCurrentValue.setText("slider当前值：" + str(self.attrs[0]))
        else:
            self.sldShowByAttrs.setMaximum(0)
            self.sldCurrentValue.setText("当前属性值为空。")
            # todo: 显示所有地图

    def sldValueChange(self):
        """ sld 值改变
         1.修改 mapcanvas 显示
         2.显示attrs 属性值
        """
        if self.attrs and len(self.attrs) != 0:
            self.sldCurrentValue.setText("slider当前值：" + str(self.attrs[int(self.sldShowByAttrs.value())]))

        self.__getCategories(self.cbFields.currentText())


    def __getCategories(self,fieldname=None):
        """
        :param fieldname:
        :param slidervalue:
        :return:
        根据属性字段值和当前slider值渲染地图
        小于当前slidervalue值的透明度为0
        """
        categories = []
        rColor = QgsRandomColorRamp()
        for i,fieldvalue in enumerate(self.attrs):
            sym = QgsSymbol.defaultSymbol(self.vlayer.layer.geometryType())

            categories.append(QgsRendererCategory(str(fieldvalue), sym, str(fieldvalue)))

        renderer = QgsCategorizedSymbolRenderer(fieldname, categories)
        renderer.updateColorRamp(rColor)
        self.vlayer.layer.setRenderer(renderer)
        self.vlayer.layer.triggerRepaint()


from qgis.core import QgsMapLayer, QgsVectorLayer

class ChangesLayer:
    def __init__(self, layer: QgsMapLayer):
        self.layer = layer
        self.categories = []

    def fields(self) -> list[str]:
        return self.layer.fields().names()

    def getRenderer(self):
        return self.layer.renderer()

    def getColorRamps(self):
        """ 获取渲染色带 """
        # colorramp = QgsRandomColorRamp()
        # colors = []
        # for i in range(5):
        #     colors.append(colorramp.color(i))
        #     colorramp.value(i)
        #
        # print(colors)
        # return colors

    def initRenderer(self,field):
        """ 首次加载初始化为 Category 方式渲染
            保存渲染颜色
            combox值更改之后改变记录颜色
        """
        attrs = self.getUniqueValues(field)
        rColor = QgsRandomColorRamp()
        for i,value in enumerate(attrs):
            sym = QgsSymbol.defaultSymbol(self.layer.geometryType())
            sym.setColor(rColor.color(i))

            self.categories.append(QgsRendererCategory(attrs, sym, str(value)))

        return self.categories


    def updateRenderer(self,field):
        """ 更新需要显示的要素的渲染透明度 """
        renderer = QgsCategorizedSymbolRenderer(field, self.categories)

        self.layer.setRenderer(renderer)
        self.layer.triggerRepaint()

    def setLayerParentation(self):
        pass

    def getUniqueValues(self, field: str):
        """
            获取分类的layer
        """
        fieldidx = self.layer.fields().indexOf(field)
        return list(self.layer.uniqueValues(fieldidx))
    def add2MapConvas(self,mapCanvas):

        addLayer2MapCnavas(self.layer,mapCanvas)


if __name__ == '__main__':
    import os.path as osp
    path = r"D:\ZRL\ynlh_GIS\data\showByAttrs\Export_Output.shp"
    qvlayer = QgsVectorLayer(path, osp.basename(path), "ogr")
    clayer = ChangesLayer(qvlayer)
    clayer.getColorRamps()
    render = clayer.getRenderer()
    print(render)

