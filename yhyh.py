from PyQt6.QtWidgets import *


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.clicks = 0
        self.initUI()

    def initUI(self):
        self.resize(400, 50)
        self.setWindowTitle('данил')
        button = QPushButton('втащить')
        self.label = QLabel('Количевтво ударов: 0')
        main_l = QVBoxLayout()
        h_l = QHBoxLayout()
        main_l.addStretch()
        main_l.addWidget(button)
        main_l.addWidget(self.label)
        h_l.stretch(2)
        main_l.addLayout(h_l)
        self.setLayout(main_l)
        button.clicked.connect(self.click)

    def click(self):
        self.clicks += 1
        self.count = self.clicks
        self.label.setText(f'количество ударов:{self.count}')


def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()
