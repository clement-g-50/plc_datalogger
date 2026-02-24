# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceAzOiup.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QCommandLinkButton, QGroupBox,
    QHeaderView, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTableWidget, QTableWidgetItem, QTextBrowser,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1026, 744)
        MainWindow.setMinimumSize(QSize(1026, 744))
        MainWindow.setMaximumSize(QSize(1026, 744))
        icon = QIcon()
        iconThemeName = u"document-save"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        MainWindow.setWindowIcon(icon)
        self.actionOuvrir = QAction(MainWindow)
        self.actionOuvrir.setObjectName(u"actionOuvrir")
        self.actionSauvegarder = QAction(MainWindow)
        self.actionSauvegarder.setObjectName(u"actionSauvegarder")
        self.actionQuitter = QAction(MainWindow)
        self.actionQuitter.setObjectName(u"actionQuitter")
        self.actionAide = QAction(MainWindow)
        self.actionAide.setObjectName(u"actionAide")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 20, 441, 671))
        self.text_type_plc = QTextBrowser(self.groupBox)
        self.text_type_plc.setObjectName(u"text_type_plc")
        self.text_type_plc.setGeometry(QRect(0, 30, 151, 31))
        self.type_plc = QComboBox(self.groupBox)
        self.type_plc.addItem("")
        self.type_plc.addItem("")
        self.type_plc.addItem("")
        self.type_plc.setObjectName(u"type_plc")
        self.type_plc.setGeometry(QRect(160, 30, 271, 31))
        self.TableWidget = QTableWidget(self.groupBox)
        if (self.TableWidget.columnCount() < 2):
            self.TableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.TableWidget.rowCount() < 20):
            self.TableWidget.setRowCount(20)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(10, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(11, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(12, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(13, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(14, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(15, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(16, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(17, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(18, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(19, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.TableWidget.setItem(0, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.TableWidget.setItem(0, 1, __qtablewidgetitem23)
        self.TableWidget.setObjectName(u"TableWidget")
        self.TableWidget.setGeometry(QRect(0, 190, 441, 481))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TableWidget.sizePolicy().hasHeightForWidth())
        self.TableWidget.setSizePolicy(sizePolicy)
        self.TableWidget.horizontalHeader().setMinimumSectionSize(200)
        self.TableWidget.horizontalHeader().setStretchLastSection(True)
        self.text_temps_scan = QTextBrowser(self.groupBox)
        self.text_temps_scan.setObjectName(u"text_temps_scan")
        self.text_temps_scan.setGeometry(QRect(0, 110, 151, 31))
        self.temps_scan = QSpinBox(self.groupBox)
        self.temps_scan.setObjectName(u"temps_scan")
        self.temps_scan.setGeometry(QRect(160, 110, 191, 31))
        self.text_temps_scan_2 = QTextBrowser(self.groupBox)
        self.text_temps_scan_2.setObjectName(u"text_temps_scan_2")
        self.text_temps_scan_2.setGeometry(QRect(360, 110, 71, 31))
        self.text_csv = QTextBrowser(self.groupBox)
        self.text_csv.setObjectName(u"text_csv")
        self.text_csv.setGeometry(QRect(0, 150, 151, 31))
        self.csv_file_text = QLineEdit(self.groupBox)
        self.csv_file_text.setObjectName(u"csv_file_text")
        self.csv_file_text.setGeometry(QRect(160, 150, 231, 31))
        self.csv_file_icon_button = QPushButton(self.groupBox)
        self.csv_file_icon_button.setObjectName(u"csv_file_icon_button")
        self.csv_file_icon_button.setGeometry(QRect(400, 150, 31, 31))
        icon1 = QIcon()
        iconThemeName = u"appointment-new"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.csv_file_icon_button.setIcon(icon1)
        self.adressip = QLineEdit(self.groupBox)
        self.adressip.setObjectName(u"adressip")
        self.adressip.setGeometry(QRect(160, 70, 271, 31))
        self.text_adressip = QTextBrowser(self.groupBox)
        self.text_adressip.setObjectName(u"text_adressip")
        self.text_adressip.setGeometry(QRect(0, 70, 151, 31))
        self.button_new_version = QCommandLinkButton(self.centralwidget)
        self.button_new_version.setObjectName(u"button_new_version")
        self.button_new_version.setGeometry(QRect(630, 0, 321, 31))
        icon2 = QIcon(QIcon.fromTheme(u"dialog-information"))
        self.button_new_version.setIcon(icon2)
        self.logger = QTextBrowser(self.centralwidget)
        self.logger.setObjectName(u"logger")
        self.logger.setGeometry(QRect(480, 40, 511, 591))
        self.button_start_stop = QPushButton(self.centralwidget)
        self.button_start_stop.setObjectName(u"button_start_stop")
        self.button_start_stop.setGeometry(QRect(480, 640, 511, 51))
        self.button_start_stop.setIcon(icon1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 1026, 22))
        self.menubar.setDefaultUp(False)
        self.menuFichier = QMenu(self.menubar)
        self.menuFichier.setObjectName(u"menuFichier")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFichier.menuAction())
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addAction(self.actionSauvegarder)
        self.menuFichier.addAction(self.actionAide)
        self.menuFichier.addAction(self.actionQuitter)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Datalogger PLC", None))
        self.actionOuvrir.setText(QCoreApplication.translate("MainWindow", u"Ouvrir", None))
        self.actionSauvegarder.setText(QCoreApplication.translate("MainWindow", u"Sauvegarder", None))
        self.actionQuitter.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.actionAide.setText(QCoreApplication.translate("MainWindow", u"Aide", None))
        self.groupBox.setTitle("")
        self.text_type_plc.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Type de p\u00e9riph\u00e9rique : </p></body></html>", None))
        self.type_plc.setItemText(0, QCoreApplication.translate("MainWindow", u"Allen-Bradley - SLC", None))
        self.type_plc.setItemText(1, QCoreApplication.translate("MainWindow", u"Rockwell Automation - Logix", None))
        self.type_plc.setItemText(2, QCoreApplication.translate("MainWindow", u"Allen-Bradley - Powerflex", None))

        ___qtablewidgetitem = self.TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"TAG PLC", None));
        ___qtablewidgetitem1 = self.TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOM DE LA COLONNE DANS LE CSV", None));
        ___qtablewidgetitem2 = self.TableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem3 = self.TableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem4 = self.TableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem5 = self.TableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem6 = self.TableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem7 = self.TableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem8 = self.TableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem9 = self.TableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem10 = self.TableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem11 = self.TableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem12 = self.TableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem13 = self.TableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem14 = self.TableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem15 = self.TableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem16 = self.TableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem17 = self.TableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem18 = self.TableWidget.verticalHeaderItem(16)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem19 = self.TableWidget.verticalHeaderItem(17)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qtablewidgetitem20 = self.TableWidget.verticalHeaderItem(18)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qtablewidgetitem21 = self.TableWidget.verticalHeaderItem(19)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"20", None));

        __sortingEnabled = self.TableWidget.isSortingEnabled()
        self.TableWidget.setSortingEnabled(False)
        ___qtablewidgetitem22 = self.TableWidget.item(0, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"TAG_PLC_NUMERO1", None));
        ___qtablewidgetitem23 = self.TableWidget.item(0, 1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"NOM DE LA COLONNE 1", None));
        self.TableWidget.setSortingEnabled(__sortingEnabled)

        self.text_temps_scan.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Temps de scan</p></body></html>", None))
        self.text_temps_scan_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">secondes</p></body></html>", None))
        self.text_csv.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Emplacement du CSV :</p></body></html>", None))
        self.csv_file_icon_button.setText("")
        self.text_adressip.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adresse IP</p></body></html>", None))
        self.button_new_version.setText(QCoreApplication.translate("MainWindow", u"Nouvelle version disponible", None))
        self.button_start_stop.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.menuFichier.setTitle(QCoreApplication.translate("MainWindow", u"Fichier", None))
    # retranslateUi

