import itertools

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QCheckBox
import sys
import csv
from pwnedapi import Password
import os

class App(QWidget):
    def __init__(self):

        super().__init__()
        self.resize(800, 800)
        self.move(200, 50)
        self.setWindowTitle('Bezpieczeństwo systemów informatycznych - Łamanie hasła')
        self.setWindowIcon(QIcon('padlock.png'))
        self.prefixes_and_suffixes=[]
        self.answers = []
        self.questions =[]

        self.questionLabel1 = QLabel('What Is your favorite book?')
        self.questionLabel2 = QLabel('What is the name of the road you grew up on?')
        self.questionLabel3 = QLabel('What is your mother’s maiden name?')
        self.questionLabel4 = QLabel('What was the name of your first/current/favorite pet?')
        self.questionLabel5 = QLabel('What was the first company that you worked for?')
        self.questionLabel6 = QLabel('Where did you meet your spouse?')
        self.questionLabel7 = QLabel('Where did you go to high school/college?')
        self.questionLabel8 = QLabel('What is your favorite food?')
        self.questionLabel9 = QLabel('What city were you born in?')
        self.questionLabel10 = QLabel('Where is your favorite place to vacation?')

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

        self.questions.append(self.questionEdit1)
        self.questions.append(self.questionEdit2)
        self.questions.append(self.questionEdit3)
        self.questions.append(self.questionEdit4)
        self.questions.append(self.questionEdit5)
        self.questions.append(self.questionEdit6)
        self.questions.append(self.questionEdit7)
        self.questions.append(self.questionEdit8)
        self.questions.append(self.questionEdit9)
        self.questions.append(self.questionEdit10)

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

        self.generate_passwords_button = QPushButton('Generate passwords')
        self.generate_passwords_button.clicked.connect(self.generate_passwords)

        self.add_prefix_suffix_checkbox = QCheckBox('permute using prefixes and suffixes')
        self.add_specials_checkbox = QCheckBox('permute using special characters ($,@,5,7 etc.)')

        self.grid.addWidget(self.add_prefix_suffix_checkbox, 11, 0)
        self.grid.addWidget(self.add_specials_checkbox, 11, 1)
        self.grid.addWidget(self.generate_passwords_button, 11, 11)

        self.setLayout(self.grid)

        self.show()
        # sys.exit(app.exec_())


    def get_answers(self):
        for i in self.questions:
            if len(i.text())>0:
                self.answers.append(i.text())
        return self.answers

    def load_prefixes_and_suffixes(self,path='presuf.csv'):
        with open(path) as csvfile:
            reader = csv.reader(csvfile)  # change contents to floats
            for row in reader:  # each row is a list
                self.prefixes_and_suffixes += row

    def permute_password_using_prefixes_and_suffixes(self, question_answer):
        results = []
        for i in self.prefixes_and_suffixes:
            if i+question_answer not in results:
                results.append(i + question_answer)
            for j in self.prefixes_and_suffixes:
                if i+question_answer+j not in results:
                    results.append(i+question_answer+j)
                if question_answer + j not in results:
                    results.append(question_answer + j)
        return results

    def permute_password_using_special_symbols(self,question_answer):
        results=[]
        results.append(question_answer.replace('s','$'))
        results.append(question_answer.replace('S', '$'))
        results.append(question_answer.replace('a', '@'))
        results.append(question_answer.replace('t', '7'))
        results.append(question_answer.replace('T', '7'))
        results.append(question_answer.replace('s', '5'))
        results.append(question_answer.replace('S', '5'))
        return results


    def get_variations_for_word(self,word):
        results= [word]
        if self.add_prefix_suffix_checkbox.isChecked():
            results += self.permute_password_using_prefixes_and_suffixes(word)
        if self.add_specials_checkbox.isChecked():
            results += self.permute_password_using_special_symbols(word)
        return results

    def get_indexes_of_letter(self,word,letter):
        indexes=[]
        for i in range(0,len(word)):
            if word[i]==letter:
                indexes.append(i)
        return indexes

    def get_permutations(self,indexes):
        res =list(itertools.permutations([1, 2, 3]))
        print(res)

    def generate_passwords(self):
        print("Generate")
        self.generate_passwords_button.setEnabled(False)

        self.load_prefixes_and_suffixes()

        textfile = open("passwords.csv", "w")
        for i in self.get_answers():
            for j in self.get_variations_for_word(i):
                textfile.write(j+'\n')
                self.check_if_password_pwned(j)

        textfile.close()
        self.generate_passwords_button.setEnabled(True)

    def check_if_password_pwned(self,password):
        pass_to_check = Password(password)
        if pass_to_check.is_pwned():
            print("password: "+password + " has been leaked "+ str(pass_to_check.pwned_count)+" times")

def rreplace(string, old, new, occurrence):
    li = string.rsplit(old, occurrence)
    return new.join(li)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())