#!/usr/bin/env python

import sys
import subprocess
import csv
import os

from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtWidgets import (QApplication, QCheckBox, QColorDialog, QDialog,
        QErrorMessage, QFileDialog, QFontDialog, QFrame, QGridLayout,
        QInputDialog, QLabel, QLineEdit, QMessageBox, QPushButton, QPlainTextEdit, QTableWidget,
        QTableWidgetItem, QVBoxLayout,QWidget, QAction)
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import time
import plotly
import plotly.graph_objects as go
import webbrowser
import pandas as pd
import re
from PyQt5.QtWebEngineWidgets import QWebEngineView
import subprocess
from Preprocess import Preprocess
import filetype

pr = Preprocess()
file_uploaded = "file.csv"

class Dialog(QDialog):
    MESSAGE = "<p>Message boxes have a caption, a text, and up to three " \
            "buttons, each with standard or custom texts.</p>" \
            "<p>Click a button to close the message box. Pressing the Esc " \
            "button will activate the detected escape button (if any).</p>"

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.openFilesPath = ''

        self.errorMessageDialog = QErrorMessage(self)

        frameStyle = QFrame.Sunken | QFrame.Panel
 
        self.issueLabel = QLabel()
        self.issueLabel.setFrameStyle(frameStyle)
        self.issueLabel = QLabel("Insert Issue id", self)

        self.issueText = QLineEdit()
        
        self.issueText = QLineEdit(self)

        self.openFileNameLabel = QLabel()
        self.openFileNameLabel.setFrameStyle(frameStyle)
        self.openFileNameButton = QPushButton("Browse File")

        self.newReqLabel = QLabel()
        self.newReqLabel.setFrameStyle(frameStyle)
        self.newReqLabel = QLabel("Insert Requirement", self) 

        self.newReqText = QPlainTextEdit()
        self.newReqText.setFrameStyle(frameStyle)
        self.newReqText = QPlainTextEdit( self)

        self.addTable = QVBoxLayout()

        self.resultViewButton = QPushButton("View Result")

        self.addButton = QPushButton("Add")

        self.vizViewButton = QPushButton("View Visualizer")

        self.web = QWebEngineView()

        self.openFileNameButton.clicked.connect(self.setOpenFileName)

        self.resultViewButton.clicked.connect(self.setLabelResult)

        self.addButton.clicked.connect(self.storeResult)

        self.vizViewButton.clicked.connect(self.open_webbrowser)

        self.headline = QFont("Arial", 14, QFont.Bold)

        self.Issueidlabel = QLabel()
        self.Issueidlabel.setFrameStyle(frameStyle)
        self.Issueidlabel = QLabel("IssueID", self)
        self.Issueidlabel.setFont(self.headline)


        self.similaritylabel = QLabel()
        self.similaritylabel.setFrameStyle(frameStyle)
        self.similaritylabel = QLabel("Similarity", self) 
        self.similaritylabel.setFont(self.headline)

        self.Requirementlabel = QLabel()
        self.Requirementlabel.setFrameStyle(frameStyle)
        self.Requirementlabel = QLabel("Requirement", self)
        self.Requirementlabel.setFont(self.headline)

        self.label1 = QLabel()
        self.label1.setFrameStyle(frameStyle)
        self.label1 = QLabel("", self)

        self.label2 = QLabel()
        self.label2.setFrameStyle(frameStyle)
        self.label2 = QLabel("", self) 

        self.label3 = QLabel()
        self.label3.setFrameStyle(frameStyle)
        self.label3 = QLabel("", self) 
        
        self.label4 = QLabel()
        self.label4.setFrameStyle(frameStyle)
        self.label4 = QLabel("", self)

        self.label5 = QLabel()
        self.label5.setFrameStyle(frameStyle)
        self.label5 = QLabel("", self) 

        self.label6 = QLabel()
        self.label6.setFrameStyle(frameStyle)
        self.label6 = QLabel("", self) 
        
        self.label7 = QLabel()
        self.label7.setFrameStyle(frameStyle)
        self.label7 = QLabel("", self)

        self.label8 = QLabel()
        self.label8.setFrameStyle(frameStyle)
        self.label8 = QLabel("", self) 

        self.label9 = QLabel()
        self.label9.setFrameStyle(frameStyle)
        self.label9 = QLabel("", self) 

        self.label10 = QLabel()
        self.label10.setFrameStyle(frameStyle)
        self.label10 = QLabel("", self)

        self.label11 = QLabel()
        self.label11.setFrameStyle(frameStyle)
        self.label11 = QLabel("", self) 

        self.label12 = QLabel()
        self.label12.setFrameStyle(frameStyle)
        self.label12 = QLabel("", self) 

        self.label13 = QLabel()
        self.label13.setFrameStyle(frameStyle)
        self.label13 = QLabel("", self)

        self.label14 = QLabel()
        self.label14.setFrameStyle(frameStyle)
        self.label14 = QLabel("", self) 

        self.label15 = QLabel()
        self.label15.setFrameStyle(frameStyle)
        self.label15 = QLabel("", self) 
        

        self.native = QCheckBox()
        self.native.setText("Use native file dialog.")
        self.native.setChecked(True)
        if sys.platform not in ("win32", "darwin"):
            self.native.hide()

        layout = QGridLayout()
        layout.setColumnStretch(1, 1)
        layout.setColumnMinimumWidth(1, 250)
       
        layout.addWidget(self.openFileNameButton, 6, 0)
        layout.addWidget(self.openFileNameLabel, 6, 1)

        layout.addWidget(self.issueLabel, 7, 0)
        layout.addWidget(self.issueText, 7, 1)

        layout.addWidget(self.web, 8, 1)
        layout.addWidget(self.newReqLabel, 9, 0)

        layout.addWidget(self.newReqText, 9, 1)

        layout.addWidget(self.resultViewButton, 11, 2)

        layout.addWidget(self.addButton, 11, 0)
    
        layout.addWidget(self.Issueidlabel, 15, 0)
        layout.addWidget(self.similaritylabel, 15, 1)
        layout.addWidget(self.Requirementlabel, 15, 2)

        layout.addWidget(self.label1, 16, 0)
        layout.addWidget(self.label2, 16, 1)
        layout.addWidget(self.label3, 16, 2)

        layout.addWidget(self.label4, 17, 0)
        layout.addWidget(self.label5, 17, 1)
        layout.addWidget(self.label6, 17, 2)

        layout.addWidget(self.label7, 18, 0)
        layout.addWidget(self.label8, 18, 1)
        layout.addWidget(self.label9, 18, 2)

        layout.addWidget(self.label10, 19, 0)
        layout.addWidget(self.label11, 19, 1)
        layout.addWidget(self.label12, 19, 2)

        layout.addWidget(self.label13, 20, 0)
        layout.addWidget(self.label14, 20, 1)
        layout.addWidget(self.label15, 20, 2)

        layout.addWidget(self.vizViewButton, 25, 0)

        width = 1000
          
        # setting  the fixed width of window 
        self.setFixedWidth(width) 
        
        self.setLayout(layout)

        self.setWindowTitle("Change Impact Analysis")
   
    def initUI(self):
                
        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 

        # Show widget
        self.show()
    def setExistingDirectory(self):    
        options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(self,
                "QFileDialog.getExistingDirectory()",
                self.directoryLabel.text(), options=options)
        if directory:
            self.directoryLabel.setText(directory)

    def setOpenFileName(self):    
        options = QFileDialog.Options()
        if not self.native.isChecked():
            options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,
                "QFileDialog.getOpenFileName()", self.openFileNameLabel.text(),
                "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            self.openFileNameLabel.setText(fileName)
    
    def storeResult(self):    
        issueid = self.issueText.text()

        reqtext= self.newReqText.toPlainText()

        temp_filename = "temp.csv"

        pr.append(issueid, reqtext, temp_filename)
        self.issueText.clear()
        self.newReqText.clear()

    def setLabelResult(self):
        add = self.storeResult
        temp_filename = "temp.csv"
        df = pd.read_csv(temp_filename)
        for index, row in df.iterrows(): 
            print (row["Issue_key"], row["Requirement"]) 

            issueid = row["Issue_key"]

            reqtext= row["Requirement"]

            filename = self.openFileNameLabel.text()

            ending = filename.split('.')[-1]

            if ending=="csv":
                df = pd.read_csv(filename)
                df.to_csv(filename, index=False)

                # pr.append(issueid, reqtext, filename)

                file_uploaded = filename

                if not os.path.exists('docx'):
                    os.makedirs('docx')

                if not os.path.exists('txt'):
                    os.makedirs('txt')

                if not os.path.exists('candidates'):
                    os.makedirs('candidates')

                path= "docx/"
                pr.csvToDocx(filename)
                pr.convertDocxToText(path)
                filenames = os.listdir('./txt')
                pr.docToVec(filenames)
                cia_model = "sl_doc2vec.model"
                pr.vecToCsv(cia_model)
                result1 = pr.similarDocs(cia_model, reqtext)
                
                model_test = "clustering_model2.pkl"
                vecs = "vecs.csv"

                txt_folder = "txt/"
                candidates_fld = 'candidates/'

                result2 = pr.cluster(model_test, filename, vecs, txt_folder, candidates_fld, reqtext)

                pr.append(issueid, reqtext, filename)

                tableValues1 = []
                tableValues2 = []

                for i in result2[0]:
                    tableValues1.append(result2[1][i[0]])
                    tableValues2.append(str(i[1]))
                print("successfully finished!")
                filename = file_uploaded

                df = pd.read_csv(str(filename))  

                content = []

                for f in df['Issue_key'].values:
                    for i in tableValues1:
                        if i in df['Issue_key'].values:
                            content.append(df.loc[df['Issue_key'] == i,'Requirement'])
                
                from string import digits
            
                res = ''.join(filter(lambda x: not x.isdigit(), content[0]))

                self.label3.setText(res)

                self.label3.adjustSize()
                self.label3.setWordWrap(True)

                res2 = ''.join(filter(lambda x: not x.isdigit(), content[1]))
                self.label6.setText(res2)
                self.label6.adjustSize()
                self.label6.setWordWrap(True)

                res3 = ''.join(filter(lambda x: not x.isdigit(), content[2]))
                self.label9.setText(res3)
                self.label9.setWordWrap(True)
                res4 = ''.join(filter(lambda x: not x.isdigit(), content[3]))
                self.label12.setText(res4)
                self.label12.setWordWrap(True)
                

                res5 = ''.join(filter(lambda x: not x.isdigit(), content[4]))
                self.label15.setText(res5)
                self.label15.setWordWrap(True)

                self.label1.setText(tableValues1[0])
                self.label2.setText(tableValues2[0])

                self.label4.setText(tableValues1[1])
                self.label5.setText(tableValues2[1])

                self.label7.setText(tableValues1[2])
                self.label8.setText(tableValues2[2])

                self.label10.setText(tableValues1[3])
                self.label11.setText(tableValues2[3])

                self.label13.setText(tableValues1[4])
                self.label14.setText(tableValues2[4])

                fig = go.Figure(data=[go.Table(
                columnorder = [1,2,3],
                columnwidth = [80,80,400],
                header = dict(
                    values = [['<b>IssueId</b><br>'],
                                ['<b>Similarity</b>'],['<b>Requirement</b>']],
                    line_color='darkslategray',
                    fill_color='royalblue',
                    align=['left','center'],
                    font=dict(color='white', size=12),
                    height=40
                )
                    )
                ])
            else:
                print("Problem detected with uploaded file")
        os.remove('temp.csv')        

            
    def createTable(self):
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(55, 70)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)
    
    def open_webbrowser(self):
        webbrowser.open('http://projector.tensorflow.org/?config=https://raw.githubusercontent.com/Bitseat/embeddings_projector/master/req_plot_config.json')

#btn.clicked.connect(open_webbrowser)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text()) 
    


if __name__ == '__main__':
    with open("temp.csv", "w") as my_empty_csv:
        writer = csv.writer(my_empty_csv)
        writer.writerow(["Issue_key", "Requirement"])
        pass
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())
    
