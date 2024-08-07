# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musicplayer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 789)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Edit_input = QtWidgets.QLineEdit(self.groupBox)
        self.Edit_input.setObjectName("Edit_input")
        self.horizontalLayout_5.addWidget(self.Edit_input)
        self.B_search = QtWidgets.QPushButton(self.groupBox)
        self.B_search.setObjectName("B_search")
        self.horizontalLayout_5.addWidget(self.B_search)
        self.horizontalLayout_5.setStretch(0, 10)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Bnetease = QtWidgets.QPushButton(self.groupBox_2)
        self.Bnetease.setCheckable(True)
        self.Bnetease.setObjectName("Bnetease")
        self.horizontalLayout_3.addWidget(self.Bnetease)
        self.Bnpr = QtWidgets.QPushButton(self.groupBox_2)
        self.Bnpr.setCheckable(True)
        self.Bnpr.setObjectName("Bnpr")
        self.horizontalLayout_3.addWidget(self.Bnpr)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.song_table = QtWidgets.QListView(self.groupBox_3)
        self.song_table.setObjectName("song_table")
        self.song_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.gridLayout.addWidget(self.song_table, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_song = QtWidgets.QLabel(self.groupBox_4)
        self.label_song.setObjectName("label_song")
        self.verticalLayout.addWidget(self.label_song)
        self.label_artist = QtWidgets.QLabel(self.groupBox_4)
        self.label_artist.setObjectName("label_artist")
        self.verticalLayout.addWidget(self.label_artist)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Bdown = QtWidgets.QPushButton(self.groupBox_4)
        self.Bdown.setObjectName("Bdown")
        self.horizontalLayout.addWidget(self.Bdown)
        self.Bpause = QtWidgets.QPushButton(self.groupBox_4)
        self.Bpause.setObjectName("Bpause")
        self.horizontalLayout.addWidget(self.Bpause)
        self.Bup = QtWidgets.QPushButton(self.groupBox_4)
        self.Bup.setObjectName("Bup")
        self.horizontalLayout.addWidget(self.Bup)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_info = QtWidgets.QLabel(self.groupBox_4)
        self.label_info.setObjectName("label_info")
        self.verticalLayout_2.addWidget(self.label_info)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 7)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 20)
        self.verticalLayout_3.setStretch(3, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MusicPlayer"))
        self.groupBox.setTitle(_translate("Form", "搜索"))
        self.B_search.setText(_translate("Form", "🔍"))
        self.groupBox_2.setTitle(_translate("Form", "音频来源"))
        self.Bnetease.setText(_translate("Form", "网易云音乐"))
        self.Bnpr.setText(_translate("Form", "npr"))
        self.groupBox_3.setTitle(_translate("Form", "搜索结果"))
        self.label_song.setText(_translate("Form", "TextLabel"))
        self.label_artist.setText(_translate("Form", "TextLabel"))
        self.Bdown.setText(_translate("Form", "←"))
        self.Bpause.setText(_translate("Form", "▶"))
        self.Bup.setText(_translate("Form", "→"))
        self.label_info.setText(_translate("Form", "TextLabel"))