# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacevSqRoK.ui'
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
        self.actionGithub = QAction(MainWindow)
        self.actionGithub.setObjectName(u"actionGithub")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 20, 501, 671))
        self.text_type_plc = QTextBrowser(self.groupBox)
        self.text_type_plc.setObjectName(u"text_type_plc")
        self.text_type_plc.setGeometry(QRect(0, 10, 151, 31))
        self.type_plc = QComboBox(self.groupBox)
        self.type_plc.setObjectName(u"type_plc")
        self.type_plc.setGeometry(QRect(160, 10, 331, 31))
        self.plccsvtable = QTableWidget(self.groupBox)
        if (self.plccsvtable.columnCount() < 2):
            self.plccsvtable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.plccsvtable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.plccsvtable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.plccsvtable.setObjectName(u"plccsvtable")
        self.plccsvtable.setGeometry(QRect(0, 210, 441, 461))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plccsvtable.sizePolicy().hasHeightForWidth())
        self.plccsvtable.setSizePolicy(sizePolicy)
        self.plccsvtable.horizontalHeader().setMinimumSectionSize(200)
        self.plccsvtable.horizontalHeader().setStretchLastSection(True)
        self.text_temps_scan = QTextBrowser(self.groupBox)
        self.text_temps_scan.setObjectName(u"text_temps_scan")
        self.text_temps_scan.setGeometry(QRect(0, 130, 151, 31))
        self.temps_scan = QSpinBox(self.groupBox)
        self.temps_scan.setObjectName(u"temps_scan")
        self.temps_scan.setGeometry(QRect(160, 130, 221, 31))
        self.text_temps_scan_2 = QTextBrowser(self.groupBox)
        self.text_temps_scan_2.setObjectName(u"text_temps_scan_2")
        self.text_temps_scan_2.setGeometry(QRect(390, 130, 101, 31))
        self.text_csv = QTextBrowser(self.groupBox)
        self.text_csv.setObjectName(u"text_csv")
        self.text_csv.setGeometry(QRect(0, 170, 151, 31))
        self.csv_file_text = QLineEdit(self.groupBox)
        self.csv_file_text.setObjectName(u"csv_file_text")
        self.csv_file_text.setGeometry(QRect(160, 170, 291, 31))
        self.csv_file_icon_button = QPushButton(self.groupBox)
        self.csv_file_icon_button.setObjectName(u"csv_file_icon_button")
        self.csv_file_icon_button.setGeometry(QRect(460, 170, 31, 31))
        icon1 = QIcon()
        iconThemeName = u"appointment-new"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.csv_file_icon_button.setIcon(icon1)
        self.adressip = QLineEdit(self.groupBox)
        self.adressip.setObjectName(u"adressip")
        self.adressip.setGeometry(QRect(160, 50, 331, 31))
        self.text_adressip = QTextBrowser(self.groupBox)
        self.text_adressip.setObjectName(u"text_adressip")
        self.text_adressip.setGeometry(QRect(0, 50, 151, 31))
        self.add_line_bp = QPushButton(self.groupBox)
        self.add_line_bp.setObjectName(u"add_line_bp")
        self.add_line_bp.setGeometry(QRect(450, 320, 41, 51))
        self.remove_line_bp = QPushButton(self.groupBox)
        self.remove_line_bp.setObjectName(u"remove_line_bp")
        self.remove_line_bp.setGeometry(QRect(450, 440, 41, 51))
        self.texr_slot = QTextBrowser(self.groupBox)
        self.texr_slot.setObjectName(u"texr_slot")
        self.texr_slot.setGeometry(QRect(0, 90, 151, 31))
        self.slot_number = QSpinBox(self.groupBox)
        self.slot_number.setObjectName(u"slot_number")
        self.slot_number.setGeometry(QRect(160, 90, 331, 31))
        self.button_new_version = QCommandLinkButton(self.centralwidget)
        self.button_new_version.setObjectName(u"button_new_version")
        self.button_new_version.setGeometry(QRect(650, 0, 261, 31))
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        brush2 = QBrush(QColor(251, 252, 253, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        brush3 = QBrush(QColor(35, 38, 41, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush4 = QBrush(QColor(125, 126, 126, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        self.button_new_version.setPalette(palette)
        font = QFont()
        font.setPointSize(11)
        self.button_new_version.setFont(font)
        self.button_new_version.setAutoFillBackground(True)
        self.button_new_version.setStyleSheet(u"")
        icon2 = QIcon()
        iconThemeName = u"dialog-information"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.button_new_version.setIcon(icon2)
        self.logger = QTextBrowser(self.centralwidget)
        self.logger.setObjectName(u"logger")
        self.logger.setGeometry(QRect(530, 40, 461, 591))
        self.button_start_stop = QPushButton(self.centralwidget)
        self.button_start_stop.setObjectName(u"button_start_stop")
        self.button_start_stop.setGeometry(QRect(530, 640, 461, 51))
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
        self.menuFichier.addSeparator()
        self.menuFichier.addSeparator()
        self.menuFichier.addSeparator()
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionAide)
        self.menuFichier.addAction(self.actionGithub)
        self.menuFichier.addSeparator()
        self.menuFichier.addSeparator()
        self.menuFichier.addSeparator()
        self.menuFichier.addSeparator()
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
        self.actionGithub.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.groupBox.setTitle("")
        self.text_type_plc.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Type de p\u00e9riph\u00e9rique : </p></body></html>", None))
        ___qtablewidgetitem = self.plccsvtable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"TAG PLC", None));
        ___qtablewidgetitem1 = self.plccsvtable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOM DE LA COLONNE DANS LE CSV", None));
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
        self.add_line_bp.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.remove_line_bp.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.texr_slot.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Slot</p></body></html>", None))
        self.button_new_version.setText(QCoreApplication.translate("MainWindow", u"Nouvelle version disponible", None))
        self.button_start_stop.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.menuFichier.setTitle(QCoreApplication.translate("MainWindow", u"Fichier", None))
    # retranslateUi

