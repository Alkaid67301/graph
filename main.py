from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pygal  as pg
import sys

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        help = QLabel('다수의 값은 항상 띄어쓰기로 구분해 입력해주세요.', self)
        help2 = QLabel('아래 버튼을 눌러 그래프 값을 입력해주세요.', self)
        graph = QPixmap('graph.png')

        lbl_img = QLabel()
        lbl_img.setPixmap(graph)

        input_btn =  QPushButton('INPUT', self)
        input_btn.toggle()
        input_btn.clicked.connect(self.input_value)

        rbtn1 = QRadioButton('Line Graph', self)
        rbtn1.setChecked(True)
        rbtn2 = QRadioButton('Bar Graph', self)
        rbtn3 = QRadioButton('Pie Graph', self)
        rbtn4 = QRadioButton('Dot Graph', self)
        rbtn5 = QRadioButton('Funnel Graph', self)

        #file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(rbtn1)
        vbox.addWidget(rbtn2)
        vbox.addWidget(rbtn3)
        vbox.addWidget(rbtn4)
        vbox.addWidget(rbtn5)
        vbox.addStretch(1)
        vbox.addWidget(help)
        vbox.addWidget(help2)
        vbox.addWidget(input_btn)
        vbox.addStretch(1)

        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(lbl_img, 0, 0)
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
        QMessageBox.question(self, '오류', '값이 총 %s개가 맞는지 확인해주세요' %len(xLabel), QMessageBox.Yes)

    def Line_input_value(self):
        num, ok = QInputDialog.getInt(self, 'Value', '입력할 값 종류의 수(정수): ')
        x, ok = QInputDialog.getText(self, 'Value', 'x축 라벨을 순서대로 띄어쓰기로 구분해 입력해주세요: ')
        xLabel = x.split()
        print(xLabel)
        valueName = []
        valueList = []
        for i in range(num):
            name, ok = QInputDialog.getText(self, 'Name', '값의 이름을 입력하세요:')
            valueName.append(name)
            a = True
            while a:
                list, ok = QInputDialog.getText(self, 'Value', '값을 띄어쓰기로 구분해 입력해주세요\n(x축 라벨과 수가 일치해야 합니다): ')
                list = list.split()
                if len(xLabel) == len(list):
                    a = False
                else:
                    QMessageBox.question(self, '오류', '값이 총 %s개가 맞는지 확인해주세요' %len(xLabel), QMessageBox.Yes)
            valueList.append(list)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
