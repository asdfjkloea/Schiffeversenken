#import libraries
import socket
import pickle
import sys
import hashlib
import time
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt

#GUI for login Page
class LoginPage(QWidget):
    def __init__(self):
        super().__init__()      #initialize QWidget class
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
        
        #create button for login
        self.loginButton = QPushButton("Login", self)
        self.loginButton.setStyleSheet(buttonStyle)
        self.loginButton.clicked.connect(self.handleLogin)
        
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
        
        #Password-Confirmation-Textinput next to Label
        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.passwordAgainLabel)
        hbox4.addWidget(self.passwordAgainEdit)
        
        #Error-Label gets its own line
        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.errorLabel)
        
        #Login-Button next to Cancel-Button
        hbox6 = QHBoxLayout()
        hbox6.addWidget(self.cancelButton)
        hbox6.addWidget(self.loginButton)

        #add all the Horizontal "Lines" vertically to vbox
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)

        self.setLayout(vbox)        #set the Layout

        self.setGeometry(100, 100, 400, 150)        #window location and size
        self.setWindowTitle("Login Page")           #window title
        self.setStyleSheet(siteStyle)
        self.show()

    #handleLogin() is called when Login-Button is pressed
    def handleLogin(self):
        global username
        username = self.usernameEdit.text()         #get text from Username-Textinput
        self.errorLabel.setText("")                 #clear the Error-Label
        password = hashlib.sha256(self.passwordEdit.text().encode()) if self.passwordEdit.text() == self.passwordAgainEdit.text() else self.errorLabel.setText("Passwords can't be different!")             #check if Password-Textinput and Password-Confirmation-Textinput are the same, if they are the same hash it with sha256, if they are not the same print Error to Error-Label
        client.send(username)
        client.send(self.passwordEdit.text())

    #shutdown() is called when Cancel-Button is pressed
    def shutdown(self):
        sys.exit()      #ends Program


#parent network class
class Network:
    def __init__(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #create socket
    
    #data send function
    def send(self,data):
        self.connection.send(pickle.dumps(data))
    
    #data receive function
    def receive(self,conn,buffer_size=1024):
        while True:
            data = conn[0].recv(buffer_size)
            if not data:
                break
            return pickle.loads(data)

#client network class
class Client_Net(Network):
    def __init__(self):
        super().__init__()
    
    #recieve function for client without the need for a connection argument
    def receive(self, buffer_size=1024):
        return super().receive([self.connection], buffer_size)
    
    #function to connect to server
    def client_Connect(self,ip,port):
        self.connection.connect((ip,port))

#server network class
class Server_Net(Network):
    def __init__(self):
        super().__init__()
    
    #send function for server, to choose client connection
    def send(self,conn,data):
        conn[0].send(pickle.dumps(data))
    
    #function to listen for incomming connections from clients
    def server_Listen(self,ip,port):
        self.connection.bind((ip,port))
        self.connection.listen()
        client_connection, client_address = self.connection.accept()
        return client_connection, client_address


username = ''

#testing
if __name__ == '__main__':
    import threading
    IP = "localhost"
    PORT = 65500
    
    app = QApplication(sys.argv)
    loginPage = LoginPage()

    def serverTest():
        server = Server_Net()
        client1 = server.server_Listen(IP,PORT)
        print(server.receive(client1))
        print(server.receive(client1))
        server.send(client1, "Hello from Server!")
    t = threading.Thread(target=serverTest)
    t.start()
    
    client = Client_Net()
    client.client_Connect(IP,PORT)
    input("")
    print(client.receive())
    t.join()
    sys.exit(app.exec())
