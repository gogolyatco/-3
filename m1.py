from PyQt5.QtWidgets import QApplication
#------------------------
#урок 3
from random import choice, shuffle
from time import sleep
#------------------------
app = QApplication([])
from m2 import *
from m3 import *
#------------------
#урок3
class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2,
                 wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_ask += 1
#
#
q1 = Question('Що сказав Гендельф на містку?', 'Ти не пройдеш!', 'Ти не пожреш!', 'Ти помреш!', 'Ти в школу підеш')
q2 = Question('Хто йшов під крутий фонк?', 'Джим, д. Лівсі, Сквайр Трелоні', 'д. Лівсі', 'Чорний пес, сліпий П"ю, Джим', 'mr. Beast')
q3 = Question('Хто кричав фразу "Що ви забули на моєму болоті"?', 'Шрек', 'путін', 'осел', 'якийсь кіт')
q4 = Question('Хто ухилився від граду куль', 'Нео', 'Оен', 'Не нео', 'отой пацан')
q5 = Question('Скільки mr. Beast хотів скинути тротилу', '250 тисяч тонн', '250 тонн', '6 особин', '250 тисяч міліметрів')
q6 = Question('Яка мелодія була при програшу в fnaf', 'Марш Тореадора', 'Пісня Скотта', 'Симфонія Баха', 'Бетховен "Хорал"')
q7 = Question('Хто сказав фразум "Сім"я це головне"', 'Домінік Торетто', 'мама', 'Домінік Торенто', 'отой пацан')
q8 = Question('Скільки в Китаї за путіном ходило валізок', '3 валізки', '1 валізка', 'вагон валізок', 'поїзд з вагоном валізок')
q9 = Question('що змогли передбачити Сімсони?', '«Дісней» придбала студію «20-те століття Фокс»', 'Президенство Трампа', '', 'Теракт 11 вересня 2001')
q10 = Question('Що означає Тролфейс', 'Нео', 'Оен', 'Не нео', 'отой пацан')
q11 = Question('Хто ухилився від граду куль', 'Нео', 'Оен', 'Не нео', 'отой пацан')
q12 = Question('Хто ухилився від граду куль', 'Нео', 'Оен', 'Не нео', 'отой пацан')
q13 = Question('Хто ухилився від граду куль', 'Нео', 'Оен', 'Не нео', 'отой пацан')
q14 = Question('Хто ухилився від граду куль', 'Нео', 'Оен', 'Не нео', 'отой пацан')
q15 = Question('Хто ухилився від граду куль', 'Нео', 'Оен', 'Не нео', 'отой пацан')

#----------------------------------
radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q12, q13, q14, q15]

def new_qestion():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q.question)
    lb_right_answer.setText(cur_q.answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)
new_qestion()
def check():
    RadioGroup.setExclusive(False)
    for answer  in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.test():
                lb_result.setText('Невже правильно?')
    else:
        lb_result.sesetText('А як інакше, неправильно')
    RadioGroup.setExclusive(True)
def click_ok():
    if btn_next.Text() == 'Відповідай':
        check()
        gb_question.hide()
        gb_answer.show()
        btn_next.setText('Крутіть барабан')
    else:
        new_qestion()
        gb_question.show()
        gb_answer.show()
        btn_next.setText('Відповідай')
btn_next.clicked.connect(click_ok)
def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show()
btn_rest.clicked.connect(rest)
def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
btn_clear.clicked.connect(clear)
def add_queston():
    new_q = Question(le_question.text(), le_right_ans.text(),le_wrong_ans1.text(),
                     le_wrong_ans2.text(), le_wrong_ans3.text())
    questions.append(new_q)
    clear()
btn_add_question.clicked.connect(add_queston)

def menu_generation():
    menu_win.show()
    window.hide()
btn_menu.clicked.connect(menu_generation)

def back_menu():
    menu_win.hide()
    window.show()
btn_back.clicked.connect(back_menu)
window.show()
app.exec_()