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
        #self.registerButton.clicked.connect(self.regsiterpage)

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
        self.errorLabel.setText("")                 #clear the Error-Label
        client.send(username)                       #send Username to server for check
        client.send(self.passwordEdit.text())       #send Password to server for check

    #shutdown() is called when Cancel-Button is pressed
    def shutdown(self):
        sys.exit(app.exec_()) #ends Program


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