set QGISPROFILR=D:\installed\QGIS316
set PYTHONHOME=%QGISPROFILR%\bin\python-qgis.bat

%PYTHONHOME% -m PyInstaller -w ^
--icon=images/logo.ico ^
--add-data="%QGISPROFILR%\apps\qgis\plugins;qgis\plugins" ^
--add-data="%QGISPROFILR%\apps\Python37\Lib\site-packages\PyQt5\*.pyd;PyQt5" ^
--add-data="%QGISPROFILR%\apps\qt5\plugins\styles;PyQt5\Qt\plugins\styles" ^
--add-data="%QGISPROFILR%\apps\qt5\plugins\iconengines;PyQt5\Qt\plugins\iconengines" ^
--add-data="%QGISPROFILR%\apps\qt5\plugins\imageformats;PyQt5\Qt\plugins\imageformats" ^
--add-data="%QGISPROFILR%\apps\qt5\plugins\platforms;PyQt5\Qt\plugins\platforms" ^
--add-data="%QGISPROFILR%\apps\qt5\plugins\platformthemes;PyQt5\Qt\plugins\platformthemes" ^
main.py