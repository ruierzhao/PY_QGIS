# -*- encoding: utf-8 -*-
"""
@File    :   utils.py
@Contact :   2656537241@qq.com
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/9/22 16:26   Ruier      1.0         None
"""
from qgis.core import QgsMapLayer, QgsVectorLayer, QgsFeatureRequest, QgsProject
from qgis.gui import QgsMapCanvas

def addLayer2MapCnavas(layer: QgsMapLayer, mapcanvas: QgsMapCanvas):
    """ 添加 QgsFeature 到地图 mapcnavas """
    if not layer.isValid():
        print(" RUIER DEBUG 待加载图层无效 ")
    else:
        Project = QgsProject.instance()
        Project.addMapLayer(layer)

        mapcanvas.setExtent(layer.extent())
        mapcanvas.setLayers([layer])
        mapcanvas.refresh()


def filterFeaturesByExpression(layer: QgsMapLayer, expression: str):  # VectorLayer
    """从当前layer中生成满足Expression 条件的新的 qgsmaplayer"""
    request = QgsFeatureRequest()
    request.setFilterExpression(expression)
    featureIterator = layer.getFeatures(request)  # QgsFeatureIterator

    newlayer = QgsVectorLayer(providerLib="memory")
    newlayer.addFeatures(featureIterator)

    return newlayer


def getLayers():
    if hasattr(QgsProject, "mapLayers"):
        return QgsProject.instance().mapLayers()
    else:
        print("QgsProject.mapLayers")


