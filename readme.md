# PY_QGIS
基于pyqt 和 QGIS二次开发的桌面GIS软件尝试。

## python interpreter
- qgis 3.16: D:\installed\QGIS316\bin\python-qgis.bat
- qgis 3.28: D:\installed\QGIS328\bin\python-qgis-ltr.bat

## project 结构                  
├─build      构建中间文件                          
│  └─main                         
├─data       测试数据文件夹                          
│  └─fmyzt                       
├─dist       最终打包结果                          
│  └─main                        
│      ├─PyQt5                   
│      │  └─Qt                   
│      │      ├─plugins          
│      │      │  ├─generic       
│      │      │  ├─iconengines   
│      │      │  ├─imageformats  
│      │      │  ├─platforms     
│      │      │  ├─platformthemes                   
│      │      │  └─styles        
│      │      └─translations     
│      └─qgis
│          └─plugins
├─images             项目图片                            
│  └─designer                    
├─scripts             项目最终打包脚本                 
├─snippet             代码片段               
├─src                项目源代码                    
│   ├─GIS              gis相关工具               
│       └─__pycache__
│   ├─resource         qt-designer 资源文件                               
│   ├─setting          项目设置相关代码                               
│   ├─test             测试代码                              
│   ├─ui               qt-designer构建的ui文件                      
│   |   └─__pycache__
│   ├─utils            项目工具文件夹                                  
│   │  └─__pycache__
│   ├─views            界面文件                               
│   │  └─__pycache__
│   └─error.py         项目错误定义                      
│   └─config.py        项目配置                         
└─main.py              入口文件            


## document


## 开发调试
```D:\installed\QGIS316\bin\python-qgis.bat main.py```

## coding notes:
> 编译完```ui```文件需要修改一下对应编译出的```py```文件的最后一行的qrc导入

## 项目打包
- https://blog.csdn.net/this_is_id/article/details/102974721
- https://blog.csdn.net/weixin_45953322/article/details/128774685

1. 安装pyintaller
```sh
# 进入qgis安装文件夹
python-qgis-ltr.bat -m pip pyinstaller
```
2. 打包项目
项目根目录下运行 ```script/build.bat```

3. 利用upx压缩exe（可选）
- https://github.com/upx/upx/releases/tag/v3.94


