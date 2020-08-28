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
        help = QLabel('다수의 값은 항상 띄어쓰기로 구분해 입력해주세요.', self)
        help2 = QLabel('아래 버튼을 눌러 그래프 값을 입력해주세요.\n한글을 입력하면 깨져 보일 수 있습니다. ', self)

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

        name = QLabel('저장할 이미지의 이름을 아래에 적어주세요:', self)
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
        self.resize(1000, 600)
        self.center()
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '종료', '정말 종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

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
        print(self.rbtn1.isChecked())
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
        graphName, ok = QInputDialog.getText(self, 'Name', '그래프의 이름을 입력해주세요: ')
        a = True
        while a:
            num, ok = QInputDialog.getInt(self, 'Value', '입력할 값 종류의 수(정수): ')
            if num <= 0:
                QMessageBox.question(self, '오류', '입력할 값은 1 이상, 7 이하의 정수여야 합니다.', QMessageBox.Yes)
            else:
                a = False
        a = True
        while a:
            x, ok = QInputDialog.getText(self, 'Value', 'x축 값을 순서대로 띄어쓰기로 구분해 입력해주세요: ')
            xLabel = x.split()
            if len(xLabel) == 0:
                QMessageBox.question(self, '오류', 'x축 값을 하나 이상 입력해주세요.', QMessageBox.Yes)
            else:
                a = False
        print(xLabel)
        valueName = []
        valueList = []
        for i in range(num):
            name, ok = QInputDialog.getText(self, 'Name', '값의 이름을 입력하세요:')
            valueName.append(name)
            a = True
            while a:
                list, ok = QInputDialog.getText(self, 'Value', 'y축 값을 띄어쓰기로 구분해 입력해주세요\n(정수만 입력해주세요, x축 라벨과 수가 일치해야 합니다): ')
                list = list.split()
                if len(xLabel) == len(list):
                    a = False
                else:
                    QMessageBox.question(self, '오류', '값이 총 %s개가 맞는지 확인해주세요' %len(xLabel), QMessageBox.Yes)
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
            ax.plot(xvalue[i], yvalue[i], c = colors[i], label = returnList[3][i])
            plt.plot(xvalue[i], yvalue[i], c = colors[i], label = returnList[3][i])

        ax.legend(loc='upper right')
        ax.grid()
        plt.legend(loc='upper right')
        plt.grid()
        #print('Fine!')
        self.canvas.draw()

    def Dot_input_value(self):
        graphName, ok = QInputDialog.getText(self, 'Name', '그래프의 이름을 입력해주세요: ')

        a = True
        while a:
            x, ok = QInputDialog.getText(self, 'Value', 'x축 값을 순서대로 띄어쓰기로 구분해 입력해주세요\n(7개 이하, 정수만 입력해주세요): ')
            xLabel = x.split()
            if len(xLabel) == 0:
                QMessageBox.question(self, '오류', 'x축 값을 하나 이상 입력해주세요.', QMessageBox.Yes)
            else:
                a = False
        print(xLabel)
        a = True
        while a:
            list, ok = QInputDialog.getText(self, 'Value', 'y축 값을 띄어쓰기로 구분해 입력해주세요\n(정수만 입력해주세요, x축 값과 수가 일치해야 합니다): ')
            list = list.split()
            if len(xLabel) == len(list):
                yLabel = list
                a = False
            else:
                QMessageBox.question(self, '오류', '값이 총 %s개가 맞는지 확인해주세요' %len(xLabel), QMessageBox.Yes)

        a = True
        while a:
            list, ok = QInputDialog.getText(self, 'Value', '값의 이름들을 띄어쓰기로 구분해 입력해주세요\n(x축 값과 수가 일치해야 합니다): ')
            list = list.split()
            if len(xLabel) == len(list):
                nameList = list
                a = False
            else:
                QMessageBox.question(self, '오류', '값이 총 %s개가 맞는지 확인해주세요' %len(xLabel), QMessageBox.Yes)

        a = True
        while a:
            list, ok = QInputDialog.getText(self, 'Value', '값의 크기들을 띄어쓰기로 구분해 입력해주세요\n(정수만 입력해주세요, x축 값과 수가 일치해야 합니다): ')
            list = list.split()
            if len(xLabel) == len(list):
                sizeList = list
                a = False
            else:
                QMessageBox.question(self, '오류', '값이 총 %s개가 맞는지 확인해주세요' %len(xLabel), QMessageBox.Yes)

        returnList = [graphName, xLabel, yLabel, nameList, sizeList]
        print(returnList)

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
        QMessageBox.question(self, '완료', '해당 경로에 저장되었습니다.', QMessageBox.Yes)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
