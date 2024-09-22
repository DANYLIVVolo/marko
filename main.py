from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QSpinBox,QLabel,QRadioButton,QGroupBox,QBoxLayout,QHBoxLayout,QVBoxLayout,QButtonGroup)


app = QApplication([])
window = QWidget()
btn_main = QPushButton("Меню")
btn_Sleep = QPushButton("Відпочити")
box_minutes = QSpinBox()
box_minutes.setValue(30)
btn_OK = QPushButton("")
lb_question = QLabel("")
RadioGroupBox=QGroupBox("Варіанти відповідей")
RadioGroup = QButtonGroup()
btn_1=QRadioButton("")
btn_2=QRadioButton("")
btn_3=QRadioButton("")
btn_4=QRadioButton("")
Answer=QGroupBox("Результет тесту")
lb_Result=QLabel("") #записує правильно чи не правильно
lb_Correct=QLabel("") #вказує правильну відповідь
layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans2.addWidget(btn_1)
layout_ans2.addWidget(btn_2)
layout_ans1.addWidget(btn_3)
layout_ans1.addWidget(btn_4)
























window = show()
