from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton
import sys

class App(QWidget):
    def __init__(self):

        super().__init__()
        self.resize(800, 800)
        self.move(200, 50)
        self.setWindowTitle('Bezpieczeństwo systemów informatycznych - Łamanie hasła')
        self.setWindowIcon(QIcon('padlock.png'))

        self.questionLabel1 = QLabel('Jak nazywał się Twój pierwszy nauczyciel?')
        self.questionLabel2 = QLabel('Jakie jest drugie imię twojego ojca?')
        self.questionLabel3 = QLabel('W jakim mieście się urodziłeś?')
        self.questionLabel4 = QLabel('Jakie jest twoje ulubione danie?')
        self.questionLabel5 = QLabel('Jak nazywa się twój zwierzak?')
        self.questionLabel6 = QLabel('Question')
        self.questionLabel7 = QLabel('Question')
        self.questionLabel8 = QLabel('Question')
        self.questionLabel9 = QLabel('Question')
        self.questionLabel10 = QLabel('Question')

        self.questionEdit1 = QLineEdit()
        self.questionEdit2 = QLineEdit()
        self.questionEdit3 = QLineEdit()
        self.questionEdit4 = QLineEdit()
        self.questionEdit5 = QLineEdit()
        self.questionEdit6 = QLineEdit()
        self.questionEdit7 = QLineEdit()
        self.questionEdit8 = QLineEdit()
        self.questionEdit9 = QLineEdit()
        self.questionEdit10 = QLineEdit()

        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.questionLabel1, 1, 0)
        self.grid.addWidget(self.questionEdit1, 1, 1)

        self.grid.addWidget(self.questionLabel2, 2, 0)
        self.grid.addWidget(self.questionEdit2, 2, 1)

        self.grid.addWidget(self.questionLabel3, 3, 0)
        self.grid.addWidget(self.questionEdit3, 3, 1)

        self.grid.addWidget(self.questionLabel4, 4, 0)
        self.grid.addWidget(self.questionEdit4, 4, 1)

        self.grid.addWidget(self.questionLabel5, 5, 0)
        self.grid.addWidget(self.questionEdit5, 5, 1)

        self.grid.addWidget(self.questionLabel6, 6, 0)
        self.grid.addWidget(self.questionEdit6, 6, 1)

        self.grid.addWidget(self.questionLabel7, 7, 0)
        self.grid.addWidget(self.questionEdit7, 7, 1)

        self.grid.addWidget(self.questionLabel8, 8, 0)
        self.grid.addWidget(self.questionEdit8, 8, 1)

        self.grid.addWidget(self.questionLabel9, 9, 0)
        self.grid.addWidget(self.questionEdit9, 9, 1)

        self.grid.addWidget(self.questionLabel10, 10, 0)
        self.grid.addWidget(self.questionEdit10, 10, 1)

        self.generate_passwords_button = QPushButton('Generuj hasła')
        self.generate_passwords_button.clicked.connect(self.generate_passwords)
        self.grid.addWidget(self.generate_passwords_button, 11, 11)

        self.setLayout(self.grid)

        self.show()
        # sys.exit(app.exec_())



    def generate_passwords(self):
        print("Generate")
        self.generate_passwords_button.setEnabled(False)

        print("Odpowiedź na pytanie 1: ", self.questionEdit1.text())
#         Generacja hasła i tak dalej
#         I na koniec

#         self.generate_passwords_button.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())