from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#import numpy as np
import sys, os

nowPath = str(os.getcwd())
os.chdir(nowPath)
font = 'Arial'

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        help = QLabel('Please tell apart each value by space.', self)
        help2 = QLabel('If you want to input graph values, please click button below.\nIt can be not seen if you input language except English. ', self)

        input_btn =  QPushButton('INPUT', self)
        input_btn.toggle()
        input_btn.clicked.connect(self.input_value)

        self.rbtn1 = QRadioButton('Line Graph', self)
        self.rbtn1.setChecked(True)
        #self.rbtn2 = QRadioButton('Bar Graph', self)
        #self.rbtn3 = QRadioButton('Pie Graph', self)
        self.rbtn4 = QRadioButton('Dot Graph', self)
        #self.rbtn5 = QRadioButton('Funnel Graph', self)

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        name = QLabel('Write the name of Image you want to save below:', self)
        self.nameEdit = QLineEdit(self)
        sumb_btn = QPushButton('EXPORT IMAGE', self)
        sumb_btn.clicked.connect(self.export_image)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.rbtn1)
        #vbox.addWidget(self.rbtn2)
        #vbox.addWidget(self.rbtn3)
        vbox.addWidget(self.rbtn4)
        #vbox.addWidget(self.rbtn5)
        vbox.addStretch(1)
        vbox.addWidget(help)
        vbox.addWidget(help2)
        vbox.addWidget(input_btn)
        vbox.addStretch(2)
        vbox.addWidget(name)
        vbox.addWidget(self.nameEdit)
        vbox.addWidget(sumb_btn)
        vbox.addStretch(1)

        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(self.canvas, 0, 0)
        grid.addLayout(vbox, 0, 1)

        self.setWindowTitle('Graph generator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(1000, 600)
        self.center()
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit', 'Are you sure?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def input_value(self):
        #print(self.rbtn1.isChecked())
        if self.rbtn1.isChecked() == True:
            self.Line_input_value()
        #elif self.rbtn2.isChecked():
            #self.Bar_input_value()
        #elif self.rbtn3.isChecked():
            #self.Pie_input_value()
        elif self.rbtn4.isChecked() == True:
            self.Dot_input_value()
        #elif self.rbtn5.isChecked():
            #self.Line_input_value()

    def Line_input_value(self):
        graphName, ok = QInputDialog.getText(self, 'Name', 'Please enter a name for the graph.h: ')
        a = True
        while a:
            num, ok = QInputDialog.getInt(self, 'Value', 'Number of the kind of values you want to input(integer bigger than 0): ')
            if num <= 0:
                QMessageBox.question(self, 'Error', 'The value must be the integer between 1 and 7.', QMessageBox.Yes)
            else:
                a = False
        a = True
        while a:
            x, ok = QInputDialog.getText(self, 'Value', 'Please input x axis values seperated by space: ')
            xLabel = x.split()
            if len(xLabel) == 0:
                QMessageBox.question(self, 'Error', 'Please enter at least one x-axis value.', QMessageBox.Yes)
            else:
                a = False
        #print(xLabel)
        valueName = []
        valueList = []
        for i in range(num):
            name, ok = QInputDialog.getText(self, 'Name', 'Please input name of values:')
            valueName.append(name)
            a = True
            while a:
                list, ok = QInputDialog.getText(self, 'Value', 'Enter y-axis value separated by spacing.\n(Please enter an integer only, the number must match the x-axis label): ')
                list = list.split()
                if len(xLabel) == len(list):
                    a = False
                else:
                    QMessageBox.question(self, 'Error', 'Please check if the total number of values entered is %s.' %len(xLabel), QMessageBox.Yes)
            valueList.append(list)

        returnList = [graphName, num, xLabel, valueName, valueList]
        #print(returnList)
        self.LineGraphGen(returnList)

    def LineGraphGen(self, returnList):
        self.fig.clear()
        plt.clf()
        ax = self.fig.add_subplot(111)
        ax.set_title = returnList[0]

        plt.title = returnList[0]
        value_num = len(returnList[2])
        xvalue = []
        yvalue = []
        for i in range(returnList[1]):
            xval = []
            yval = []
            for j in range(value_num):
                xval.append((returnList[2][j]))
                yval.append(int(returnList[4][i][j]))
            xvalue.append(xval)
            yvalue.append(yval)
        #print(xvalue, yvalue)
        colors = 'r g b c m y k'.split()
        #print(colors)
        for i in range(returnList[1]):
            #print(xvalue[i], yvalue[i])
            ax.plot(xvalue[i], yvalue[i], c = colors[i], marker = "o", label = returnList[3][i])
            plt.plot(xvalue[i], yvalue[i], c = colors[i], marker = "o", label = returnList[3][i])

        ax.legend(loc='upper right')
        ax.grid()
        plt.legend(loc='upper right')
        plt.grid()
        #print('Fine!')
        self.canvas.draw()

    def Dot_input_value(self):
        graphName, ok = QInputDialog.getText(self, 'Name', 'Please enter a name for the graph.: ')

        a = True
        while a:
            x, ok = QInputDialog.getText(self, 'Value', 'Enter the x-axis values separated by spacing in order.\n (7 or less, please enter an integer only): ')
            xLabel = x.split()
            if len(xLabel) == 0:
                QMessageBox.question(self, 'Error', 'Please enter at least one x-axis value.', QMessageBox.Yes)
            else:
                a = False
        #print(xLabel)
        a = True
        while a:
            list, ok = QInputDialog.getText(self, 'Value', 'Enter y-axis value separated by spacing.\n(Please enter an integer only, the x-axis value and number must match): ')
            list = list.split()
            if len(xLabel) == len(list):
                yLabel = list
                a = False
            else:
                QMessageBox.question(self, 'Error', 'Please check if the total price is %s.' %len(xLabel), QMessageBox.Yes)

        a = True
        while a:
            list, ok = QInputDialog.getText(self, 'Value', 'Enter the names of the values separated by spacing\n(the x-axis value and number must match): ')
            list = list.split()
            if len(xLabel) == len(list):
                nameList = list
                a = False
            else:
                QMessageBox.question(self, 'Error', 'Please check if the total price is %s.' %len(xLabel), QMessageBox.Yes)

        a = True
        while a:
            list, ok = QInputDialog.getText(self, 'Value', 'Enter the size of the value separated by spacing.\n(Please enter an integer only, the x-axis value and number must match): ')
            list = list.split()
            if len(xLabel) == len(list):
                sizeList = list
                a = False
            else:
                QMessageBox.question(self, 'Error', 'Please check if the total price is %s.' %len(xLabel), QMessageBox.Yes)

        returnList = [graphName, xLabel, yLabel, nameList, sizeList]
        #print(returnList)

        self.DotGraphGen(returnList)

    def DotGraphGen(self, returnList):
        self.fig.clear()
        plt.clf()
        #print('Fine')
        ax = self.fig.add_subplot(111)
        ax.set_title = returnList[0]

        plt.title = returnList[0]
        value_num = len(returnList[2])
        xvalue = []
        yvalue = []
        sizevalue = []
        #print('Fine')
        for j in range(value_num):
            xvalue.append(int(returnList[1][j]))
            yvalue.append(int(returnList[2][j]))
            sizevalue.append(int(returnList[4][j]))
        colors = 'r g b c m y k'.split()
        if len(xvalue) != 7:
            colors = colors[0:len(xvalue)]
        #print('Fine')

        #print(xvalue, yvalue, sizevalue, colors)
        ax.scatter(x = xvalue, y = yvalue, s = sizevalue, c = colors, alpha = 0.5)
        plt.scatter(x = xvalue, y = yvalue, s = sizevalue, c = colors, alpha = 0.5)
        #print('Fine')

        #gr.legend(loc='upper right')
        ax.grid()
        plt.grid()
        #print('Fine!')
        self.canvas.draw()

    def export_image(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        plt.savefig(file + '\\' + self.nameEdit.text())
        QMessageBox.question(self, 'Done', 'It has been saved to that path.', QMessageBox.Yes)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
