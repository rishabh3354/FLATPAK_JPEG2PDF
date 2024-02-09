# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'donate_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Donate(object):
    def setupUi(self, Donate):
        Donate.setObjectName("Donate")
        Donate.resize(803, 493)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Donate)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.donate_button = QtWidgets.QPushButton(Donate)
        self.donate_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.donate_button.setStyleSheet("QPushButton {\n"
"    padding: 5px;\n"
"    padding-right: 10px;\n"
"    padding-left: 10px;\n"
"    background-color:rgb(255, 170, 0);\n"
"    border-radius: 5px;\n"
"    color:black;\n"
"\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/myresource/resource/icons8-paypal-144.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.donate_button.setIcon(icon)
        self.donate_button.setIconSize(QtCore.QSize(30, 30))
        self.donate_button.setObjectName("donate_button")
        self.verticalLayout.addWidget(self.donate_button)
        self.developer_info = QtWidgets.QTextBrowser(Donate)
        self.developer_info.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.developer_info.sizePolicy().hasHeightForWidth())
        self.developer_info.setSizePolicy(sizePolicy)
        self.developer_info.setStyleSheet("")
        self.developer_info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.developer_info.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.developer_info.setReadOnly(True)
        self.developer_info.setOpenExternalLinks(True)
        self.developer_info.setObjectName("developer_info")
        self.verticalLayout.addWidget(self.developer_info)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(Donate)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Donate)
        QtCore.QMetaObject.connectSlotsByName(Donate)

    def retranslateUi(self, Donate):
        _translate = QtCore.QCoreApplication.translate
        Donate.setWindowTitle(_translate("Donate", "Dialog"))
        self.donate_button.setText(_translate("Donate", "Donate Now"))
        self.developer_info.setHtml(_translate("Donate", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/myresource/resource/icons8-account-96.png\" height=\"60\" /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#35a849;\">Developed by: </span><span style=\" font-weight:600; color:#35a849;\">Rishabh Bhardwaj</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://snapcraft.io/search?q=rishabh\"><span style=\" font-weight:600; text-decoration: underline; color:#ef2929;\">Get more apps</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#35a849;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#35a849;\">Support Request:</span><span style=\" color:#35a849;\">   If you like this Application, then please support the developer by donation. Your donations make me </span><span style=\" font-weight:600; color:#35a849;\">feel motivated</span><span style=\" color:#35a849;\"> to my work. Thanks!  Expect </span><span style=\" font-weight:600; color:#35a849;\">new updates</span><span style=\" color:#35a849;\"> in near future!</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#35a849;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#35a849;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#35a849;\">Donor\'s Name</span><span style=\" color:#35a849;\"> and Contributions will be displayed in @ </span><a href=\"https://warlordsoftwares.com/apps/supporter-names/\"><span style=\" font-weight:600; text-decoration: underline; color:#ef2929;\">Warlord Software</span></a><span style=\" color:#35a849;\"> as a Thanksgiving notes!</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#35a849;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#35a849;\"><br /></p></body></html>"))
        self.textBrowser.setHtml(_translate("Donate", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/myresource/resource/jpg2pdf.png\" height=\"60\" /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#35a849;\">JPEG2PDF FOR LINUX</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#35a849;\">Version stable</span></p></body></html>"))
import resource_rc
