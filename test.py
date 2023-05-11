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
                self.close()
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
                            foSnt-family: Arial;
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
            if(self.client.register(username, password) == True):
                self.close()
            else:
                self.errorLabel.setText("Username is already taken!")

    #shutdown() is called when Cancel-Button is pressed
    def shutdown(self):
        self.close()      #ends Program


#ANCHOR enemy_Window
class enemy_Window(QWidget):
    def __init__(self, client, username):
        super().__init__()

        self.setFixedSize(356, 145)
        self.accept = None
        self.username = username

        self.timer = QTimer()
        self.timer1 = QTimer()
        self.timer2 = QTimer()
        self.timer4 = QTimer()
        self.timer5 = QTimer()

        self.update_table(client)
        self.timer = QTimer()
        self.client = client
        self.timer.timeout.connect(lambda:self.update_table(client))
        self.timer.start(10000)  # 10 Sekunden
        self.check_Invite()

    def close_Window(self):
        self.w.close()
        if self.accept == True:
            self.client.accepted(self.username[0])
        elif self.accept == False:
            self.client.denied(self.username[0])
    
    def check_Invite(self):
        invite = self.client.got_invited()
        if invite != []:
            self.timer_delay = QTimer()
            self.timer_delay.timeout.connect(self.show_shipplacement)
            self.timer_delay.start(15000)
            self.timer5 = QTimer()
            self.timer5.timeout.connect(self.close_Window)
            self.timer5.start(5000)
            self.w = request_Window(invite, self)
            self.w.show()
        self.timer4 = QTimer()
        self.timer4.timeout.connect(self.check_Invite)
        self.timer4.start(4500)

    def show_shipplacement(self):
        if self.accept == True:
            print(self.username)
            self.timer.stop()
            self.timer1.stop()
            self.timer2.stop()
            self.timer5.stop()
            self.timer4.stop()
            self.client.accepted(self.username[0])
            self.w1 = ship_placement(self.client, self.username, True)
            self.w1.show()
            self.destroy()
        elif self.accept == False:
            self.client.denied(self.username[0])
        self.accept = None

    def on_button_clicked(self, spieler, var_list):
        self.client.request_player(spieler)
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.check_Request)
        self.timer2.start(20000)
    
    def check_Request(self):
        username = self.client.check_Request()
        if(username != False):
            self.timer.stop()
            self.timer1.stop()
            self.timer2.stop()
            self.timer5.stop()
            self.timer4.stop()
            self.w1 = ship_placement(self.client, self.username, False)
            self.w1.show()
            self.destroy()

    #function to send game request to other player
    def request_player(self, var_list, user_list, player_button, x, y, timer2):
        user = var_list[0][x][y]
        #print(user) #test
        self.client.request_player(user)
        for i in range(0,len(var_list[0]),1):
            for j in range(1):
                disbutton = var_list[1][i][j]
                disbutton.setEnabled(False)
        self.timer2.stop()
        self.timer1 = QTimer()
        self.timer1.timeout.connect(lambda : self.enable_buttons(var_list, user_list, player_button))
        self.timer1.start(10000) #for testing after -> 10s
    
        self.timer1.stop()
        self.timer2.start(10000) #for testing after -> 10s
    
    #function to reload page every 10s
    
    def update_table(self, client):
        
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
        for i in range(0,len(user_list),1):
            name_var = user_list[i][0]
            print(name_var, self.username)
            button = QPushButton(name_var)
            button.setStyleSheet("background-color: #454545; color: #e0e0e0;")
            button.clicked.connect(lambda checked, s=name_var, t=user_list: self.on_button_clicked(s, t))
            if(name_var == self.username):
                button.setEnabled(False)
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
        self.table_widget.setStyleSheet("alternate-background-color: #333333; background-color: #454545; color: #e0e0e0;")


