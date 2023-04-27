from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
import Network
import time

#temp list for testing
user_info =['user','342','30']

# ANCHOR Login_Page

#GUI for login Page
class Login_Page(QWidget):
    def __init__(self):
        super().__init__()      #initialize QWidget class
        self.client = Network.Client_Net()
        self.client.client_Connect("localhost", 44444)
        self.initUI()           #call initUI Function

    def initUI(self):
        self.setFixedSize(400, 157)

        #CSS Styles
        siteStyle = """ background-color: #404040;"""
        labelStyle = """color: #e0e0e0;
                        font-family: Arial;
                        font-size: 20px;"""
        editStyle = """ border-radius: 9px;
                        background-color: #505050;
                        color: #e5e5e5;
                        font-family: Arial;
                        font-size: 20px;"""
        buttonStyle = """   color: #e0e0e0;
                            background-color: #454545;
                            font-family: Arial;
                            font-size: 20px;
                            border: 1px solid #353535;
                            border-radius: 5px;"""
        buttonStyle2 = """  color: #e0e0e0;
                            background-color: #454545;
                            font-family: Arial;
                            font-size: 20px;
                            border: none;
                            border-radius: 5px;"""

        errorStyle = """color: #e00000;
                        font-family: Arial;
                        font-size: 15px;"""

        editSize = (250,20)     #size for text inputs
        
        #create Username-Label and Username-Textinput
        self.usernameLabel = QLabel("Username:", self)
        self.usernameLabel.setStyleSheet(labelStyle)
        self.usernameEdit = QLineEdit(self)
        self.usernameEdit.setFixedSize(editSize[0],editSize[1])                 #set size of Textinput
        self.usernameEdit.setStyleSheet(editStyle)
        self.usernameEdit.setAlignment(Qt.AlignmentFlag.AlignHCenter)           #text is in the center of Textinput-Field
        
        #create Password-Label and Password-Textinput
        self.passwordLabel = QLabel("Password:", self)
        self.passwordLabel.setStyleSheet(labelStyle)
        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setFixedSize(editSize[0],editSize[1])                 #set size of Textinput
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)              #only show dots instead of text
        self.passwordEdit.setStyleSheet(editStyle)
        self.passwordEdit.setAlignment(Qt.AlignmentFlag.AlignHCenter)           #dots are in the center of Textinput-Field
        
        
        #create Label to show Errors
        self.errorLabel = QLabel("",self)
        self.errorLabel.setStyleSheet(errorStyle)
        
        #create button for login
        self.loginButton = QPushButton("Login", self)
        self.loginButton.setStyleSheet(buttonStyle)
        self.loginButton.clicked.connect(self.handleLogin)
        
        #create register button
        self.registerButton = QPushButton("I don't have an Account yet", self)
        self.registerButton.setStyleSheet(buttonStyle2)
        #redirect to Register-Page!!!
        self.registerButton.clicked.connect(self.registerpage)

        #create button to cancel everything
        self.cancelButton = QPushButton("Cancel", self)
        self.cancelButton.setStyleSheet(buttonStyle)
        self.cancelButton.clicked.connect(self.shutdown)
        
        #Username-Textinput next to Username-Label
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.usernameLabel)
        hbox1.addWidget(self.usernameEdit)

        #Password-Textinput next to Password-Label
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.passwordLabel)
        hbox3.addWidget(self.passwordEdit)
        
        #Error-Label gets its own line
        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.errorLabel)
        #register-Button in seperate Line
        hbox6 = QHBoxLayout()
        hbox6.addWidget(self.registerButton)
        #Login-Button next to Cancel-Button
        hbox7 = QHBoxLayout()
        hbox7.addWidget(self.cancelButton)
        hbox7.addWidget(self.loginButton)

        #add all the Horizontal "Lines" vertically to vbox
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)
        vbox.addLayout(hbox7)


        self.setLayout(vbox)        #set the Layout

        self.setGeometry(100, 100, 400, 150)        #window location and size
        self.setWindowTitle("Login Page")           #window title
        self.setStyleSheet(siteStyle)
        self.show()

    #handleLogin() is called when Login-Button is pressed
    def handleLogin(self):
        global username
        username = self.usernameEdit.text()         #get text from Username-Textinput
        password = self.passwordEdit.text()
        self.errorLabel.setText("")                 #clear the Error-Label
        if(username == ""):
            self.errorLabel.setText("Username and password can't be empty!")
        else:
            if(self.client.login(username, password) == True):
                self.w = enemy_Window(self.client, self.usernameEdit.text())
                self.w.show()
    #shutdown() is called when Cancel-Button is pressed
    def shutdown(self):
        self.close()

    def registerpage(self):
        self.w = Register_Page(self.client)
        self.w.show()

