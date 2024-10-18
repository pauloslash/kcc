# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KCC.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QStatusBar,
    QWidget)
from . import KCC_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(450, 400)
        icon = QIcon()
        icon.addFile(u":/Icon/icons/comic2ebook.png", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralWidget = QWidget(mainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.gridLayout = QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 5)
        self.optionWidget = QWidget(self.centralWidget)
        self.optionWidget.setObjectName(u"optionWidget")
        self.gridLayout_2 = QGridLayout(self.optionWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.qualityBox = QCheckBox(self.optionWidget)
        self.qualityBox.setObjectName(u"qualityBox")
        self.qualityBox.setTristate(True)

        self.gridLayout_2.addWidget(self.qualityBox, 0, 2, 1, 1)

        self.deleteBox = QCheckBox(self.optionWidget)
        self.deleteBox.setObjectName(u"deleteBox")

        self.gridLayout_2.addWidget(self.deleteBox, 4, 1, 1, 1)

        self.maximizeStrips = QCheckBox(self.optionWidget)
        self.maximizeStrips.setObjectName(u"maximizeStrips")

        self.gridLayout_2.addWidget(self.maximizeStrips, 3, 1, 1, 1)

        self.gammaBox = QCheckBox(self.optionWidget)
        self.gammaBox.setObjectName(u"gammaBox")

        self.gridLayout_2.addWidget(self.gammaBox, 1, 2, 1, 1)

        self.borderBox = QCheckBox(self.optionWidget)
        self.borderBox.setObjectName(u"borderBox")
        self.borderBox.setTristate(True)

        self.gridLayout_2.addWidget(self.borderBox, 2, 0, 1, 1)

        self.webtoonBox = QCheckBox(self.optionWidget)
        self.webtoonBox.setObjectName(u"webtoonBox")

        self.gridLayout_2.addWidget(self.webtoonBox, 1, 0, 1, 1)

        self.upscaleBox = QCheckBox(self.optionWidget)
        self.upscaleBox.setObjectName(u"upscaleBox")
        self.upscaleBox.setTristate(True)

        self.gridLayout_2.addWidget(self.upscaleBox, 1, 1, 1, 1)

        self.mangaBox = QCheckBox(self.optionWidget)
        self.mangaBox.setObjectName(u"mangaBox")

        self.gridLayout_2.addWidget(self.mangaBox, 0, 0, 1, 1)

        self.rotateBox = QCheckBox(self.optionWidget)
        self.rotateBox.setObjectName(u"rotateBox")
        self.rotateBox.setTristate(True)

        self.gridLayout_2.addWidget(self.rotateBox, 0, 1, 1, 1)

        self.croppingBox = QCheckBox(self.optionWidget)
        self.croppingBox.setObjectName(u"croppingBox")
        self.croppingBox.setTristate(True)

        self.gridLayout_2.addWidget(self.croppingBox, 3, 2, 1, 1)

        self.outputSplit = QCheckBox(self.optionWidget)
        self.outputSplit.setObjectName(u"outputSplit")

        self.gridLayout_2.addWidget(self.outputSplit, 2, 1, 1, 1)

        self.mozJpegBox = QCheckBox(self.optionWidget)
        self.mozJpegBox.setObjectName(u"mozJpegBox")
        self.mozJpegBox.setTristate(True)

        self.gridLayout_2.addWidget(self.mozJpegBox, 3, 0, 1, 1)

        self.colorBox = QCheckBox(self.optionWidget)
        self.colorBox.setObjectName(u"colorBox")

        self.gridLayout_2.addWidget(self.colorBox, 2, 2, 1, 1)

        self.disableProcessingBox = QCheckBox(self.optionWidget)
        self.disableProcessingBox.setObjectName(u"disableProcessingBox")

        self.gridLayout_2.addWidget(self.disableProcessingBox, 4, 2, 1, 1)

        self.dedupeCoverBox = QCheckBox(self.optionWidget)
        self.dedupeCoverBox.setObjectName(u"dedupeCoverBox")

        self.gridLayout_2.addWidget(self.dedupeCoverBox, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.optionWidget, 5, 0, 1, 2)

        self.gammaWidget = QWidget(self.centralWidget)
        self.gammaWidget.setObjectName(u"gammaWidget")
        self.gammaWidget.setVisible(False)
        self.horizontalLayout_2 = QHBoxLayout(self.gammaWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gammaLabel = QLabel(self.gammaWidget)
        self.gammaLabel.setObjectName(u"gammaLabel")

        self.horizontalLayout_2.addWidget(self.gammaLabel)

        self.gammaSlider = QSlider(self.gammaWidget)
        self.gammaSlider.setObjectName(u"gammaSlider")
        self.gammaSlider.setMaximum(250)
        self.gammaSlider.setSingleStep(5)
        self.gammaSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.gammaSlider)


        self.gridLayout.addWidget(self.gammaWidget, 6, 0, 1, 2)

        self.croppingWidget = QWidget(self.centralWidget)
        self.croppingWidget.setObjectName(u"croppingWidget")
        self.croppingWidget.setVisible(False)
        self.horizontalLayout_3 = QHBoxLayout(self.croppingWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.croppingPowerLabel = QLabel(self.croppingWidget)
        self.croppingPowerLabel.setObjectName(u"croppingPowerLabel")

        self.horizontalLayout_3.addWidget(self.croppingPowerLabel)

        self.croppingPowerSlider = QSlider(self.croppingWidget)
        self.croppingPowerSlider.setObjectName(u"croppingPowerSlider")
        self.croppingPowerSlider.setMaximum(200)
        self.croppingPowerSlider.setSingleStep(1)
        self.croppingPowerSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.croppingPowerSlider)


        self.gridLayout.addWidget(self.croppingWidget, 8, 0, 1, 2)

        self.buttonWidget = QWidget(self.centralWidget)
        self.buttonWidget.setObjectName(u"buttonWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonWidget.sizePolicy().hasHeightForWidth())
        self.buttonWidget.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.buttonWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.directoryButton = QPushButton(self.buttonWidget)
        self.directoryButton.setObjectName(u"directoryButton")
        self.directoryButton.setMinimumSize(QSize(0, 30))
        icon1 = QIcon()
        icon1.addFile(u":/Other/icons/folder_new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.directoryButton.setIcon(icon1)

        self.gridLayout_4.addWidget(self.directoryButton, 0, 0, 1, 1)

        self.fileButton = QPushButton(self.buttonWidget)
        self.fileButton.setObjectName(u"fileButton")
        self.fileButton.setMinimumSize(QSize(0, 30))
        icon2 = QIcon()
        icon2.addFile(u":/Other/icons/document_new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fileButton.setIcon(icon2)

        self.gridLayout_4.addWidget(self.fileButton, 0, 3, 1, 1)

        self.deviceBox = QComboBox(self.buttonWidget)
        self.deviceBox.setObjectName(u"deviceBox")
        self.deviceBox.setMinimumSize(QSize(0, 28))

        self.gridLayout_4.addWidget(self.deviceBox, 1, 0, 1, 1)

        self.formatBox = QComboBox(self.buttonWidget)
        self.formatBox.setObjectName(u"formatBox")
        self.formatBox.setMinimumSize(QSize(0, 28))

        self.gridLayout_4.addWidget(self.formatBox, 1, 3, 1, 1)

        self.convertButton = QPushButton(self.buttonWidget)
        self.convertButton.setObjectName(u"convertButton")
        self.convertButton.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setBold(True)
        self.convertButton.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/Other/icons/convert.png", QSize(), QIcon.Normal, QIcon.Off)
        self.convertButton.setIcon(icon3)

        self.gridLayout_4.addWidget(self.convertButton, 1, 2, 1, 1)

        self.clearButton = QPushButton(self.buttonWidget)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setMinimumSize(QSize(0, 30))
        icon4 = QIcon()
        icon4.addFile(u":/Other/icons/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearButton.setIcon(icon4)

        self.gridLayout_4.addWidget(self.clearButton, 0, 2, 1, 1)

        self.directoryButton.raise_()
        self.clearButton.raise_()
        self.fileButton.raise_()
        self.deviceBox.raise_()
        self.convertButton.raise_()
        self.formatBox.raise_()

        self.gridLayout.addWidget(self.buttonWidget, 3, 0, 1, 2)

        self.toolWidget = QWidget(self.centralWidget)
        self.toolWidget.setObjectName(u"toolWidget")
        self.horizontalLayout = QHBoxLayout(self.toolWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.editorButton = QPushButton(self.toolWidget)
        self.editorButton.setObjectName(u"editorButton")
        self.editorButton.setMinimumSize(QSize(0, 30))
        icon5 = QIcon()
        icon5.addFile(u":/Other/icons/editor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editorButton.setIcon(icon5)

        self.horizontalLayout.addWidget(self.editorButton)

        self.wikiButton = QPushButton(self.toolWidget)
        self.wikiButton.setObjectName(u"wikiButton")
        self.wikiButton.setMinimumSize(QSize(0, 30))
        icon6 = QIcon()
        icon6.addFile(u":/Other/icons/wiki.png", QSize(), QIcon.Normal, QIcon.Off)
        self.wikiButton.setIcon(icon6)

        self.horizontalLayout.addWidget(self.wikiButton)


        self.gridLayout.addWidget(self.toolWidget, 0, 0, 1, 2)

        self.jobList = QListWidget(self.centralWidget)
        self.jobList.setObjectName(u"jobList")
        self.jobList.setStyleSheet(u"QListWidget#jobList {background:#ffffff;background-image:url(:/Other/icons/list_background.png);background-position:center center;background-repeat:no-repeat;color:rgb(0,0,0);}")
        self.jobList.setSelectionMode(QAbstractItemView.NoSelection)
        self.jobList.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.jobList.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.gridLayout.addWidget(self.jobList, 2, 0, 1, 2)

        self.progressBar = QProgressBar(self.centralWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 30))
        self.progressBar.setFont(font)
        self.progressBar.setVisible(False)
        self.progressBar.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 2)

        self.customWidget = QWidget(self.centralWidget)
        self.customWidget.setObjectName(u"customWidget")
        self.customWidget.setVisible(False)
        self.gridLayout_3 = QGridLayout(self.customWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.hLabel = QLabel(self.customWidget)
        self.hLabel.setObjectName(u"hLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.hLabel.sizePolicy().hasHeightForWidth())
        self.hLabel.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.hLabel, 0, 2, 1, 1)

        self.widthBox = QSpinBox(self.customWidget)
        self.widthBox.setObjectName(u"widthBox")
        self.widthBox.setMaximum(2160)

        self.gridLayout_3.addWidget(self.widthBox, 0, 1, 1, 1)

        self.wLabel = QLabel(self.customWidget)
        self.wLabel.setObjectName(u"wLabel")
        sizePolicy1.setHeightForWidth(self.wLabel.sizePolicy().hasHeightForWidth())
        self.wLabel.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.wLabel, 0, 0, 1, 1)

        self.heightBox = QSpinBox(self.customWidget)
        self.heightBox.setObjectName(u"heightBox")
        self.heightBox.setMaximum(3840)

        self.gridLayout_3.addWidget(self.heightBox, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.customWidget, 7, 0, 1, 2)

        mainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(mainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setSizeGripEnabled(False)
        mainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.convertButton, self.clearButton)
        QWidget.setTabOrder(self.clearButton, self.directoryButton)
        QWidget.setTabOrder(self.directoryButton, self.fileButton)
        QWidget.setTabOrder(self.fileButton, self.deviceBox)
        QWidget.setTabOrder(self.deviceBox, self.formatBox)
        QWidget.setTabOrder(self.formatBox, self.mangaBox)
        QWidget.setTabOrder(self.mangaBox, self.rotateBox)
        QWidget.setTabOrder(self.rotateBox, self.qualityBox)
        QWidget.setTabOrder(self.qualityBox, self.webtoonBox)
        QWidget.setTabOrder(self.webtoonBox, self.upscaleBox)
        QWidget.setTabOrder(self.upscaleBox, self.gammaBox)
        QWidget.setTabOrder(self.gammaBox, self.borderBox)
        QWidget.setTabOrder(self.borderBox, self.outputSplit)
        QWidget.setTabOrder(self.outputSplit, self.colorBox)
        QWidget.setTabOrder(self.colorBox, self.croppingBox)
        QWidget.setTabOrder(self.croppingBox, self.mozJpegBox)
        QWidget.setTabOrder(self.mozJpegBox, self.maximizeStrips)
        QWidget.setTabOrder(self.maximizeStrips, self.deleteBox)
        QWidget.setTabOrder(self.deleteBox, self.disableProcessingBox)
        QWidget.setTabOrder(self.disableProcessingBox, self.editorButton)
        QWidget.setTabOrder(self.editorButton, self.wikiButton)
        QWidget.setTabOrder(self.wikiButton, self.jobList)
        QWidget.setTabOrder(self.jobList, self.gammaSlider)
        QWidget.setTabOrder(self.gammaSlider, self.widthBox)
        QWidget.setTabOrder(self.widthBox, self.heightBox)
        QWidget.setTabOrder(self.heightBox, self.croppingPowerSlider)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Kindle Comic Converter", None))
#if QT_CONFIG(tooltip)
        self.qualityBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">Não selecionado - 4 painéis<br/></span>Aumenta cada canto separadamente.</p><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">Indeterminado - 2 painéis<br/></span>Aumenta apenas a parte superior e inferior da página.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Selecionado - 4 painéis de alta qualidade<br/></span>Aumenta cada canto separadamente. Tente aumentar a qualidade da ampliação. Consulte a wiki para mais detalhes.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.qualityBox.setText(QCoreApplication.translate("mainWindow", u"Visualização de Painéis 4/2/HQ", None))
#if QT_CONFIG(tooltip)
        self.deleteBox.setToolTip(QCoreApplication.translate("mainWindow", u"Excluir arquivo(s) ou diretório de entrada. Não é recuperável!", None))
#endif // QT_CONFIG(tooltip)
        self.deleteBox.setText(QCoreApplication.translate("mainWindow", u"Excluir entrada", None))
#if QT_CONFIG(tooltip)
        self.maximizeStrips.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Não selecionado - 1x4<br/></span>Manter formato de tiras de painéis 1x4.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Selecionado - 2x2<br/></span>Transformar tiras 1x4 em 2x2 para maximizar o uso da tela.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeStrips.setText(QCoreApplication.translate("mainWindow", u"Tiras de 1x4 para 2x2", None))
#if QT_CONFIG(tooltip)
        self.gammaBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Desabilitar correção automática de gama.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.gammaBox.setText(QCoreApplication.translate("mainWindow", u"Gama personalizada", None))
#if QT_CONFIG(tooltip)
        self.borderBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Desmarcado - Autodetecção<br/></span>A cor do preenchimento das margens será detectada automaticamente.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Indeterminado - Branco<br/></span>As margens serão preenchidas com a cor branca.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Marcado - Preto<br/></span>As margens serão preenchidas com a cor preta.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.borderBox.setText(QCoreApplication.translate("mainWindow", u"B/P margens", None))
#if QT_CONFIG(tooltip)
        self.webtoonBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Ativar modo de análise especial para Webtoons coreanos.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.webtoonBox.setText(QCoreApplication.translate("mainWindow", u"Modo Webtoon", None))
#if QT_CONFIG(tooltip)
        self.upscaleBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Desmarcado - Nada<br/></span>Imagens menores que a resolução do dispositivo não serão redimensionadas.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Indeterminado - Estiramento<br/></span>Imagens menores que a resolução do dispositivo serão redimensionadas. A proporção será desconsiderada.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Marcado - Redimensionamento<br/></span>Imagens menores que a resolução do dispositivo serão redimensionadas. A proporção será preservada.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.upscaleBox.setText(QCoreApplication.translate("mainWindow", u"Esticar/Redimensionar", None))
#if QT_CONFIG(tooltip)
        self.mangaBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Ativar leitura da direita para a esquerda.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.mangaBox.setText(QCoreApplication.translate("mainWindow", u"Modo Manga", None))
#if QT_CONFIG(tooltip)
        self.rotateBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Desmarcado - Dividir<br/></span>Páginas duplas serão cortadas em duas páginas separadas.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Indeterminado - Rotacionar e dividir<br/></span>Páginas duplas serão exibidas duas vezes. Primeiro rotacionadas e depois divididas.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Marcado - Rotacionar<br/></span>Páginas duplas serão rotacionadas.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rotateBox.setText(QCoreApplication.translate("mainWindow", u"Divisor de página dupla", None))
#if QT_CONFIG(tooltip)
        self.croppingBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Desmarcado - Desabilitado</span></p><p>Desabilitado</p><p><span style=\" font-weight:600; text-decoration: underline;\">Indeterminado - Margens<br/></span>Margens</p><p><span style=\" font-weight:600; text-decoration: underline;\">Marcado - Margens + números de página<br/></span>Margens + números de página</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.croppingBox.setText(QCoreApplication.translate("mainWindow", u"Modo de recorte", None))
#if QT_CONFIG(tooltip)
        self.outputSplit.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">Desmarcado - Modo automático<br/></span>A saída será dividida automaticamente.</p><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">Marcado - Modo volume<br/></span>Cada subdiretório será considerado como um volume separado.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.outputSplit.setText(QCoreApplication.translate("mainWindow", u"Divisão de saída", None))
#if QT_CONFIG(tooltip)
        self.mozJpegBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Desmarcado - JPEG<br/></span>Usar arquivos JPEG</p><p><span style=\" font-weight:600; text-decoration: underline;\">Indeterminado - forçar PNG<br/></span>Criar arquivos PNG em vez de JPEG</p><p><span style=\" font-weight:600; text-decoration: underline;\">Marcado - mozJpeg<br/></span>Arquivo JPEG 10-20% menor, com a mesma qualidade de imagem, mas tempo de processamento multiplicado por 2</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.mozJpegBox.setText(QCoreApplication.translate("mainWindow", u"JPEG/PNG/mozJpeg", None))
#if QT_CONFIG(tooltip)
        self.colorBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Desativar conversão para escala de cinza.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.colorBox.setText(QCoreApplication.translate("mainWindow", u"Modo de cor", None))
#if QT_CONFIG(tooltip)
        self.disableProcessingBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Não processe nenhuma imagem, ignore o perfil e as opções de processamento</pre></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.disableProcessingBox.setText(QCoreApplication.translate("mainWindow", u"Desabilitar processamento", None))
#if QT_CONFIG(tooltip)
        self.dedupeCoverBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>Não duplicar a primeira página como a capa. Útil para alinhamento de páginas duplas.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dedupeCoverBox.setText(QCoreApplication.translate("mainWindow", u"Remover duplicatas da capa", None))
        self.gammaLabel.setText(QCoreApplication.translate("mainWindow", u"Gama: Automático", None))
        self.croppingPowerLabel.setText(QCoreApplication.translate("mainWindow", u"Potência de recorte:", None))
#if QT_CONFIG(tooltip)
        self.directoryButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Adicionar diretório contendo arquivos JPG, PNG ou GIF à fila.<br/><span style=\" font-weight:600;\">Arquivos CBR, CBZ e CB7 dentro não serão processados!</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.directoryButton.setText(QCoreApplication.translate("mainWindow", u"Adicionar diretório", None))
#if QT_CONFIG(tooltip)
        self.fileButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Adicionar arquivo CBR, CBZ, CB7 ou PDF à fila.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fileButton.setText(QCoreApplication.translate("mainWindow", u"Adicionar arquivo", None))
#if QT_CONFIG(tooltip)
        self.deviceBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Dispositivo alvo.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.formatBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Formato de saída.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.convertButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Shift+Clique para selecionar o diretório de saída.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.convertButton.setText(QCoreApplication.translate("mainWindow", u"Converter", None))
        self.clearButton.setText(QCoreApplication.translate("mainWindow", u"Limpar lista", None))
#if QT_CONFIG(tooltip)
        self.editorButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Shift+Clique para editar o diretório.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.editorButton.setText(QCoreApplication.translate("mainWindow", u"Editor", None))
        self.wikiButton.setText(QCoreApplication.translate("mainWindow", u"Wiki", None))
#if QT_CONFIG(tooltip)
        self.hLabel.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Resolução do dispositivo alvo.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.hLabel.setText(QCoreApplication.translate("mainWindow", u"Altura personalizada:", None))
#if QT_CONFIG(tooltip)
        self.widthBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Resolução do dispositivo alvo.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.wLabel.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Resolução do dispositivo alvo.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.wLabel.setText(QCoreApplication.translate("mainWindow", u"Largura personalizada:", None))
#if QT_CONFIG(tooltip)
        self.heightBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Resolução do dispositivo alvo.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

