from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel)

app = QApplication([])

window = QWidget()

btn1 = QPushButton('Ответить')
btn2 = QPushButton('Андрей лох')
# 2 кнопки

btn3 = QPushButton('На забив')

rbtn_1 = QLabel('Вариант 1')
# лейбл 1





layout_ans1 = QHBoxLayout()

layout_ans1.addWidget(btn1)
layout_ans1.addWidget(btn2)

line = QVBoxLayout()

line.addLayout(rbtn_1)
line.addLayout(layout_ans1)

layout_ans2 = QHBoxLayout()
layout_ans2.addWidget(btn3)
layout_ans2.addWidget(line)

window.setLayout(line)

window.setWindowTitle('Memo Card')
window.show()
app.exec()