# ANCHOR Register_Page

#GUI for Register Page
class Register_Page(QWidget):
    def __init__(self, client):
        super().__init__()      #initialize QWidget class
        self.client = client
        self.initUI()           #call initUI Function

    def initUI(self):
        #CSS Styles
        siteStyle = """ background-color: #404040;"""
        labelStyle = """color: #e0e0e0;
                        font-family: Arial;
                        font-size: 20px;"""
        editStyle = """ border-radius: 9px;
                        background-color: #505050;
                        color: #e5e5e5;
                        font-family: Arial;
                        font-size: 20px;"""
        buttonStyle = """   color: #e0e0e0;
                            background-color: #454545;
                            font-family: Arial;
                            font-size: 20px;
                            border: 1px solid #353535;
                            border-radius: 5px;"""
        errorStyle = """color: #e00000;
                        font-family: Arial;
                        font-size: 15px;"""

        editSize = (250,20)     #size for text inputs
        
        #create Username-Label and Username-Textinput
        self.usernameLabel = QLabel("Username:", self)
        self.usernameLabel.setStyleSheet(labelStyle)
        self.usernameEdit = QLineEdit(self)
        self.usernameEdit.setFixedSize(editSize[0],editSize[1])                 #set size of Textinput
        self.usernameEdit.setStyleSheet(editStyle)
        self.usernameEdit.setAlignment(Qt.AlignmentFlag.AlignHCenter)           #text is in the center of Textinput-Field
        
        #create Password-Label and Password-Textinput
        self.passwordLabel = QLabel("Password:", self)
        self.passwordLabel.setStyleSheet(labelStyle)
        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setFixedSize(editSize[0],editSize[1])                 #set size of Textinput
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)              #only show dots instead of text
        self.passwordEdit.setStyleSheet(editStyle)
        self.passwordEdit.setAlignment(Qt.AlignmentFlag.AlignHCenter)           #dots are in the center of Textinput-Field
        
        #create Password-Confirmation-Label and -Textinput
        self.passwordAgainLabel = QLabel("Password(Wiederholung):", self)
        self.passwordAgainLabel.setStyleSheet(labelStyle)
        self.passwordAgainEdit = QLineEdit(self)
        self.passwordAgainEdit.setFixedSize(editSize[0],editSize[1])            #set size of Textinput
        self.passwordAgainEdit.setEchoMode(QLineEdit.EchoMode.Password)         #only show dots intstead of text
        self.passwordAgainEdit.setStyleSheet(editStyle) 
        self.passwordAgainEdit.setAlignment(Qt.AlignmentFlag.AlignHCenter)      #dots are in the center of Textinput-Field
        
        #create Label to show Errors
        self.errorLabel = QLabel("",self)
        self.errorLabel.setStyleSheet(errorStyle)
        
        #create button for Register
        self.registerButton = QPushButton("Register", self)
        self.registerButton.setStyleSheet(buttonStyle)
        self.registerButton.clicked.connect(self.handleLogin)
        
        #create button to cancel everything
        self.cancelButton = QPushButton("Cancel", self)
        self.cancelButton.setStyleSheet(buttonStyle)
        self.cancelButton.clicked.connect(self.shutdown)
        
        #Username-Textinput next to Username-Label
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.usernameLabel)
        hbox1.addWidget(self.usernameEdit)

        #Password-Textinput next to Password-Label
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.passwordLabel)
        hbox3.addWidget(self.passwordEdit)
        
        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.passwordAgainLabel)
        hbox4.addWidget(self.passwordAgainEdit)
        #Error-Label gets its own line
        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.errorLabel)
        #register-Button in seperate Line
        #Login-Button next to Cancel-Button
        hbox6 = QHBoxLayout()
        hbox6.addWidget(self.cancelButton)
        hbox6.addWidget(self.registerButton)

        #add all the Horizontal "Lines" vertically to vbox
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)


        self.setLayout(vbox)        #set the Layout

        self.setGeometry(100, 100, 400, 150)        #window location and size
        self.setWindowTitle("RegisterPage")           #window title
        self.setStyleSheet(siteStyle)
        self.show()

    #handleLogin() is called when Login-Button is pressed
    def handleLogin(self):
        global username
        username = self.usernameEdit.text()         #get text from Username-Textinput
        self.errorLabel.setText("")                 #clear the Error-Label
        if(self.usernameEdit.text() == "" or self.passwordEdit.text() == "" or self.passwordEdit.text() != self.passwordAgainEdit.text()):
            self.errorLabel.setText("Passwords can't be different or empty!")             #check if Password-Textinput and Password-Confirmation-Textinput are the same, if they are not the same print Error to Error-Label
        else:
            password = self.passwordEdit.text()
            print(username)
            if(self.client.register(username, password) == True):
                self.close()
            else:
                self.errorLabel.setText("Username is already taken!")

    #shutdown() is called when Cancel-Button is pressed
    def shutdown(self):
        self.close()      #ends Program

