# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_welcomForm(object):
    def setupUi(self, welcomForm):
        welcomForm.setObjectName("welcomForm")
        welcomForm.setWindowModality(QtCore.Qt.NonModal)
        welcomForm.resize(940, 560)
        welcomForm.setMinimumSize(QtCore.QSize(940, 560))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icos/app.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        welcomForm.setWindowIcon(icon)
        self.styleSheet = QtWidgets.QWidget(welcomForm)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet("QWidget{\n"
"    color: #333;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"QToolTip {\n"
"    color: #333;\n"
"    background-color: #f8f8f2;\n"
"    border: 1px solid #CCC;\n"
"    background-image: none;\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 2px solid rgb(255, 121, 198);\n"
"    text-align: left;\n"
"    padding-left: 8px;\n"
"    margin: 0px;\n"
"}\n"
"#bgApp {    \n"
"    background-color: #f8f8f2;\n"
"    border: 1px solid #CCC;\n"
"    color: #44475a;\n"
"    margin: 0;\n"
"}\n"
"#leftMenuBg {    \n"
"    background-color: #6272a4;\n"
"}\n"
"#topLogo {\n"
"    background-color: #6272a4;\n"
"    background-position: centered;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; color: #f8f8f2; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: #bd93f9; }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {    \n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"    background-color: #bd93f9;\n"
"}\n"
"#topMenu .QPushButton:pressed {    \n"
"    background-color: #ff79c6;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {    \n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 20px solid transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"    background-color: #bd93f9;\n"
"}\n"
"#bottomMenu .QPushButton:pressed {    \n"
"    background-color: #ff79c6;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"    border-top: 3px solid #6a7cb1;\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 20px solid transparent;\n"
"    background-color: #5b6996;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#toggleButton:hover {\n"
"    background-color: #bd93f9;\n"
"}\n"
"#toggleButton:pressed {    \n"
"    background-color: #ff79c6;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"#extraLeftBox {    \n"
"    background-color: #495474;\n"
"    color: #f8f8f2;\n"
"}\n"
"#extraTopBg{    \n"
"    background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"    border-top: 3px solid #6272a4;\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"    background-color: #5d6c99;\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {    \n"
"    background-color: rgb(189, 147, 249);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#contentTopBg{    \n"
"    background-color: #6272a4;\n"
"}\n"
"#contentBottom{\n"
"    border-top: 3px solid #bd93f9;\n"
"}\n"
"#titleRightInfo{\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: #bd93f9; border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: #ff79c6; border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: #495474; }\n"
"#themeSettingsTopDetail { background-color: #6272a4; }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: #495474 }\n"
"#bottomBar QLabel { font-size: 11px; color: #f8f8f2; padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"#contentSettings .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"    background-color: #5d6c99;\n"
"}\n"
"#contentSettings .QPushButton:pressed {    \n"
"    background-color: rgb(189, 147, 249);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QTableWidget {    \n"

"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: #9faeda;\n"
"    outline: none;\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: #9faeda;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: #9faeda;\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(189, 147, 249);\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section{\n"
"    background-color: #6272a4;\n"
"    max-width: 30px;\n"
"    border: none;\n"
"    border-style: none;\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: #6272a4;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid #6272a4;\n"
"    background-color: #6272a4;\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #6272a4;\n"
"}\n"
"QLineEdit {\n"
"    background-color: #6272a4;\n"
"    border-radius: 5px;\n"
"    border: 2px solid #6272a4;\n"
"    padding-left: 10px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #ff79c6;\n"
"}\n"
"QPlainTextEdit {\n"
"    background-color: #6272a4;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #ff79c6;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"    border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    width: 20px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    width: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: #6272a4;\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {    \n"
"    background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"    border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: #6272a4;\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"     height: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid #6272a4;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: #6272a4;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"    border: 3px solid #bd93f9;    \n"
"    background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid #6272a4;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: #6272a4;\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"    border: 3px solid #bd93f9;    \n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"    background-color: #6272a4;\n"
"    border-radius: 5px;\n"
"    border: 2px solid #6272a4;\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid #7284b9;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px; \n"
"    border-left-width: 3px;\n"
"    border-left-color: #6272a4;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;    \n"
"    background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(255, 121, 198);    \n"
"    background-color: #6272a4;\n"
"    padding: 10px;\n"
"    selection-background-color: #6272a4;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    background-color: #6272a4;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: #6272a4;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    background-color: #6272a4;\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"    background-color: #6272a4;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"#pagesContainer QCommandLinkButton {    \n"
"    color: rgb(255, 121, 198);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    border: 2px solid #ff79c6;\n"
"    color: #ff79c6;\n"
"}\n"
"#pagesContainer QCommandLinkButton:hover {    \n"
"    color: rgb(255, 170, 255);\n"
"    background-color: #6272a4;\n"
"}\n"
"#pagesContainer QCommandLinkButton:pressed {    \n"
"    color: rgb(189, 147, 249);\n"
"    background-color: #586796;\n"
"}\n"
"#pagesContainer QPushButton {\n"
"    border: 2px solid #6272a4;\n"
"    border-radius: 5px;    \n"
"    background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"    background-color: #7082b6;\n"
"    border: 2px solid #7082b6;\n"
"}\n"
"#pagesContainer QPushButton:pressed {    \n"
"    background-color: #546391;\n"
"    border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"\n"
"")
        self.styleSheet.setObjectName("styleSheet")
        self.appMargins = QtWidgets.QVBoxLayout(self.styleSheet)
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName("appMargins")
        self.bgApp = QtWidgets.QFrame(self.styleSheet)
        self.bgApp.setStyleSheet("")
        self.bgApp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bgApp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bgApp.setObjectName("bgApp")
        self.appLayout = QtWidgets.QHBoxLayout(self.bgApp)
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName("appLayout")
        self.leftMenuBg = QtWidgets.QFrame(self.bgApp)
        self.leftMenuBg.setMinimumSize(QtCore.QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QtCore.QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftMenuBg.setObjectName("leftMenuBg")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.topLogoInfo = QtWidgets.QFrame(self.leftMenuBg)
        self.topLogoInfo.setMinimumSize(QtCore.QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QtCore.QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topLogoInfo.setObjectName("topLogoInfo")
        self.topLogo = QtWidgets.QFrame(self.topLogoInfo)
        self.topLogo.setGeometry(QtCore.QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QtCore.QSize(42, 42))
        self.topLogo.setMaximumSize(QtCore.QSize(42, 42))
        self.topLogo.setStyleSheet("#topLogo{background:url(:/dracula/images/PyDracula.png)}")
        self.topLogo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.topLogo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topLogo.setObjectName("topLogo")
        self.titleLeftApp = QtWidgets.QLabel(self.topLogoInfo)
        self.titleLeftApp.setGeometry(QtCore.QRect(70, 8, 160, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.titleLeftApp.setFont(font)
        self.titleLeftApp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.titleLeftApp.setObjectName("titleLeftApp")
        self.titleLeftDescription = QtWidgets.QLabel(self.topLogoInfo)
        self.titleLeftDescription.setGeometry(QtCore.QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.titleLeftDescription.setFont(font)
        self.titleLeftDescription.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.titleLeftDescription.setObjectName("titleLeftDescription")
        self.verticalLayout_3.addWidget(self.topLogoInfo)
        self.leftMenuFrame = QtWidgets.QFrame(self.leftMenuBg)
        self.leftMenuFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftMenuFrame.setObjectName("leftMenuFrame")
        self.verticalMenuLayout = QtWidgets.QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName("verticalMenuLayout")
        self.toggleBox = QtWidgets.QFrame(self.leftMenuFrame)
        self.toggleBox.setMaximumSize(QtCore.QSize(16777215, 45))
        self.toggleBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toggleBox.setObjectName("toggleBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.toggleButton = QtWidgets.QPushButton(self.toggleBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toggleButton.setStyleSheet("background-image:url(:/dracula/icons/cil-arrow-circle-right.png);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/dracula/icons/cil-arrow-circle-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toggleButton.setIcon(icon1)
        self.toggleButton.setObjectName("toggleButton")
        self.verticalLayout_4.addWidget(self.toggleButton)
        self.verticalMenuLayout.addWidget(self.toggleBox)
        self.topMenu = QtWidgets.QFrame(self.leftMenuFrame)
        self.topMenu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.topMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topMenu.setObjectName("topMenu")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.btn_home = QtWidgets.QPushButton(self.topMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_home.setStyleSheet("background-image: url(:/dracula/icons/cil-home.png);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/dracula/icons/icon_restore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home.setIcon(icon2)
        self.btn_home.setObjectName("btn_home")
        self.verticalLayout_8.addWidget(self.btn_home)
        self.btn_recent = QtWidgets.QPushButton(self.topMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_recent.sizePolicy().hasHeightForWidth())
        self.btn_recent.setSizePolicy(sizePolicy)
        self.btn_recent.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_recent.setFont(font)
        self.btn_recent.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_recent.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_recent.setStyleSheet("background-image:url(:/dracula/icons/cil-layers.png);")
        self.btn_recent.setObjectName("btn_recent")
        self.verticalLayout_8.addWidget(self.btn_recent)
        self.btn_new = QtWidgets.QPushButton(self.topMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_new.setStyleSheet("background-image:url(:/dracula/icons/cil-file.png);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/dracula/icons/cil-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_new.setIcon(icon3)
        self.btn_new.setObjectName("btn_new")
        self.verticalLayout_8.addWidget(self.btn_new)
        self.btn_exit = QtWidgets.QPushButton(self.topMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_exit.setStyleSheet("background-image:url(:/dracula/icons/cil-account-logout.png) ;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/dracula/icons/cil-account-logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_exit.setIcon(icon4)
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout_8.addWidget(self.btn_exit)
        self.verticalMenuLayout.addWidget(self.topMenu, 0, QtCore.Qt.AlignTop)
        self.bottomMenu = QtWidgets.QFrame(self.leftMenuFrame)
        self.bottomMenu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomMenu.setObjectName("bottomMenu")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.toggleLeftBox = QtWidgets.QPushButton(self.bottomMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet("background-image:url(:/dracula/icons/icon_settings.png)")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/dracula/icons/icon_settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toggleLeftBox.setIcon(icon5)
        self.toggleLeftBox.setObjectName("toggleLeftBox")
        self.verticalLayout_9.addWidget(self.toggleLeftBox)
        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_3.addWidget(self.leftMenuFrame)
        self.appLayout.addWidget(self.leftMenuBg)
        self.extraLeftBox = QtWidgets.QFrame(self.bgApp)
        self.extraLeftBox.setMinimumSize(QtCore.QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QtCore.QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extraLeftBox.setObjectName("extraLeftBox")
        self.extraColumLayout = QtWidgets.QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName("extraColumLayout")
        self.extraTopBg = QtWidgets.QFrame(self.extraLeftBox)
        self.extraTopBg.setMinimumSize(QtCore.QSize(0, 50))
        self.extraTopBg.setMaximumSize(QtCore.QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extraTopBg.setObjectName("extraTopBg")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.extraTopLayout = QtWidgets.QGridLayout()
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setObjectName("extraTopLayout")
        self.extraIcon = QtWidgets.QFrame(self.extraTopBg)
        self.extraIcon.setMinimumSize(QtCore.QSize(20, 0))
        self.extraIcon.setMaximumSize(QtCore.QSize(20, 20))
        self.extraIcon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extraIcon.setObjectName("extraIcon")
        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)
        self.extraLabel = QtWidgets.QLabel(self.extraTopBg)
        self.extraLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.extraLabel.setObjectName("extraLabel")
        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)
        self.extraCloseColumnBtn = QtWidgets.QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QtCore.QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.extraCloseColumnBtn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/images/icons/icon_close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon6)
        self.extraCloseColumnBtn.setIconSize(QtCore.QSize(20, 20))
        self.extraCloseColumnBtn.setObjectName("extraCloseColumnBtn")
        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.extraTopLayout)
        self.extraColumLayout.addWidget(self.extraTopBg)
        self.extraContent = QtWidgets.QFrame(self.extraLeftBox)
        self.extraContent.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.extraContent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extraContent.setObjectName("extraContent")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.extraTopMenu = QtWidgets.QFrame(self.extraContent)
        self.extraTopMenu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extraTopMenu.setObjectName("extraTopMenu")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.btn_share = QtWidgets.QPushButton(self.extraTopMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_share.setStyleSheet("background-image: url(:/icons/images/icons/cil-share-boxed.png);")
        self.btn_share.setObjectName("btn_share")
        self.verticalLayout_11.addWidget(self.btn_share)
        self.btn_adjustments = QtWidgets.QPushButton(self.extraTopMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet("background-image: url(:/icons/images/icons/cil-equalizer.png);")
        self.btn_adjustments.setObjectName("btn_adjustments")
        self.verticalLayout_11.addWidget(self.btn_adjustments)
        self.btn_more = QtWidgets.QPushButton(self.extraTopMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_more.setStyleSheet("background-image: url(:/icons/images/icons/cil-layers.png);")
        self.btn_more.setObjectName("btn_more")
        self.verticalLayout_11.addWidget(self.btn_more)
        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, QtCore.Qt.AlignTop)
        self.extraCenter = QtWidgets.QFrame(self.extraContent)
        self.extraCenter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extraCenter.setObjectName("extraCenter")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.textEdit = QtWidgets.QTextEdit(self.extraCenter)
        self.textEdit.setMinimumSize(QtCore.QSize(222, 0))
        self.textEdit.setStyleSheet("background: transparent;")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_10.addWidget(self.textEdit)
        self.verticalLayout_12.addWidget(self.extraCenter)
        self.extraBottom = QtWidgets.QFrame(self.extraContent)
        self.extraBottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extraBottom.setObjectName("extraBottom")
        self.verticalLayout_12.addWidget(self.extraBottom)
        self.extraColumLayout.addWidget(self.extraContent)
        self.appLayout.addWidget(self.extraLeftBox)
        self.contentBox = QtWidgets.QFrame(self.bgApp)
        self.contentBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.contentBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentBox.setObjectName("contentBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.contentTopBg = QtWidgets.QFrame(self.contentBox)
        self.contentTopBg.setMinimumSize(QtCore.QSize(0, 50))
        self.contentTopBg.setMaximumSize(QtCore.QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentTopBg.setObjectName("contentTopBg")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftBox = QtWidgets.QFrame(self.contentTopBg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy)
        self.leftBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.leftBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftBox.setObjectName("leftBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.titleRightInfo = QtWidgets.QLabel(self.leftBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy)
        self.titleRightInfo.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.titleRightInfo.setObjectName("titleRightInfo")
        self.horizontalLayout_3.addWidget(self.titleRightInfo)
        self.horizontalLayout.addWidget(self.leftBox)
        self.rightButtons = QtWidgets.QFrame(self.contentTopBg)
        self.rightButtons.setMinimumSize(QtCore.QSize(0, 28))
        self.rightButtons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightButtons.setObjectName("rightButtons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.settingsTopBtn = QtWidgets.QPushButton(self.rightButtons)
        self.settingsTopBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QtCore.QSize(28, 28))
        self.settingsTopBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settingsTopBtn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/dracula/icons/cil-cursor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsTopBtn.setIcon(icon7)
        self.settingsTopBtn.setIconSize(QtCore.QSize(20, 20))
        self.settingsTopBtn.setObjectName("settingsTopBtn")
        self.horizontalLayout_2.addWidget(self.settingsTopBtn)
        self.minimizeAppBtn = QtWidgets.QPushButton(self.rightButtons)
        self.minimizeAppBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QtCore.QSize(28, 28))
        self.minimizeAppBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimizeAppBtn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/dracula/icons/icon_minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeAppBtn.setIcon(icon8)
        self.minimizeAppBtn.setIconSize(QtCore.QSize(20, 20))
        self.minimizeAppBtn.setObjectName("minimizeAppBtn")
        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)
        self.maximizeRestoreAppBtn = QtWidgets.QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QtCore.QSize(28, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font)
        self.maximizeRestoreAppBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.maximizeRestoreAppBtn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/dracula/icons/icon_maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon9)
        self.maximizeRestoreAppBtn.setIconSize(QtCore.QSize(20, 20))
        self.maximizeRestoreAppBtn.setObjectName("maximizeRestoreAppBtn")
        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)
        self.closeAppBtn = QtWidgets.QPushButton(self.rightButtons)
        self.closeAppBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QtCore.QSize(28, 28))
        self.closeAppBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeAppBtn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/dracula/icons/icon_close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeAppBtn.setIcon(icon10)
        self.closeAppBtn.setIconSize(QtCore.QSize(20, 20))
        self.closeAppBtn.setObjectName("closeAppBtn")
        self.horizontalLayout_2.addWidget(self.closeAppBtn)
        self.horizontalLayout.addWidget(self.rightButtons, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.contentTopBg)
        self.contentBottom = QtWidgets.QFrame(self.contentBox)
        self.contentBottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentBottom.setObjectName("contentBottom")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.content = QtWidgets.QFrame(self.contentBottom)
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pagesContainer = QtWidgets.QFrame(self.content)
        self.pagesContainer.setStyleSheet("")
        self.pagesContainer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pagesContainer.setObjectName("pagesContainer")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.stackedWidget = QtWidgets.QStackedWidget(self.pagesContainer)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setStyleSheet("background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.home.setObjectName("home")
        self.label_2 = QtWidgets.QLabel(self.home)
        self.label_2.setGeometry(QtCore.QRect(290, 40, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.widNewProj = QtWidgets.QWidget(self.home)
        self.widNewProj.setGeometry(QtCore.QRect(160, 120, 441, 121))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widNewProj.sizePolicy().hasHeightForWidth())
        self.widNewProj.setSizePolicy(sizePolicy)
        self.widNewProj.setStyleSheet("#widNewProj .QWidget：hover{\n"
"background-color: rgb(189, 147, 249);\n"
"}\n"
"")
        self.widNewProj.setObjectName("widNewProj")
        self.gridLayout = QtWidgets.QGridLayout(self.widNewProj)
        self.gridLayout.setContentsMargins(9, 9, 9, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.newKongbai = QtWidgets.QWidget(self.widNewProj)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newKongbai.sizePolicy().hasHeightForWidth())
        self.newKongbai.setSizePolicy(sizePolicy)
        self.newKongbai.setObjectName("newKongbai")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.newKongbai)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.pbNewKongbai_2 = QtWidgets.QPushButton(self.newKongbai)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbNewKongbai_2.sizePolicy().hasHeightForWidth())
        self.pbNewKongbai_2.setSizePolicy(sizePolicy)
        self.pbNewKongbai_2.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/dracula/images/PyDracula.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbNewKongbai_2.setIcon(icon11)
        self.pbNewKongbai_2.setIconSize(QtCore.QSize(32, 32))
        self.pbNewKongbai_2.setObjectName("pbNewKongbai_2")
        self.verticalLayout_51.addWidget(self.pbNewKongbai_2)
        self.label_5 = QtWidgets.QLabel(self.newKongbai)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_51.addWidget(self.label_5)
        self.gridLayout.addWidget(self.newKongbai, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.widNewProj)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.pbNewKongbai_3 = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbNewKongbai_3.sizePolicy().hasHeightForWidth())
        self.pbNewKongbai_3.setSizePolicy(sizePolicy)
        self.pbNewKongbai_3.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/alibaba/alibaba/file1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbNewKongbai_3.setIcon(icon12)
        self.pbNewKongbai_3.setIconSize(QtCore.QSize(32, 32))
        self.pbNewKongbai_3.setObjectName("pbNewKongbai_3")
        self.verticalLayout_22.addWidget(self.pbNewKongbai_3)
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_22.addWidget(self.label_6)
        self.gridLayout.addWidget(self.widget_3, 0, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.widNewProj)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_101 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_101.setObjectName("verticalLayout_101")
        self.pbNewKongbai_4 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbNewKongbai_4.sizePolicy().hasHeightForWidth())
        self.pbNewKongbai_4.setSizePolicy(sizePolicy)
        self.pbNewKongbai_4.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/alibaba/alibaba/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbNewKongbai_4.setIcon(icon13)
        self.pbNewKongbai_4.setIconSize(QtCore.QSize(32, 32))
        self.pbNewKongbai_4.setObjectName("pbNewKongbai_4")
        self.verticalLayout_101.addWidget(self.pbNewKongbai_4)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_101.addWidget(self.label_7)
        self.gridLayout.addWidget(self.widget, 0, 2, 1, 1)
        self.stackedWidget.addWidget(self.home)
        self.widgets = QtWidgets.QWidget()
        self.widgets.setStyleSheet("b")
        self.widgets.setObjectName("widgets")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widgets)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.row_2 = QtWidgets.QFrame(self.widgets)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.row_2.sizePolicy().hasHeightForWidth())
        self.row_2.setSizePolicy(sizePolicy)
        self.row_2.setMinimumSize(QtCore.QSize(0, 60))
        self.row_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.row_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.row_2.setObjectName("row_2")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_3 = QtWidgets.QLabel(self.row_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_19.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.row_2)
        self.row_3 = QtWidgets.QFrame(self.widgets)
        self.row_3.setMinimumSize(QtCore.QSize(0, 150))
        self.row_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.row_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.row_3.setObjectName("row_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout.addWidget(self.row_3)
        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QtWidgets.QWidget()
        self.new_page.setObjectName("new_page")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label = QtWidgets.QLabel(self.new_page)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_20.addWidget(self.label)
        self.stackedWidget.addWidget(self.new_page)
        self.verticalLayout_15.addWidget(self.stackedWidget)
        self.horizontalLayout_4.addWidget(self.pagesContainer)
        self.extraRightBox = QtWidgets.QFrame(self.content)
        self.extraRightBox.setMinimumSize(QtCore.QSize(0, 0))
        self.extraRightBox.setMaximumSize(QtCore.QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extraRightBox.setObjectName("extraRightBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.themeSettingsTopDetail = QtWidgets.QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setMaximumSize(QtCore.QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.themeSettingsTopDetail.setObjectName("themeSettingsTopDetail")
        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)
        self.contentSettings = QtWidgets.QFrame(self.extraRightBox)
        self.contentSettings.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentSettings.setObjectName("contentSettings")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.topMenus = QtWidgets.QFrame(self.contentSettings)
        self.topMenus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.topMenus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topMenus.setObjectName("topMenus")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.btn_message = QtWidgets.QPushButton(self.topMenus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_message.setStyleSheet("background-image: url(:/icons/images/icons/cil-envelope-open.png);")
        self.btn_message.setObjectName("btn_message")
        self.verticalLayout_14.addWidget(self.btn_message)
        self.btn_print = QtWidgets.QPushButton(self.topMenus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_print.setStyleSheet("background-image: url(:/icons/images/icons/cil-print.png);")
        self.btn_print.setObjectName("btn_print")
        self.verticalLayout_14.addWidget(self.btn_print)
        self.btn_logout = QtWidgets.QPushButton(self.topMenus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_logout.setStyleSheet("background-image: url(:/icons/images/icons/cil-account-logout.png);")
        self.btn_logout.setObjectName("btn_logout")
        self.verticalLayout_14.addWidget(self.btn_logout)
        self.verticalLayout_13.addWidget(self.topMenus, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_7.addWidget(self.contentSettings)
        self.horizontalLayout_4.addWidget(self.extraRightBox)
        self.verticalLayout_6.addWidget(self.content)
        self.bottomBar = QtWidgets.QFrame(self.contentBottom)
        self.bottomBar.setMinimumSize(QtCore.QSize(0, 22))
        self.bottomBar.setMaximumSize(QtCore.QSize(16777215, 22))
        self.bottomBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomBar.setObjectName("bottomBar")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.creditsLabel = QtWidgets.QLabel(self.bottomBar)
        self.creditsLabel.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.creditsLabel.setFont(font)
        self.creditsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.creditsLabel.setObjectName("creditsLabel")
        self.horizontalLayout_5.addWidget(self.creditsLabel)
        self.version = QtWidgets.QLabel(self.bottomBar)
        self.version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.version.setObjectName("version")
        self.horizontalLayout_5.addWidget(self.version)
        self.frame_size_grip = QtWidgets.QFrame(self.bottomBar)
        self.frame_size_grip.setMinimumSize(QtCore.QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QtCore.QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_size_grip.setObjectName("frame_size_grip")
        self.horizontalLayout_5.addWidget(self.frame_size_grip)
        self.verticalLayout_6.addWidget(self.bottomBar)
        self.verticalLayout_2.addWidget(self.contentBottom)
        self.appLayout.addWidget(self.contentBox)
        self.appMargins.addWidget(self.bgApp)
        welcomForm.setCentralWidget(self.styleSheet)

        self.retranslateUi(welcomForm)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(welcomForm)

    def retranslateUi(self, welcomForm):
        _translate = QtCore.QCoreApplication.translate
        welcomForm.setWindowTitle(_translate("welcomForm", "wellcom"))
        self.titleLeftApp.setText(_translate("welcomForm", "PyDracula"))
        self.titleLeftDescription.setText(_translate("welcomForm", "Modern GUI / Flat Style"))
        self.toggleButton.setText(_translate("welcomForm", "Hide"))
        self.btn_home.setText(_translate("welcomForm", "Home"))
        self.btn_recent.setText(_translate("welcomForm", "最近项目"))
        self.btn_new.setText(_translate("welcomForm", "New"))
        self.btn_exit.setText(_translate("welcomForm", "退出"))
        self.toggleLeftBox.setText(_translate("welcomForm", "设置"))
        self.extraLabel.setText(_translate("welcomForm", "Left Box"))
        self.extraCloseColumnBtn.setToolTip(_translate("welcomForm", "Close left box"))
        self.btn_share.setText(_translate("welcomForm", "Share"))
        self.btn_adjustments.setText(_translate("welcomForm", "Adjustments"))
        self.btn_more.setText(_translate("welcomForm", "More"))
        self.textEdit.setHtml(_translate("welcomForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>"))
        self.titleRightInfo.setText(_translate("welcomForm", "ynlh-GIS"))
        self.settingsTopBtn.setToolTip(_translate("welcomForm", "Settings"))
        self.minimizeAppBtn.setToolTip(_translate("welcomForm", "Minimize"))
        self.maximizeRestoreAppBtn.setToolTip(_translate("welcomForm", "Maximize"))
        self.closeAppBtn.setToolTip(_translate("welcomForm", "Close"))
        self.label_2.setText(_translate("welcomForm", "新建工程"))
        self.label_5.setText(_translate("welcomForm", "空白项目"))
        self.label_6.setText(_translate("welcomForm", "造林作业"))
        self.label_7.setText(_translate("welcomForm", "采伐作业"))
        self.label_3.setText(_translate("welcomForm", "最近的项目"))
        self.label.setText(_translate("welcomForm", "NEW PAGE TEST"))
        self.btn_message.setText(_translate("welcomForm", "Message"))
        self.btn_print.setText(_translate("welcomForm", "Print"))
        self.btn_logout.setText(_translate("welcomForm", "Logout"))
        self.creditsLabel.setText(_translate("welcomForm", "By: ynlh"))
        self.version.setText(_translate("welcomForm", "v1.0.0"))

from . import lhqgis_rc
