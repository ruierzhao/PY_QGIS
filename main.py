import time
import cgitb

cgitb.enable(format="text")

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QIcon
from qgis.core import QgsApplication

from src.widgets.splash import SplashScreen
from src.widgets.welcome import WelcomeForm
# from src.widgets.mainwindow import MainWindow
from src.widgets.systemtoolbar import SystemTray,loadSysToolBarIcon

# 适应高分辨率
QgsApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
# 设置窗口风格
QgsApplication.setStyle("Fusion")
QgsApplication.setPrefixPath(r"D:\installed\QGIS328")

# 创建app
app = QgsApplication([], True, platformName="desktop")

app.initQgis()

# 创建启动界面
splashScreen = SplashScreen()
splashScreen.show()

splashScreen.tipMessage("load file...")
# time.sleep(2)

# TODO 加载软件设置
# 加载系统任务栏图标
# SystemTray("./images/logo.ico")

# 创建主程序界面
welWin = WelcomeForm()
welWin.setWindowIcon(QIcon("./images/logo.ico"))
# mainWin = MainWindow()
# mainWin.setWindowIcon(QIcon("./images/logo.ico"))

loadSysToolBarIcon(app,welWin,"./images/logo.ico")


welWin.show()
# mainWin.show()

# 主程序界面加载完成后启动界面退出
splashScreen.finish(welWin)

# 运行app
app.exec_()
app.exitQgis()
