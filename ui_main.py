# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'APS.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(772, 607)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(212, 255, 234);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ctTitulo = QFrame(self.centralwidget)
        self.ctTitulo.setObjectName(u"ctTitulo")
        self.ctTitulo.setStyleSheet(u"")
        self.ctTitulo.setFrameShape(QFrame.StyledPanel)
        self.ctTitulo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.ctTitulo)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 0, 9, 0)
        self.lblTitulo = QLabel(self.ctTitulo)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 65, 105, 210), stop:0.46 rgba(28, 143, 255, 248), stop:0.75 rgba(78, 230, 255, 234));\n"
"\n"
"color: rgb(0, 86, 20)\n"
"\n"
"\n"
"")
        self.lblTitulo.setMargin(9)
        self.lblTitulo.setIndent(-1)

        self.horizontalLayout_4.addWidget(self.lblTitulo)

        self.lblLogo = QLabel(self.ctTitulo)
        self.lblLogo.setObjectName(u"lblLogo")
        self.lblLogo.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 65, 105, 210), stop:0.46 rgba(28, 143, 255, 248), stop:0.75 rgba(78, 230, 255, 234));")
        self.lblLogo.setLineWidth(0)
        self.lblLogo.setMargin(9)
        self.lblLogo.setIndent(0)

        self.horizontalLayout_4.addWidget(self.lblLogo)


        self.verticalLayout.addWidget(self.ctTitulo)

        self.ctConteudo = QFrame(self.centralwidget)
        self.ctConteudo.setObjectName(u"ctConteudo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ctConteudo.sizePolicy().hasHeightForWidth())
        self.ctConteudo.setSizePolicy(sizePolicy1)
        self.ctConteudo.setFrameShape(QFrame.StyledPanel)
        self.ctConteudo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.ctConteudo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ctEsquerda_2 = QFrame(self.ctConteudo)
        self.ctEsquerda_2.setObjectName(u"ctEsquerda_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ctEsquerda_2.sizePolicy().hasHeightForWidth())
        self.ctEsquerda_2.setSizePolicy(sizePolicy2)
        self.ctEsquerda_2.setMaximumSize(QSize(16777215, 16777215))
        self.ctEsquerda_2.setFrameShape(QFrame.StyledPanel)
        self.ctEsquerda_2.setFrameShadow(QFrame.Raised)
        self.ctEsquerda_2.setLineWidth(0)
        self.tabConteudo = QTabWidget(self.ctEsquerda_2)
        self.tabConteudo.setObjectName(u"tabConteudo")
        self.tabConteudo.setGeometry(QRect(0, 10, 731, 431))
        font1 = QFont()
        font1.setBold(True)
        self.tabConteudo.setFont(font1)
        self.tabConteudo.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.tabConteudo.setStyleSheet(u"QPushButton {\n"
"		\n"
"	background-color: rgb(0, 255, 127);\n"
"	color: rgb(0, 10, 108);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 153, 153);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QTabBar:tab {\n"
"	background-color: rgb(0, 255, 127);\n"
"	color: rgb(0,10,108);\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QTabBar:tab:selected {\n"
"	background-color: rgb(0, 119, 119);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QTabBar:tab:hover {\n"
"	background-color: rgb(0, 153, 153);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"QLabel {\n"
"	color: rgb(0, 10, 108);\n"
"	font: bold;\n"
"}")
        self.tabCalculo = QWidget()
        self.tabCalculo.setObjectName(u"tabCalculo")
        self.lblUpload = QLabel(self.tabCalculo)
        self.lblUpload.setObjectName(u"lblUpload")
        self.lblUpload.setEnabled(True)
        self.lblUpload.setGeometry(QRect(10, 260, 711, 20))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lblUpload.sizePolicy().hasHeightForWidth())
        self.lblUpload.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        self.lblUpload.setFont(font2)
        self.lblUpload.setStyleSheet(u"color: rgb(255, 0, 0)")
        self.ctBotoesCalculo = QFrame(self.tabCalculo)
        self.ctBotoesCalculo.setObjectName(u"ctBotoesCalculo")
        self.ctBotoesCalculo.setGeometry(QRect(0, 280, 701, 61))
        self.ctBotoesCalculo.setFrameShape(QFrame.StyledPanel)
        self.ctBotoesCalculo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.ctBotoesCalculo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnUpload = QPushButton(self.ctBotoesCalculo)
        self.btnUpload.setObjectName(u"btnUpload")
        self.btnUpload.setMinimumSize(QSize(0, 30))
        self.btnUpload.setSizeIncrement(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        self.btnUpload.setFont(font3)
        self.btnUpload.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnUpload)

        self.btnAbrirArquivo = QPushButton(self.ctBotoesCalculo)
        self.btnAbrirArquivo.setObjectName(u"btnAbrirArquivo")
        self.btnAbrirArquivo.setMinimumSize(QSize(0, 30))
        self.btnAbrirArquivo.setFont(font3)
        self.btnAbrirArquivo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnAbrirArquivo)

        self.btnExcluirArquivo = QPushButton(self.ctBotoesCalculo)
        self.btnExcluirArquivo.setObjectName(u"btnExcluirArquivo")
        self.btnExcluirArquivo.setMinimumSize(QSize(0, 30))
        self.btnExcluirArquivo.setFont(font3)
        self.btnExcluirArquivo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnExcluirArquivo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnCalcular = QPushButton(self.tabCalculo)
        self.btnCalcular.setObjectName(u"btnCalcular")
        self.btnCalcular.setGeometry(QRect(10, 340, 161, 31))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.btnCalcular.setFont(font4)
        self.btnCalcular.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lblInstrucoes = QLabel(self.tabCalculo)
        self.lblInstrucoes.setObjectName(u"lblInstrucoes")
        self.lblInstrucoes.setGeometry(QRect(10, 0, 691, 241))
        self.tabConteudo.addTab(self.tabCalculo, "")
        self.tabResultado = QWidget()
        self.tabResultado.setObjectName(u"tabResultado")
        self.lblResultado = QLabel(self.tabResultado)
        self.lblResultado.setObjectName(u"lblResultado")
        self.lblResultado.setGeometry(QRect(10, 10, 691, 16))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setItalic(False)
        self.lblResultado.setFont(font5)
        self.ctResultado = QFrame(self.tabResultado)
        self.ctResultado.setObjectName(u"ctResultado")
        self.ctResultado.setGeometry(QRect(10, 50, 691, 331))
        self.ctResultado.setFrameShape(QFrame.StyledPanel)
        self.ctResultado.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.ctResultado)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ctGraficos = QFrame(self.ctResultado)
        self.ctGraficos.setObjectName(u"ctGraficos")
        self.ctGraficos.setMinimumSize(QSize(0, 0))
        self.ctGraficos.setFrameShape(QFrame.StyledPanel)
        self.ctGraficos.setFrameShadow(QFrame.Raised)
        self.swGraficos = QStackedWidget(self.ctGraficos)
        self.swGraficos.setObjectName(u"swGraficos")
        self.swGraficos.setGeometry(QRect(10, 10, 461, 281))
        self.pgGrafico1 = QWidget()
        self.pgGrafico1.setObjectName(u"pgGrafico1")
        self.gvGrafico1 = QGraphicsView(self.pgGrafico1)
        self.gvGrafico1.setObjectName(u"gvGrafico1")
        self.gvGrafico1.setGeometry(QRect(10, 20, 421, 241))
        self.swGraficos.addWidget(self.pgGrafico1)
        self.pgGrafico2 = QWidget()
        self.pgGrafico2.setObjectName(u"pgGrafico2")
        self.gvGrafico2 = QGraphicsView(self.pgGrafico2)
        self.gvGrafico2.setObjectName(u"gvGrafico2")
        self.gvGrafico2.setGeometry(QRect(10, 20, 421, 241))
        self.swGraficos.addWidget(self.pgGrafico2)
        self.ctBtnGraficos = QFrame(self.ctGraficos)
        self.ctBtnGraficos.setObjectName(u"ctBtnGraficos")
        self.ctBtnGraficos.setGeometry(QRect(510, 0, 141, 291))
        self.ctBtnGraficos.setMaximumSize(QSize(150, 16777215))
        self.ctBtnGraficos.setFrameShape(QFrame.StyledPanel)
        self.ctBtnGraficos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ctBtnGraficos)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnExtrairRelatorio = QPushButton(self.ctBtnGraficos)
        self.btnExtrairRelatorio.setObjectName(u"btnExtrairRelatorio")
        self.btnExtrairRelatorio.setMinimumSize(QSize(0, 35))
        self.btnExtrairRelatorio.setMaximumSize(QSize(16777215, 45))
        self.btnExtrairRelatorio.setFont(font3)
        self.btnExtrairRelatorio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btnExtrairRelatorio)

        self.btnGrafico1 = QPushButton(self.ctBtnGraficos)
        self.btnGrafico1.setObjectName(u"btnGrafico1")
        self.btnGrafico1.setMinimumSize(QSize(0, 35))
        font6 = QFont()
        font6.setBold(True)
        font6.setUnderline(False)
        font6.setKerning(True)
        self.btnGrafico1.setFont(font6)
        self.btnGrafico1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGrafico1.setMouseTracking(False)
        self.btnGrafico1.setTabletTracking(False)
        self.btnGrafico1.setFlat(False)

        self.verticalLayout_2.addWidget(self.btnGrafico1)

        self.btnGrafico2 = QPushButton(self.ctBtnGraficos)
        self.btnGrafico2.setObjectName(u"btnGrafico2")
        self.btnGrafico2.setMinimumSize(QSize(0, 35))
        self.btnGrafico2.setFont(font6)
        self.btnGrafico2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGrafico2.setMouseTracking(False)
        self.btnGrafico2.setTabletTracking(False)
        self.btnGrafico2.setFlat(False)

        self.verticalLayout_2.addWidget(self.btnGrafico2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.ctGraficos)

        self.tabConteudo.addTab(self.tabResultado, "")

        self.horizontalLayout.addWidget(self.ctEsquerda_2)


        self.verticalLayout.addWidget(self.ctConteudo)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabConteudo.setCurrentIndex(1)
        self.swGraficos.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblTitulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:28pt;\">EMERGIX</span></p></body></html>", None))
        self.lblLogo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><img src=\":/Icons/Icons/Logo_Emergix - principal.png\"/></p></body></html>", None))
        self.lblUpload.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.btnUpload.setText(QCoreApplication.translate("MainWindow", u"Carregar arquivo", None))
        self.btnAbrirArquivo.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.btnExcluirArquivo.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btnCalcular.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.lblInstrucoes.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; text-decoration: underline;\">Instru\u00e7\u00f5es:</span></p><p>Para upload do arquivo CSV, siga este padr\u00e3o para apresenta\u00e7\u00e3o dos dados:</p><p>Coluna 1: nome do processo;</p><p>Coluna 2: nome do material utilizado;</p><p>Coluna 3: tipo de fluxo do material (indicar se o material foi utilizado na entrada ou se \u00e9 a sa\u00edda do processo);</p><p>Coluna 4: quantidade do material;</p><p>Coluna 5: unidade de medida do material;</p><p>Coluna 6: valor da transformidade do material;</p><p>Coluna 7: processo de origem do material (indicar qual o processo que originou aquele material).</p></body></html>", None))
        self.tabConteudo.setTabText(self.tabConteudo.indexOf(self.tabCalculo), QCoreApplication.translate("MainWindow", u"C\u00e1lculo", None))
        self.lblResultado.setText(QCoreApplication.translate("MainWindow", u"Quantidade total de emergia consumida:", None))
        self.btnExtrairRelatorio.setText(QCoreApplication.translate("MainWindow", u"Extrair relat\u00f3rio", None))
        self.btnGrafico1.setText(QCoreApplication.translate("MainWindow", u"Emergia por \n"
"processo", None))
        self.btnGrafico2.setText(QCoreApplication.translate("MainWindow", u"Ranking de \n"
"consumo", None))
        self.tabConteudo.setTabText(self.tabConteudo.indexOf(self.tabResultado), QCoreApplication.translate("MainWindow", u"Resultado", None))
    # retranslateUi

