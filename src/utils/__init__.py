from copy import deepcopy

from .qgis_utils import *

def unique(listdata):
    """ 1.数组去重 (使用对象)
        2.数组去重（排序取相邻比较）
        返回 listdata 数组的唯一值
    :param [2,3,4,5,2,7,5,4]
    :return [2,3,4,5,7]
    """
    def unique1(listdata):
        """ 只是去重 """
        return list({data:i for i, data in enumerate(listdata)}.keys())

    def unique2(listdata):
        """ 排序加去重 """
        # 原始数组排序
        listdata.sort()
        # 复制一份
        _listdata = list(listdata[1:])

        return [listdata[0]] + [data for i,data in enumerate(_listdata)if data != listdata[i]]

    if len(listdata) == 0:
        print(" RUIER DEBUG listdata 为空。。")
        return []

    if isinstance(listdata[0], str):
        # 字符串去重
        return unique1(listdata)
    if isinstance(listdata[0], (int,float)):
        # 数值 排序加 去重，也可以使用 unique1(listdata) 不排序
        return unique2(listdata)






if __name__ == '__main__':
    def test_listdata(listdata):
        c = unique(listdata)
        print(c)
    def test_():
        return 0

    test_listdata([2, 3, 4, 5, 2, 7, 5, 4])
    test_listdata(["rueir", "license", "dsh"])
