from qgis.core import QgsMapLayer,QgsVectorLayer,QgsRasterLayer,QgsMapLayerType
from qgis.core import Qgis
from src.error import QgisReadError

def readGISDataByPath(path,datatype):
    if datatype == Qgis.LayerType.Vector:
        return QgsVectorLayer(path)
    elif datatype == Qgis.LayerType.Raster:
        return QgsRasterLayer(path)

    raise QgisReadError("数据读取错误")

def readTest(path):
    return QgsVectorLayer(path)


def addLayerToMap():
    return

if __name__ == "__main__":
    """"""
    path = "/data/test/cg_test.shp"
    # layer = QgsVectorLayer(path)
    # layer = QgsVectorLayer("E:\\Downloads\\mapabc\\呈贡区高德卫星04261503_L17\\呈贡区高德卫星04261503.tif")
    # layer = QgsRasterLayer("E:\\Downloads\\mapabc\\呈贡区高德卫星04261503_L17\\呈贡区高德卫星04261503.tif")
    layer = readTest(path)
    print(layer.crs())
