from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
import Network

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

# ANCHOR enemy_Window

class enemy_Window(QWidget):
    def __init__(self, client, username):
        super().__init__()
        #temp list for testing|later need users from server
        self.username = username
        self.client = client
        window.close()
        user_list = self.client.get_Players()
        self.timer2 = QTimer()
        self.resize(1000, 660)
        self.setWindowTitle("choose your enemy")
        layout = QGridLayout()
        self.setLayout(layout)
        label = QLabel(self)
        label.setText("Playerstats are given like: username | games played | WLR       Challenge a player by clicking on the buttons.")
        layout.addWidget(label,0,0,4,0,Qt.AlignmentFlag.AlignTop)
    
        player_button = []
        for i in range(0,len(user_list),1):
            button_var = user_list[i][0]+' | '+user_list[i][1]+' | '+user_list[i][2]   
            p_button = []
            for j in range(1):     
                button = QPushButton(button_var)
                layout.addWidget(button,i+1,0,4,0,Qt.AlignmentFlag.AlignTop)
                p_button.append(button)
            player_button.append(p_button)
        
        for i in range(0,len(user_list),1):
            for j in range(1):
                self.button = player_button[i][j]
                self.button.clicked.connect(lambda _, x=i, y=j: self.request_player(var_list, user_list, player_button, x, y, self.timer2))
        var_list = [user_list, player_button, layout]
        
        
        self.timer2.timeout.connect(lambda : self.reload_page(var_list, p_button, user_list, player_button, self.timer2))
        self.timer2.start(1000) #for testing after -> 10s
        
        

    #function to send game request to other player
    def request_player(self, var_list, user_list, player_button, x, y, timer2):
        user = var_list[0][x][y]
        print(user) #test
        self.client.request_player(user)
        for i in range(0,len(var_list[0]),1):
            for j in range(1):
                disbutton = var_list[1][i][j]
                disbutton.setEnabled(False)
        self.timer2.stop()
        self.timer1 = QTimer()
        self.timer1.timeout.connect(lambda : self.enable_buttons(var_list, user_list, player_button))
        self.timer1.start(1000) #for testing after -> 10s
    
    #function to enable buttons 10s after button was clicked
    def enable_buttons(self, var_list, user_list, player_button):
        for i in range(0,len(var_list[0]),1):
            for j in range(1):
                enbutton = var_list[1][i][j]
                enbutton.setEnabled(True)
        self.timer1.stop()
        self.timer2.start(1000) #for testing after -> 10s
    
    #function to reload page every 10s
    def reload_page(self, var_list, p_button, user_list, player_button, timer2):
        for i in range(0,len(var_list[0]),1):
            for j in range(1):
                var_list[1][i][j].deleteLater()
        #temp list for testing|later need users from server
        var_list[0] = self.client.get_Players()
        var_list[1] = []
        for i in range(0,len(var_list[0]),1):
            button_var = var_list[0][i][0]+' | '+var_list[0][i][1]+' | '+var_list[0][i][2]   
            p_button = []
            for j in range(1):     
                button = QPushButton(button_var)
                var_list[2].addWidget(button,i+1,0,4,0,Qt.AlignmentFlag.AlignTop)
                p_button.append(button)
            var_list[1].append(p_button)
        for i in range(0,len(var_list[0]),1):
            for j in range(1):
                self.button = var_list[1][i][j]
                self.button.clicked.connect(lambda _, x=i, y=j: self.request_player(var_list, user_list, player_button, x, y, self.timer2))
        


app = QApplication(sys.argv)
window = Login_Page()
window.show()
sys.exit(app.exec())






















"""
import Network
import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QLineEdit, QApplication, QMainWindow, QGridLayout, QLabel, QWidget, QPushButton, QMessageBox


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        #Layout erstellen
        layout = QGridLayout(self)
        #Fenstergröße definieren
        self.setFixedSize(QSize(300, 200))

        self.network = Network.Client_Net()
        self.network.client_Connect("127.0.0.1", 44444)

        #Die Felder erstellen
        name_text = QLabel("Name: ", self)
        self.name = QLineEdit(self)
        pwd_text_1 = QLabel("Passwort: ", self)
        pwd_text_2 = QLabel("Passwort (Wiederholung): ", self)
        self.pwd1 = QLineEdit(self)
        self.pwd2 = QLineEdit(self)
        button_ok = QPushButton("Ok", self)
        button_abbrechen = QPushButton("Abbrechen", self)

        #Die passwörter verdecken
        self.pwd1.setEchoMode(QLineEdit.EchoMode.Password)
        self.pwd2.setEchoMode(QLineEdit.EchoMode.Password)

        #den Buttons Funktionen zuweisen
        button_ok.clicked.connect(self.check)
        button_abbrechen.clicked.connect(self.exit)

        #die Felder dem Layout zuweisen
        layout.addWidget(name_text, 0, 0)
        layout.addWidget(self.name, 0, 1)
        layout.addWidget(pwd_text_1, 2, 0)
        layout.addWidget(pwd_text_2, 3, 0)
        layout.addWidget(self.pwd1, 2, 1)
        layout.addWidget(self.pwd2, 3, 1)
        layout.addWidget(button_ok, 4, 0)
        layout.addWidget(button_abbrechen, 4, 1)

        #das Layout dem Fenster zuweisen
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    #Funktion zum checken der Eingabe und Öffnen einer Message-Box
    def check(self):
        if(self.name.text() == "" or self.pwd1.text() == "" or self.pwd1.text() != self.pwd2.text()):
            box = QMessageBox(self)
            box.setText("Inkorrekte Eingabe!")
            box.exec()
        else:
            self.network.send(f"{self.name.text()};{self.pwd1.text()}")
            box = QMessageBox(self)
            box.setText("Sie haben sich erfolgreich eingeloggt!")
            box.exec()

    #Funktion zum Schließen des Fensters
    def exit(self):
        self.destroy()



app = QApplication(sys.argv)
window = Widget()
window.show()
app.exec()

"""
Schiffeversenken.py
19 kB