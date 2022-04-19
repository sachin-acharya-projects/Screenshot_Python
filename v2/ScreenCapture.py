from PyQt5 import QtCore, QtGui, QtWidgets
from win10toast_click import ToastNotifier
import pyautogui, os, time, datetime
from pyscreeze import PyScreezeException
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.lastScreenshot = ""
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.mainWindow = MainWindow
        self.toaster = ToastNotifier()
        MainWindow.setStyleSheet("*{\n"
"background: #333;\n"
"color: white;\n"
"}\n"
"QPushButton{\n"
"border: 2px solid #444;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid #555;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(77, 65, 65);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 40))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.takeScreenshot)
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(200, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 40))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.deleteScreenshot)
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def takeScreenshot(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        SCREENSHOT_LOCATION = os.path.join(BASE_DIR, os.environ.get('USERPROFILE'), 'Pictures\\Screenshotsv2')
        if not os.path.exists(SCREENSHOT_LOCATION):
            os.mkdir(SCREENSHOT_LOCATION)
        self.mainWindow.showMinimized()
        time.sleep(0.3)
        outputName = str(datetime.datetime.now()).replace(' ', '').replace(':', '').replace('-', '').split('.')[0]
        outputName = os.path.join(SCREENSHOT_LOCATION, outputName+'.png')
        self.lastScreenshot = outputName
        myScreenshot = pyautogui.screenshot()
        try:
            myScreenshot.save(outputName)
        except PyScreezeException:
            os.system("pip install --upgrade pip&&pip install --upgrade Pillow")
            self.toaster.show_toast(
                title="Error Occured",
                duration=5,
                msg="Sorry, Some requirements were not satisfied\nNow Packages has been installed successfully\nPlease RESTART the application",
                icon_path=os.path.join(BASE_DIR, 'icon.ico'),
            )
            exit(1)
        self.label.setPixmap(QtGui.QPixmap(outputName))
        self.mainWindow.showMaximized()
        self.toaster.show_toast(
            title="Screenshot",
            msg="Screenshot has been saved\n\n{}".format(SCREENSHOT_LOCATION),
            icon_path=os.path.join(BASE_DIR, 'icon.ico'),
            duration=5,
            callback_on_click=lambda: self.displayImage(outputName)
        )
    def deleteScreenshot(self):
        _translate = QtCore.QCoreApplication.translate
        os.remove(self.lastScreenshot)
        self.label.setText(_translate("MainWindow", "Last Screenshot has been deleted\nYour newly captured screenshot will\nbe shown here"))
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.toaster.show_toast(
            title="Screenshot",
            msg="Screenshot {} has been deleted".format(self.lastScreenshot),
            duration=5,
            icon_path=os.path.join(BASE_DIR, 'icon.ico'),
        )
    def displayImage(self, image):
        os.startfile(image)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Screen Capture"))
        self.label.setText(_translate("MainWindow", "Your Captured Image will\n"
"be shown here"))
        self.pushButton.setText(_translate("MainWindow", "Take Screenshot"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete Screenshot"))
import resources_rc

def logout(app):
    app.exec_()
    exit()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(logout(app))