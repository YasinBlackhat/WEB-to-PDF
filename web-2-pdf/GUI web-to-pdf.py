from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import (QPixmap)
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import sys
import os
# Import Library

class Ui_MainWindow(object):
    file_loc = str('')
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(os.path.abspath(os.path.join(os.path.dirname(__file__),"bg.png"))))
        self.label.setObjectName("label")
        self.url_in = QtWidgets.QLineEdit(self.centralwidget)
        self.url_in.setGeometry(QtCore.QRect(120, 40, 541, 51))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.url_in.setFont(font)
        self.url_in.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.url_in.setStyleSheet("border-style:solid;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(31, 57, 94);\n"
"")
        self.url_in.setInputMask("")
        self.url_in.setText("")
        self.url_in.setFrame(False)
        self.url_in.setObjectName("url_in")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(680, 48, 105, 40))
        self.submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit.setStyleSheet("QPushButton{\n"
"border-style:solid;\n"
"color: rgb(255, 255, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"\n"
"")
        self.submit.setText("")
        self.submit.setObjectName("submit")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(20, 40, 51, 61))
        self.save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save.setStyleSheet("QPushButton{\n"
"border-style:solid;\n"
"color: rgb(255, 255, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"\n"
"")
        self.save.setText("")
        self.save.setObjectName("save")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.submit.clicked.connect(self.res) # Submit function clicked to request
        self.save.clicked.connect(self.save_file) # save function clicked to change location file for save


    def res(self): # function download
        import requests
        import json # lib
        
        k = Ui_MainWindow.file_loc
        if k == '':
            self.save_file()

        in_url = self.url_in.text()
        loc = str(Ui_MainWindow.file_loc)
        url = 'https://restpack.io/api/html2pdf/v6/convert'
        
        headers = {
        'Content-Type': 'application/json',
        'x-access-token': 'hHc5xxoTEc5x4EBAjunfG8gQk6g6MEMF7PmB78qjJHYpieLB' # Enter Token ------------------------------********************------------------
        }
        
        payload = {
        'url': in_url, # URL For cinvert to Pdf
        'json': 'true'
        }

        response = requests.post(url, headers = headers, params = {}, data = json.dumps(payload)) # requests
        response.raise_for_status()
        k = response.json() # get json file
        file_loc = k['file']
        r = requests.get(file_loc)

        
        with open(loc, 'wb') as f:
            f.write(r.content)


    def save_file(self): # save function
        savefile = QFileDialog.getSaveFileName()
        Ui_MainWindow.file_loc = savefile[0]

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WEB to PDF"))
        self.url_in.setToolTip(_translate("MainWindow", "URL for Convert to pdf"))
        self.url_in.setPlaceholderText(_translate("MainWindow", "URL : Https://www.google.com"))
        self.submit.setToolTip(_translate("MainWindow", "Submit"))
        self.save.setToolTip(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
    # Thank you
