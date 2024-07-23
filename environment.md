# 基于 QGIS 3.32版本 二次开发产品

## windows环境
- python 解释器路径：%QGIS_PROFILE%/bin/python-qgis.bat
- qt-designer 路径：%QGIS_PROFILE%/bin/qgis-designer.bat

### 依赖路径
在qgis客户端中的python console中使用如下代码查看依赖路径,设置相应的 ```PYTHONPATH``` 环境变量
``` python
import sys
sys.path
"""
'%Userprofile%/AppData/Roaming/QGIS/QGIS3/profiles/default/python',
'%Userprofile%/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins',
'%Userprofile%/AppData/Roaming/QGIS/QGIS3/profiles/default/python'
'%QGIS_PROFILE%/bin',
'%QGIS_PROFILE%/bin/python37.zip',
'%QGIS_PROFILE%/apps/qgis/./python',
'%QGIS_PROFILE%/apps/qgis/./python/plugins',
'%QGIS_PROFILE%/apps/Python39',
'%QGIS_PROFILE%/apps/Python39/Scripts',
'%QGIS_PROFILE%/apps/Python39/DLLs',
'%QGIS_PROFILE%/apps/Python39/lib',
'%QGIS_PROFILE%/apps/Python39/lib/site-packages',
'%QGIS_PROFILE%/apps/Python39/lib/site-packages/win32',
'%QGIS_PROFILE%/apps/Python39/lib/site-packages/win32/lib',
'%QGIS_PROFILE%/apps/Python39/lib/site-packages/Pythonwin',
"""
```

### 临时环境变量设置
```sh
rem python_qgis.bat

rem o4w_env.bat
REM Make parent of this script location our current directory,
REM converting UNC path to drive letter if needed
pushd %~dp0
cd ..

REM set OSGEO4W_ROOT to short path version
for %%i in ("%CD%") do set OSGEO4W_ROOT=%%~fsi
:: for %i in ("D:\installed\QGIS316") do set OSGEO4W_ROOT=%~fsi 设置OSGEO4W_ROOT路径

REM start with clean path
set path=%OSGEO4W_ROOT%\bin;%WINDIR%\system32;%WINDIR%;%WINDIR%\system32\WBem

for %%f in ("%OSGEO4W_ROOT%\etc\ini\*.bat") do call "%%f"
:: 运行 D:\installed\QGIS316\etc\ini 下所有初始化 bat 文件
:: call "D:\installed\QGIS316\etc\ini\gdal.bat"
:: SET GDAL_DATA=D:\installed\QGIS316\share\gdal
:: SET GDAL_DRIVER_PATH=D:\installed\QGIS316\bin\gdalplugins 

:: call "D:\installed\QGIS316\etc\ini\libgeotiff.bat"
:: SET GEOTIFF_CSV=D:\installed\QGIS316\share\epsg_csv

:: call "D:\installed\QGIS316\etc\ini\libjpeg.bat"
:: set JPEGMEM=1000000

:: call "D:\installed\QGIS316\etc\ini\liblas.bat"
:: SET GDAL_DATA=D:\installed\QGIS316\share\gdal

:: call "D:\installed\QGIS316\etc\ini\msvcrt.bat"

:: call "D:\installed\QGIS316\etc\ini\proj.bat"
:: SET PROJ_LIB=D:\installed\QGIS316\share\proj

popd


rem qt5_env.bat
@echo off
path %OSGEO4W_ROOT%\apps\qt5\bin;%PATH%

set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\Qt5\plugins

set O4W_QT_PREFIX=%OSGEO4W_ROOT:\=/%/apps/Qt5
set O4W_QT_BINARIES=%OSGEO4W_ROOT:\=/%/apps/Qt5/bin
set O4W_QT_PLUGINS=%OSGEO4W_ROOT:\=/%/apps/Qt5/plugins
set O4W_QT_LIBRARIES=%OSGEO4W_ROOT:\=/%/apps/Qt5/lib
set O4W_QT_TRANSLATIONS=%OSGEO4W_ROOT:\=/%/apps/Qt5/translations
set O4W_QT_HEADERS=%OSGEO4W_ROOT:\=/%/apps/Qt5/include
set O4W_QT_DOC=%OSGEO4W_ROOT:\=/%/apps/Qt5/doc


rem py3_env.bat
SET PYTHONHOME=%OSGEO4W_ROOT%\apps\Python37
SET PYTHONPATH=%PYTHONHOME%;%PYTHONHOME%\Scripts
PATH %PYTHONPATH%;%PATH%


@echo off
path %OSGEO4W_ROOT%\apps\qgis\bin;%PATH%
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT:\=/%/apps/qgis
set GDAL_FILENAME_IS_UTF8=YES
rem Set VSI cache to be used as buffer, see #6448
set VSI_CACHE=TRUE
set VSI_CACHE_SIZE=1000000
set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\qgis\qtplugins;%OSGEO4W_ROOT%\apps\qt5\plugins
set PYTHONPATH=%OSGEO4W_ROOT%\apps\qgis\python;%PYTHONPATH%
"%PYTHONHOME%\python" %*

```


### 欢迎页面：
![img.png](images/designer/welcome.png)
### 新项目页面
![img.png](images/designer/newproject.png)
![img.png](images/designer/newproject2.png)