#ANCHOR request_Window
#window to accept/deny request
class request_Window(QWidget):
    def __init__(self, user_info, window):
        super().__init__()
        self.window = window
        self.user_info = user_info
        self.resize(500, 300)
        self.setWindowTitle("game request")
        label = QLabel(self)
        label.resize(500,15)
        label.setText("Wanna play against {}? Games played: {} WLR: {}".format(user_info[0][0], user_info[0][1], user_info[0][2][0]))
        label.move(10, 10)
        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        abutton = QPushButton("accept")
        abutton.clicked.connect(self.request_accept)
        hlayout.addWidget(abutton)
        dbutton = QPushButton("deny")
        dbutton.clicked.connect(self.request_deny)
        hlayout.addWidget(dbutton)
        self.setLayout(hlayout)
    
    def request_accept(self):
        #client.send("True")
        self.window.accept = True
        self.window.username = self.user_info[0]
        self.close()
    def request_deny(self):
        #client.send("False")
        self.window.accept = False
        self.close()


#ANCHOR ship_placement
class ship_placement(QWidget):
    def __init__(self, client, username, is_Host):
        self.is_Host = is_Host
        self.client = client
        self.all_Ships_placed = False
        self.username = username
        def visual_ship(cur_placing, rot_list, show_ship_label):
            selected_ship = cur_placing[0]
            width = int(cur_placing[2])
            length = int(cur_placing[1])
            if(selected_ship != ' '):
                for i in range(0,5,1):
                    for j in range(0,5,1):
                        show_ship = show_ship_label[i][j]
                        show_ship.setStyleSheet("background-color: white")
                if (rot_list[0] == 'horizontal'):
                    if (width == 1):
                        for i in range(0,length,1):
                            show_ship = show_ship_label[0][i]
                            show_ship.setStyleSheet("background-color: cyan")
                        show_ship =  show_ship_label[0][0]
                        show_ship.setStyleSheet("background-color: red")
                    elif (width == 2):
                        for j in range(0,width,1):
                            for i in range(0,length,1):
                                show_ship = show_ship_label[j][i]
                                show_ship.setStyleSheet("background-color: cyan")
                        show_ship =  show_ship_label[0][0]
                        show_ship.setStyleSheet("background-color: red")
                elif (rot_list[0] == 'vertical'):
                    if (width == 1):
                        for i in range(0,length,1):
                            show_ship = show_ship_label[i][0]
                            show_ship.setStyleSheet("background-color: cyan")
                        show_ship =  show_ship_label[0][0]
                        show_ship.setStyleSheet("background-color: red")
                    elif (width == 2):
                        for j in range(0,width,1):
                            for i in range(0,length,1):
                                show_ship = show_ship_label[i][j]
                                show_ship.setStyleSheet("background-color: cyan")
                        show_ship =  show_ship_label[0][0]
                        show_ship.setStyleSheet("background-color: red")
        
        super().__init__()

        layout = QGridLayout()
        
        self.setLayout(layout)
        
        #just labels for rows/columns
        for i in range(1,11,1):
            label_num = QLabel(self)
            label_num.setFixedSize(50,50)
            label_num.setStyleSheet("background-color: cyan")
            label_num.setText("{}".format(i))
            label_num.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label_num,0,i,Qt.AlignmentFlag.AlignCenter)
        
        letters = ['A','B','C','D','E','F','G','H','I','J']
        for i in range(1,11,1):
            label_let = QLabel(self)
            label_let.setFixedSize(50,50)
            label_let.setStyleSheet("background-color: cyan")
            label_let.setText("{}".format(letters[i-1]))
            label_let.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label_let,i,0,Qt.AlignmentFlag.AlignCenter)
        
        #field with buttons 
        pl_field = []
        field_buttons = []
        for i in range(1,11,1):
            field = []   
            f_button = []
            for j in range(1,11,1):     
                fbuttons = QPushButton(" ")
                fbuttons.setFixedSize(50,50)
                layout.addWidget(fbuttons,i,j,Qt.AlignmentFlag.AlignCenter)
                f_button.append(fbuttons)
                field.append(' ')
            field_buttons.append(f_button)
            pl_field.append(field)
        for i in range(0,10,1):
            for j in range(0,10,1):
                field_button = field_buttons[i][j]
                field_button.clicked.connect(lambda _, x=i, y=j: self.try_place(x, y, field_buttons, pl_field, cur_placing, rot_list, ships_placed, done_lab, show_ship_label))
        
        #button to reset field
        reset_button = QPushButton('reset')
        layout.addWidget(reset_button,0,11,1,4)
        reset_button.clicked.connect(lambda : self.reset_field(layout, cur_placing, rot_list, ship_buttons, ships_placed, done_lab, show_ship_label))

        #time left to place ship
        timer_cnt = [40]
        label_time = QLabel(self)
        label_time.setText("Seconds left: {}".format(timer_cnt[0]))
        layout.addWidget(label_time,2,11,1,4,Qt.AlignmentFlag.AlignCenter)
        self.placement_timer = QTimer()
        self.placement_timer.timeout.connect(lambda : self.place_timer(timer_cnt, label_time, pl_field))
        self.placement_timer.start(1000)

        #ships [name, width, length]
        ship_list = [['s1','1','2'],['s2','1','3'],['s3','1','4'],['s4','1','5'],['s5','2','3'],['s6','2','4'],['s7','2','5']]
        #list from server with index ||| set now for testing !!!!!
        ran_ships = [0, 2, 3, 5, 6]

        rot_list = ['horizontal']
        #button to rotate ship
        rot_but = QPushButton('rotate ship')
        layout.addWidget(rot_but,3,11,1,4)
        rot_but.clicked.connect(lambda : self.rotate_ship(rot_list, cur_placing, show_ship_label, visual_ship))

        #info for user on selected ship
        cur_placing = [' ', 0, 0, 0] #[name, length, width, (button)]

        #buttons to select which ship to place
        ship_buttons = []
        for i in range(0,5,1):
            ship = QPushButton("{}".format(ship_list[ran_ships[i]][0]))
            layout.addWidget(ship,i+4,11,1,4)
            ship_buttons.append(ship)
        for i in range(0,5,1):
            ship = ship_buttons[i]
            ship.clicked.connect(lambda _, x=i: self.selected_ship(x, ship_list, cur_placing, ran_ships, ship_buttons, rot_list, show_ship_label, visual_ship))
        
        #done
        ships_placed = [0]
        done_lab = QLabel(self)
        done_lab.setText("place ships to go on")
        layout.addWidget(done_lab,9,11)
        done_but = QPushButton('done placing')
        layout.addWidget(done_but,10,11,1,4)
        done_but.clicked.connect(lambda : self.done_placing(ships_placed, reset_button))

        #show ship
        show_ship_label = []
        for i in range(0,5,1):
            show_label = []
            for j in range(0,5,1):
                show_ship = QLabel(self)
                show_ship.setStyleSheet("background-color: white")
                show_ship.setFixedSize(50,50)
                layout.addWidget(show_ship,i+4,j+15)
                show_label.append(show_ship)
            show_ship_label.append(show_label)
    
    

    #rotate ship
    def rotate_ship(self, rot_list, cur_placing, show_ship_label, visual_ship):
        if (rot_list[0] == 'horizontal'):
            rot_list[0] = 'vertical'
        else:
            rot_list[0] = 'horizontal'
        visual_ship(cur_placing, rot_list, show_ship_label)

    
    #info to which ship is selected
    def selected_ship(self, x, ship_list, cur_placing, ran_ships, ship_buttons, rot_list, show_ship_label, visual_ship):
        cur_placing[0] = ship_list[ran_ships[x]][0]
        cur_placing[1] = ship_list[ran_ships[x]][2]
        cur_placing[2] = ship_list[ran_ships[x]][1]
        cur_placing[3] = ship_buttons[x]
        visual_ship(cur_placing, rot_list, show_ship_label)

    #reset the field if u wanna replace ships   
    def reset_field(self, layout, cur_placing, rot_list, ship_buttons, ships_placed, done_lab, show_ship_label):
        pl_field = []
        field_buttons = []
        for i in range(1,11,1):
            field = []   
            f_button = []
            for j in range(1,11,1):     
                fbuttons = QPushButton(" ")
                fbuttons.setFixedSize(50,50)
                fbuttons.setStyleSheet("background-color: white")
                layout.addWidget(fbuttons,i,j,Qt.AlignmentFlag.AlignCenter)
                f_button.append(fbuttons)
                field.append(' ')
            field_buttons.append(f_button)
            pl_field.append(field)
        for i in range(0,10,1):
            for j in range(0,10,1):
                field_button = field_buttons[i][j]
                field_button.clicked.connect(lambda _, x=i, y=j: self.try_place(x, y, field_buttons, pl_field, cur_placing, rot_list, ships_placed, done_lab, show_ship_label))
        for i in range(0,5,1):
            ship = ship_buttons[i]
            ship.setEnabled(True)
        done_lab.setText("place ships to go on")
        ships_placed[0] = 0
        

    #check if able to place ship
    def try_place(self, x, y, field_buttons, pl_field, cur_placing, rot_list, ships_placed, done_lab, show_ship_label):
        selected_ship = cur_placing[3]
        width = int(cur_placing[2])
        length = int(cur_placing[1])
        check_var = ' '
        if (rot_list[0] == 'horizontal'):
            if (width == 1):
                if (y+length > 10):
                    check_var = 'no'                
                else:                 
                    for i in range(y,y+length,1):
                        if (str(pl_field[x][i]) != ' '):
                            check_var = 'no'                         
                            break
                        else:
                            check_var = 'yes'                        
                    
            elif (width == 2):
                if (x == 9):
                    check_var = 'no'
                elif(y+length > 10):
                    check_var = 'no'
                else:                  
                    for j in range(x,x+width,1):
                        for i in range(y,y+length,1):
                            if (str(pl_field[j][i]) != ' '):
                                check_var = 'no'                             
                                break
                            else:
                                check_var = 'yes'                              
                
        elif (rot_list[0] == 'vertical'):
            if (width == 1):
                if (x+length > 10):
                    check_var = 'no'                  
                else:               
                    for i in range(x,x+length,1):
                        if (str(pl_field[i][y]) != ' '):
                            check_var = 'no'                          
                            break
                        else:
                            check_var = 'yes'                           
            elif(width == 2):
                if (y == 9):
                    check_var = 'no'                    
                elif(x+length > 10):
                    check_var = 'no'                 
                else:                   
                    for j in range(y,y+width,1):
                        for i in range(x,x+length,1):
                            if (str(pl_field[i][j]) != ' '):
                                check_var = 'no'
                                break
                            else:
                                check_var = 'yes'
                                
        if (cur_placing[0] != ' '):
            if(check_var == 'yes'):
                if (rot_list[0] == 'horizontal'):
                    if (width == 1):
                        for i in range(y,y+length,1):
                            disbutton = field_buttons[x][i]
                            disbutton.setStyleSheet("background-color: cyan") 
                            disbutton.setEnabled(False)
                            selected_ship.setEnabled(False)
                            pl_field[x][i] = cur_placing[0]
                        
                    elif (width == 2):
                        for j in range(x,x+width,1):
                            for i in range(y,y+length,1):
                                disbutton = field_buttons[j][i]
                                disbutton.setStyleSheet("background-color: cyan")
                                disbutton.setEnabled(False)
                                selected_ship.setEnabled(False)
                                pl_field[j][i] = cur_placing[0]
                    
                elif (rot_list[0] == 'vertical'):
                    if (width == 1):
                        for i in range(x,x+length,1):
                            disbutton = field_buttons[i][y]
                            disbutton.setStyleSheet("background-color: cyan")
                            disbutton.setEnabled(False)
                            selected_ship.setEnabled(False)
                            pl_field[i][y] = cur_placing[0]
                        
                    elif (width == 2):
                        for j in range(y,y+width,1):
                            for i in range(x,x+length,1):
                                disbutton = field_buttons[i][j]
                                disbutton.setStyleSheet("background-color: cyan")
                                disbutton.setEnabled(False)
                                selected_ship.setEnabled(False)
                                pl_field[i][j] = cur_placing[0]

                for i in range(0,5,1):
                    for j in range(0,5,1):
                        show_ship = show_ship_label[i][j]
                        show_ship.setStyleSheet("background-color: white")        
                cur_placing[0] = ' '
                ships_placed[0] = ships_placed[0]+1
                if (ships_placed[0] == 5):
                    done_lab.setText("done placing all ships")

    def done_placing(self, ships_placed, reset_button):
        reset_button.setEnabled(False)
        if (ships_placed[0] == 5):
            self.all_Ships_placed = True
    
    def place_timer(self, timer_cnt, label_time, pl_field):
        timer_cnt[0] -= 1
        label_time.setText("Seconds left: {}".format(timer_cnt[0]))
        if(timer_cnt[0] == 0):
            #send time over to server and go back to enemy window !!!
            self.placement_timer.stop()
            if self.all_Ships_placed == True:
                self.client.send_Ships(pl_field)
                #turn = self.client.receive()
                self.w = game_gui(self.client, self.is_Host, pl_field, self.username)
                self.w.show()
                self.close()

