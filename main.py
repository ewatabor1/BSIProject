import itertools

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QCheckBox, \
    QPlainTextEdit
import sys
import csv
from pwnedapi import Password
import os

class App(QWidget):
    def __init__(self):

        super().__init__()
        self.resize(800, 400)
        self.move(200, 50)
        self.setWindowTitle('Bezpieczeństwo systemów informatycznych - Łamanie hasła')
        self.setWindowIcon(QIcon('padlock.png'))
        self.prefixes_and_suffixes=[]
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

        self.check_passwords_button = QPushButton('Check if passwords were leaked')
        self.check_passwords_button.clicked.connect(self.check_if_passwords_pwned)

        self.add_prefix_suffix_checkbox = QCheckBox('permute using prefixes and suffixes')
        self.add_specials_checkbox = QCheckBox('permute using special characters ($,@,5,7 etc.)')
        self.add_upper_lower = QCheckBox('permute using variations with lower and upper case')
        self.add_permutation_of_answers = QCheckBox('permute (combine) answers')

        self.grid.addWidget(self.add_prefix_suffix_checkbox, 11, 0)
        self.grid.addWidget(self.add_specials_checkbox, 11, 1)
        self.grid.addWidget(self.add_upper_lower, 11, 2)
        self.grid.addWidget(self.add_permutation_of_answers, 11, 3)
        self.grid.addWidget(self.generate_passwords_button, 11, 11)
        self.grid.addWidget(self.check_passwords_button, 11, 10)

        self.terminal_label = QLabel('Output:')
        self.grid.addWidget(self.terminal_label,12,0)

        self.terminal = QPlainTextEdit()
        self.terminal.setReadOnly(True)
        self.grid.addWidget(self.terminal,13,0,-1,-1)

        self.setLayout(self.grid)

        self.show()
        # sys.exit(app.exec_())


    def get_answers(self):
        answers=[]
        for i in self.questions:
            if len(i.text())>0:
                answers.append(i.text())
        return answers

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
        return list(dict.fromkeys(results))


    def get_variations_for_word(self,word):
        results = []
        if self.add_prefix_suffix_checkbox.isChecked():
            results += self.permute_password_using_prefixes_and_suffixes(word)
        if self.add_specials_checkbox.isChecked():
            results += self.permute_password_using_special_symbols(word)
        if self.add_upper_lower.isChecked():
            results += self.get_variaions_for_letters(results)

        if len(results) == 0:
            results.append(word)

        return results


    def get_variaions_for_letters(self,words):
        f = lambda x: (x.lower(), x.upper()) if x.isalpha() else x
        results = []
        for rps in words:
            results += map("".join, itertools.product(*map(f, rps)))
        return results

    def generate_passwords(self):
        self.add_terminal_line("Generate")
        self.generate_passwords_button.setEnabled(False)

        self.load_prefixes_and_suffixes()
        textfile = open("passwords.csv", "w")

        if self.add_permutation_of_answers.isChecked():
            answers = self.combine_permute_passwords(self.get_answers())
        else:
            answers = self.get_answers()
        for i in answers:
            for j in self.get_variations_for_word(i):
                textfile.write(j+'\n')

        textfile.close()
        self.generate_passwords_button.setEnabled(True)
        print("Done")

    def add_terminal_line(self,text):
        self.terminal.appendPlainText(text)

    def combine_permute_passwords(self, answers):
        result = []
        for i in range(1, len(answers) + 1):
            for group in itertools.permutations(answers, i):
                result.append(''.join(group))
        return result

    def check_if_passwords_pwned(self):
        textfile = open("passwords.csv", "r")
        line = textfile.readline()
        while line:
            pass_to_check = Password(str(line).removesuffix('\n'))
            if pass_to_check.is_pwned():
                self.add_terminal_line("password: "+pass_to_check.password + " has been leaked "+ str(pass_to_check.pwned_count)+" times")
            line = textfile.readline()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())