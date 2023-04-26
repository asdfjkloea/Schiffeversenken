import sys

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class ship_placement(QWidget):
    def __init__(self):
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
        timer_cnt = [120]
        label_time = QLabel(self)
        label_time.setText("Seconds left: {}".format(timer_cnt[0]))
        layout.addWidget(label_time,2,11,1,4,Qt.AlignmentFlag.AlignCenter)
        self.placement_timer = QTimer()
        self.placement_timer.timeout.connect(lambda : self.place_timer(timer_cnt, label_time))
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
        print(ship_buttons)
        for i in range(0,5,1):
            ship = ship_buttons[i]
            ship.clicked.connect(lambda _, x=i: self.selected_ship(x, ship_list, cur_placing, ran_ships, ship_buttons, rot_list, show_ship_label, visual_ship))
            print(ship)
        
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
        print('reset')
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
        print(pl_field)
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
                    print('no')
                elif(y+length > 10):
                    check_var = 'no'
                    print('no')
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
                print(ships_placed[0])
                if (ships_placed[0] == 5):
                    done_lab.setText("done placing all ships")
                print(pl_field)

             
    def done_placing(self, ships_placed, reset_button):
        reset_button.setEnabled(False)
        if (ships_placed[0] == 5):
            print('done') #go on later
    
    def place_timer(self, timer_cnt, label_time):
        timer_cnt[0] -= 1
        label_time.setText("Seconds left: {}".format(timer_cnt[0]))
        print(timer_cnt)
        if(timer_cnt[0] == 0):
            print('time over')
            self.placement_timer.stop()
            #send time over to server and go back to enemy window !!!


    



app = QApplication(sys.argv)
place = ship_placement()
place.show()
app.exec()