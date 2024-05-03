# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(578, 665)
        MainWindow.setMinimumSize(QSize(578, 665))
        MainWindow.setMaximumSize(QSize(578, 665))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 50, 80);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 30, 221, 27))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 22px;")
        self.link = QLineEdit(self.centralwidget)
        self.link.setObjectName(u"link")
        self.link.setGeometry(QRect(50, 150, 471, 41))
        self.link.setStyleSheet(u"background-color: #424769;\n"
"border-radius: 8px;\n"
"color: #FFF;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 120, 47, 21))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 220, 161, 21))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.option = QComboBox(self.centralwidget)
        self.option.setObjectName(u"option")
        self.option.setGeometry(QRect(50, 250, 471, 41))
        self.option.setCursor(QCursor(Qt.PointingHandCursor))
        self.option.setStyleSheet(u"background-color: #424769;\n"
"border-radius: 8px;\n"
"color: #FFF;")
        self.location = QLineEdit(self.centralwidget)
        self.location.setObjectName(u"location")
        self.location.setGeometry(QRect(50, 350, 361, 41))
        self.location.setStyleSheet(u"background-color: #424769;\n"
"border-radius: 8px;\n"
"color: #FFF;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 320, 91, 21))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnPath = QPushButton(self.centralwidget)
        self.btnPath.setObjectName(u"btnPath")
        self.btnPath.setGeometry(QRect(430, 350, 91, 41))
        self.btnPath.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnPath.setStyleSheet(u"border: 1px solid #F7B176;\n"
"background-color: #F7B176;\n"
"border-radius: 8px;\n"
"box-shadow: 5px 5px 5px #F7B176;")
        self.result = QLabel(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(140, 490, 291, 41))
        self.result.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 22px;")
        self.btnDownload = QPushButton(self.centralwidget)
        self.btnDownload.setObjectName(u"btnDownload")
        self.btnDownload.setGeometry(QRect(240, 420, 91, 41))
        self.btnDownload.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDownload.setStyleSheet(u"border: 1px solid #C1D37F;\n"
"background-color: #C1D37F;\n"
"border-radius: 8px;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 560, 331, 16))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(180, 600, 241, 16))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 578, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"YouTube Downloader - TikTok @victorbeser / @ofabioacarvalho", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"YouTube Downloader", None))
        self.link.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cole aqui o link do YouTube", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Link:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Selecione uma op\u00e7\u00e3o:", None))
        self.location.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta que deseja salvar o arquivo", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Onde salvar:", None))
        self.btnPath.setText(QCoreApplication.translate("MainWindow", u"Escolher", None))
        self.result.setText("")
        self.btnDownload.setText(QCoreApplication.translate("MainWindow", u"Baixar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Desenvolvido por: Victor Beser - Contribui\u00e7\u00e3o: F\u00e1bio Carvalho", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TikTok: @victorbeser  /  @ofabioacarvalho", None))
    # retranslateUi

