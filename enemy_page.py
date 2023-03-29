from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys

#temp list for testing
user_info =['user','342','30']

#need user_info for request like ['username','games played','wlr']
'''
#window to accept/deny request
class request_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 300)
        self.setWindowTitle("game request")

        label = QLabel(self)
        label.resize(500,15)
        label.setText("Wanna play against {}? Games played: {} WLR: {}".format(user_info[0], user_info[1], user_info[2]))
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
        print("True") #test

    def request_deny(self):
        #client.send("False")
        print("False") #test
''' 

class enemy_Window(QWidget):
    def __init__(self):
        super().__init__()
        #temp list for testing|later need users from server
        user_list = [['1','2','3'],['2','4','3']]
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
        var_list[0] = [['2','1','3'],['2','hallo','3'],['3','hi','no']]
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
        print("reload")
        print(var_list[0])
        print(var_list[1])
        






app = QApplication(sys.argv)
ewindow = enemy_Window()
ewindow.show()
sys.exit(app.exec())
'''
app = QApplication(sys.argv)
rwindow = request_Window()
rwindow.show()
sys.exit(app.exec())
'''