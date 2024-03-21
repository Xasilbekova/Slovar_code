from PyQt5.QtWidgets import (
    QApplication, 
    QListWidget, 
    QWidget, 
    QPushButton, 
    QVBoxLayout, 
    QHBoxLayout, 
    QLabel, 
    QLineEdit,
    QMessageBox
)

class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 600)
        self.vBox  = QVBoxLayout()
        self.hBox  = QHBoxLayout()

        self.btn_add_new_word = QPushButton("Add new word")
        self.btn_add_new_word.setStyleSheet("""
                            max-width: 200px;
                            background-color: rgb(17, 225, 17);
                            border-radius: 10px;
                            font-size: 20px;
                            padding: 20px;
                        """)
        self.btn_2 = QPushButton("List of words")
        self.btn_2.setStyleSheet("""
                            max-width: 200px;
                            background-color: rgb(17, 225, 17);
                            border-radius: 10px;
                            font-size: 20px;
                            padding: 20px;
                        """)
        self.btn_3 = QPushButton("Search word")
        self.btn_3.setStyleSheet("""
                            max-width: 200px;
                            background-color: rgb(17, 225, 17);
                            border-radius: 10px;
                            font-size: 20px;
                            padding: 20px;
                        """)
        self.btn_4 = QPushButton("Exit")
        self.btn_4.setStyleSheet("""
                            max-width: 200px;
                            background-color: rgb(17, 225, 17);
                            border-radius: 10px;
                            font-size: 20px;
                            padding: 20px;
                        """)

        self.btn_add_new_word.clicked.connect(self.show_menu2)
        self.btn_2.clicked.connect(self.show_menu3)
        self.btn_3.clicked.connect(self.show_menu4)
        self.btn_4.clicked.connect(self.show_exit)

        self.vBox.addStretch()
        self.vBox.addWidget(self.btn_add_new_word)
        self.vBox.addWidget(self.btn_2)
        self.vBox.addWidget(self.btn_3)
        self.vBox.addWidget(self.btn_4)
        self.vBox.addStretch()

        self.hBox.addStretch()
        self.hBox.addLayout(self.vBox)
        self.hBox.addStretch()


        self.setLayout(self.hBox)
        self.show()

    def show_menu1(self):
        self.close()
        self.menu2 = Menu()
        self.menu2.show()

    def show_menu2(self):
        self.close()
        self.menu2 = Menu2()
        self.menu2.show()

    def show_menu3(self):
        self.close()
        self.menu3 = Menu3()
        self.menu3.show()

    def show_menu4(self):
        self.close()
        self.menu4 = Menu4()
        self.menu4.show()
    
    def show_exit(self):
        self.close()
        

class Menu2(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 600)
        self.setWindowTitle("Add new word")
        self.vBox  = QVBoxLayout()
        self.hBox  = QHBoxLayout()
        self.hBoxForBtn  = QHBoxLayout()
        self.vBoxForBtn  = QHBoxLayout()

        self.words_list = []

        self.line1 = QLineEdit(placeholderText="English")
        self.line2 = QLineEdit(placeholderText="Uzbek") 

        self.btn1_1 = QPushButton("Menu")
        self.btn1_2 = QPushButton("List of words")
        self.btn1_3 = QPushButton("Search")

        self.send_btn = QPushButton("Send")
        self.send_btn.clicked.connect(self.save_data)
        self.send_btn.clicked.connect(self.show_menu2)
        self.send_btn.clicked.connect(self.show_results)
        self.send_btn.setStyleSheet("margin-bottom: 500px; padding: 15px")

        self.vBox.addWidget(self.line1)
        self.vBox.addWidget(self.line2)

        self.hBox.addLayout(self.vBox)
        self.hBox.addWidget(self.send_btn)
        self.vBox.addStretch()
        
        self.hBoxForBtn.addWidget(self.btn1_1)
        self.hBoxForBtn.addWidget(self.btn1_2)
        self.hBoxForBtn.addWidget(self.btn1_3)

        self.vBox.addLayout(self.hBoxForBtn)

        self.btn1_1.clicked.connect(self.show_menu1)
        self.btn1_2.clicked.connect(self.show_menu2)
        self.btn1_3.clicked.connect(self.show_menu3)
        
        self.setLayout(self.hBox)
        
        self.show()

    def save_data(self):
        word1 = self.line1.text()
        word2 = self.line2.text()

        with open('words.txt', 'a') as file:
            file.write(f"{word1} - {word2}\n")
        self.line1.clear()
        self.line2.clear()

    def show_results(self):
        print("Ma'lumot faylga va List of words ga yozildi")

    def show_menu1(self):
        self.close()
        self.menu = Menu()
        self.menu.show()

    def show_menu2(self):
        self.close()
        self.menu3 = Menu3()
        self.menu3.show()

    def show_menu3(self):
        self.close()
        self.menu4 = Menu4()
        self.menu4.show()