class enemy_Window(QWidget):
    def __init__(self, client, username):
        super().__init__()

        self.setFixedSize(356, 145)
        
        self.update_table(client)
        self.timer = QTimer()
        self.timer.timeout.connect(lambda :self.update_table(client))
        self.timer.start(10000)  # 10 Sekunden

    def on_button_clicked(self, spieler, button_list, timer_disable):
        print(spieler)
        for i in range(0,len(button_list),1):
            button = button_list[i]
            button.setEnabled(False)
            timer_disable.start(10000)
            timer_disable.timeout.connect(lambda:self.button_enable(button_list, timer_disable))
    
    def button_enable(self, button_list, timer_disable): 
        for i in range(0,len(button_list),1):
            button = button_list[i]
            button.setEnabled(True)
        timer_disable.stop()

    #function to reload page every 10s
    def update_table(self, client):
        timer_disable = QTimer()
        self.client = client
        user_list = self.client.get_Players()
        
        #Tabellen-Widget erstellen
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(len(user_list))
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Spieler", "Anzahl der Spiele", "Win-Loss-Ratio"])
        self.table_widget.horizontalHeaderItem(0).setTextAlignment(4)
        self.table_widget.horizontalHeaderItem(1).setTextAlignment(4)
        self.table_widget.horizontalHeaderItem(2).setTextAlignment(4)

        # Spieler-Statistik in Tabelle einfügen
        row = 0
        button_list = []
        for i in range(0,len(user_list),1):
            name_var = user_list[i][0]
            print(type(user_list[i][1]))
            print(type(user_list[i][2]))
            button = QPushButton(name_var)
            button.setStyleSheet("background-color: #454545; color: #e0e0e0;")
            button.clicked.connect(lambda checked, s=i: self.on_button_clicked(s, button_list, timer_disable))
            button_list.append(button)
            self.table_widget.setCellWidget(row, 0, button)
            self.table_widget.setItem(row, 1, QTableWidgetItem(str(user_list[i][1])))
            self.table_widget.item(row, 1).setTextAlignment(4) # zentriert ausrichten
            self.table_widget.setItem(row, 2, QTableWidgetItem(str(user_list[i][2])))
            self.table_widget.item(row, 2).setTextAlignment(4) # zentriert ausrichten
            row += 1


        # Layout erstellen und Tabelle hinzufügen
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

        # Farben setzen
        self.setStyleSheet("background-color: #454545; color: #e0e0e0;")
        self.table_widget.setStyleSheet("QHeaderView::section { background-color:#333333 }alternate-background-color: #333333; background-color: #454545; color: #e0e0e0;")

        print("reloaded")


app = QApplication(sys.argv)
window = Login_Page()
window.show()
sys.exit(app.exec())