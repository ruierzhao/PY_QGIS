# -*- encoding: utf-8 -*-
"""
@File    :   qgislayer.py   
@Contact :   2656537241@qq.com
@License :   (C)Copyright 2018-2021
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/8/11 16:26   Ruier      1.0         None
"""
from abc import abstractmethod,ABCMeta
import os.path as osp

from qgis.core import(
    QgsProject,
    QgsVectorLayer,
    QgsField,
    QgsFeature
)
from qgis.gui import (
    QgsMapCanvas
)

VectorDataProvider = [
    "memory",  # scratchLayer = QgsVectorLayer("point?crs=epsg:4326&field=id:integer", "Scratch point layer",  "memory")
    "ogr",    # https://gdal.org/drivers/vector/index.html
    "spatialite",
    "postgres",
    "wfs",
    "mssql",
    "oapif",  # OGC
    "delimitedtext",
    "gpx",
    "grass"
]

# ############################### $Vector$ ###############################
class VetorLayer(metaclass=ABCMeta):
    def __init__(self):
        self.layer = None

    def fields(self) -> list[str]:
        return self.layer.fields().names()

    def addToMapCanvas(self, mapCanvas: QgsMapCanvas) -> None:
        if not self.layer.isValid():
            print(" RUIER DEBUG 待加载图层无效 ")
        else:
            Project = QgsProject.instance()
            Project.addMapLayer(self.layer)

            mapCanvas.setExtent(self.layer.extent())
            mapCanvas.setLayers([self.layer])
            mapCanvas.refresh()


    @abstractmethod
    def features(self) -> QgsFeature:
        pass

    @abstractmethod
    def getAttrsByFields(self, field: str) -> list:
        """ 根据 field 获取所有属性数组 """
        pass


class VectorLayerSHP(VetorLayer):
    def __init__(self, path,):
        """ 读取shp文件 """
        super().__init__()
        self.layer = QgsVectorLayer(path, osp.basename(path), "ogr")

    def addToMapCanvas(self, mapCanvas):
        super().addToMapCanvas(mapCanvas)

    def features(self) -> QgsFeature:
        return self.layer.getFeatures()

    def getAttrsByFields(self, field: str) -> list[str]:
        """ 通过 field 获取数据集的属性值数组 """
        if field not in self.fields():
            return []

        fs = self.features()
        return [f.attribute(field) for f in fs]

    def getUniqueValues(self, field: str):
        """
            获取分类的layer
        """
        fieldidx = self.layer.fields().indexOf(field)
        return list(self.layer.uniqueValues(fieldidx))


if __name__ == '__main__':
    shplayer = VectorLayerSHP(r"D:\ZRL\ynlh_GIS\data\showByAttrs\Export_Output.shp")
    fs = shplayer.getAttrsByFields("原编码")
    print(fs)