class Menu3(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 600)
        self.setWindowTitle("List of words")
        self.hBox  = QHBoxLayout()
        self.hBox2  = QHBoxLayout()
        self.vBox  = QVBoxLayout()
        self.vBox2  = QVBoxLayout()
        self.vBox3  = QVBoxLayout()

        self.lebel1 = QLabel("English")
        self.list1 = QListWidget()
        self.lebel2 = QLabel("Uzbek")
        self.list2 = QListWidget()

        self.btn2_1 = QPushButton("Menu")
        self.btn2_2 = QPushButton("Add new word")
        self.btn2_3 = QPushButton("Search")

        self.vBox.addWidget(self.lebel1)
        self.vBox.addWidget(self.list1)
        self.vBox2.addWidget(self.lebel2)
        self.vBox2.addWidget(self.list2)

        self.hBox2.addWidget(self.btn2_1)
        self.hBox2.addWidget(self.btn2_2)
        self.hBox2.addWidget(self.btn2_3)

        self.hBox.addLayout(self.vBox)
        self.hBox.addLayout(self.vBox2)

        self.vBox3.addLayout(self.hBox)
        self.vBox3.addLayout(self.hBox2)

        self.btn2_1.clicked.connect(self.show_menu1)
        self.btn2_2.clicked.connect(self.show_menu2)
        self.btn2_3.clicked.connect(self.show_menu4)

        self.setLayout(self.vBox3)
        self.load_data()
        self.show()

    def load_data(self):
        try:
            with open('words.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    word1, word2 = line.strip().split(' - ')
                    self.list1.addItem(word1)
                    self.list2.addItem(word2)
        except FileNotFoundError:
            QMessageBox.critical(self, "Fayl ochilmadi")

    def show_menu1(self):
        self.close()
        self.menu = Menu()
        self.menu.show()

    def show_menu2(self):
        self.close()
        self.menu2 = Menu2()
        self.menu2.show()

    def show_menu4(self):
        self.close()
        self.menu4 = Menu4()
        self.menu4.show()
class Menu4(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 600)
        self.setWindowTitle("Search")
        self.hBox  = QHBoxLayout()
        self.hBox2  = QHBoxLayout()
        self.vBox  = QVBoxLayout()


        self.line3 = QLineEdit()
        self.btn_3_1 = QPushButton("Search")
        self.list3 = QListWidget()
        
        self.btn2_1 = QPushButton("Menu")
        self.btn2_2 = QPushButton("Add new word")
        self.btn2_3 = QPushButton("List of words")

        self.hBox.addWidget(self.line3)
        self.hBox.addWidget(self.btn_3_1)

        self.hBox2.addWidget(self.btn2_1)
        self.hBox2.addWidget(self.btn2_2)
        self.hBox2.addWidget(self.btn2_3)

        self.vBox.addLayout(self.hBox)
        self.vBox.addWidget(self.list3)
        self.vBox.addLayout(self.hBox2)

        self.btn2_1.clicked.connect(self.show_menu1)
        self.btn2_2.clicked.connect(self.show_menu2)
        self.btn2_3.clicked.connect(self.show_menu3)

        self.setLayout(self.vBox)

        self.show()

    def show_menu1(self):
        self.close()
        self.menu = Menu()
        self.menu.show()

    def show_menu2(self):
        self.close()
        self.menu2 = Menu2()
        self.menu2.show()

    def show_menu3(self):
        self.close()
        self.menu3 = Menu3()
        self.menu3.show()

app = QApplication([])
win = Menu()

app.exec_()