#ANCHOR game_gui
class game_gui(QWidget):
    def __init__(self, client, is_Host, pl_field, username):
        self.is_Host = is_Host
        self.username = username
        self.timer1 = QTimer()
        if(is_Host == True):
            self.player = 1
        else:
            self.player = 2
        self.client = client
        self.own_field = pl_field    
        super().__init__()

        layout = QGridLayout()
        
        self.setLayout(layout)

        self.statlabel_text = " "
        self.statlabel = QLabel(self)
        self.statlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.statlabel.setText("{}".format(self.statlabel_text))
        layout.addWidget(self.statlabel,12,1,1,21,Qt.AlignmentFlag.AlignCenter)

        #just labels for rows/columns
        for i in range(1,11,1):
            label_num = QLabel(self)
            label_num.setFixedSize(50,50)
            label_num.setStyleSheet("background-color: cyan")
            label_num.setText("{}".format(i))
            label_num.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label_num,0,i,Qt.AlignmentFlag.AlignCenter)
        
        letters = ['A','B','C','D','E','F','G','H','I','J']
        for i in range(1,11,1):
            label_let = QLabel(self)
            label_let.setFixedSize(50,50)
            label_let.setStyleSheet("background-color: cyan")
            label_let.setText("{}".format(letters[i-1]))
            label_let.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label_let,i,0,Qt.AlignmentFlag.AlignCenter)
        
        #field with buttons 
        game_field_buttons = []
        enable_buttons = []
        for i in range(1,11,1):
            field = []   
            f_button = []
            for j in range(1,11,1):     
                fbuttons = QPushButton(" ")
                fbuttons.setFixedSize(50,50)
                layout.addWidget(fbuttons,i,j,Qt.AlignmentFlag.AlignCenter)
                f_button.append(fbuttons)
                field.append(' ')
            game_field_buttons.append(f_button)
            enable_buttons.append(field)
        for i in range(0,10,1):
            for j in range(0,10,1):
                field_button = game_field_buttons[i][j]
                field_button.clicked.connect(lambda _, x=i, y=j: self.hit_coords(x, y, game_field_buttons, enable_buttons))

        for i in range(1,11,1):
            label_num = QLabel(self)
            label_num.setFixedSize(50,50)
            label_num.setStyleSheet("background-color: cyan")
            label_num.setText("{}".format(i))
            label_num.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label_num,0,i+12,Qt.AlignmentFlag.AlignCenter)
        
        letters = ['A','B','C','D','E','F','G','H','I','J']
        for i in range(1,11,1):
            label_let = QLabel(self)
            label_let.setFixedSize(50,50)
            label_let.setStyleSheet("background-color: cyan")
            label_let.setText("{}".format(letters[i-1]))
            label_let.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label_let,i,12,Qt.AlignmentFlag.AlignCenter)

        own_field_labels = []
        for i in range(1,11,1): 
            ownf_label = []
            for j in range(13,23,1):     
                flabels = QLabel(" ")
                flabels.setFixedSize(50,50)
                if(self.own_field[i-1][j-13] == ' '):
                    flabels.setStyleSheet("background-color: white")
                else:
                    flabels.setStyleSheet("background-color: grey")
                layout.addWidget(flabels,i,j,Qt.AlignmentFlag.AlignCenter)
                ownf_label.append(fbuttons)
            self.layout = layout
            own_field_labels.append(f_button)
            self.own_field_labels = own_field_labels

        if(self.player == 2):
            for i in range(0,10,1):
                for j in range(0,10,1):
                    game_field_buttons[i][j].setEnabled(False)
            self.timer1 = QTimer()
            self.timer1.timeout.connect(lambda : self.get_hit_list(game_field_buttons))
            self.timer1.start(15000)

    def get_hit_list(self, game_field_buttons):
        self.timer1.stop()
        flabels = QLabel(" ")
        flabels.setFixedSize(50, 50)
        hit_list = self.client.get_hit_list()
        if(hit_list[1] == 1):
            flabels.setStyleSheet("background-color: red")
            #own_field_labels[hit_list[0][0]][hit_list[0][1]].setStyleSheet("background-color: red")
            if(hit_list[3] == 1):
                if(hit_list[4] == 1):
                    box = QMessageBox()
                    box.setText("You have lost")
                    box.exec()
                    self.w = enemy_Window(self.client, self.username)
                    self.w.show()
                    self.destroy()
        else:
            flabels.setStyleSheet("background-color: blue")
        for i in range(10):
            for j in range(10):
                game_field_buttons[i][j].setEnabled(True)
            #own_field_labels[hit_list[0][0]][hit_list[0][1]].setStyleSheet("background-color: blue")
        self.layout.addWidget(flabels,hit_list[0][0]+1,hit_list[0][1]+13,Qt.AlignmentFlag.AlignCenter)
        self.show()

    
    def hit_coords(self, x, y, game_field_buttons, enable_buttons):
        print("click")
        coords_hit = f"{x},{y}"
        enable_buttons[x][y] = 'no' 
        hit_list = self.client.send_hit(coords_hit)
        for i in range(0,10,1):
                for j in range(0,10,1):
                    game_field_buttons[i][j].setEnabled(False)
        if hit_list[1] == 1:
            game_field_buttons[hit_list[0][0]][hit_list[0][1]].setStyleSheet("background-color: red")
            if(hit_list[3] == 1):
                self.statlabel.setText("hit {} and it's sunken".format(hit_list[2][0]))
                if(hit_list[4] == 1):
                    box = QMessageBox()
                    box.setText("You have won")
                    box.exec()
                    self.w = enemy_Window(self.client, self.username)
                    self.w.show()
                    self.destroy()
            else:
                self.statlabel.setText("hit {} but it's not sunken".format(hit_list[2][0]))
        else:
            self.statlabel.setText("didn't hit a ship")
            game_field_buttons[hit_list[0][0]][hit_list[0][1]].setStyleSheet("background-color: blue")
        self.timer1 = QTimer()
        self.timer1.timeout.connect(lambda : self.get_hit_list(game_field_buttons))
        self.timer1.start(15000)
        #print(coords_hit)
        #print(enable_buttons)

app = QApplication(sys.argv)
window = Login_Page()
window.show()
sys.exit(app.exec())