import sys

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class ship_placement(QWidget):
    def __init__(self):
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
                field_button.clicked.connect(lambda _, x=i, y=j: self.try_place(x, y, field_buttons, pl_field, cur_placing, rot_list, cur, ships_placed, done_lab))
        
        #button to reset field
        reset_button = QPushButton('reset')
        layout.addWidget(reset_button,0,11,1,4)
        reset_button.clicked.connect(lambda : self.reset_field(layout, cur_placing, rot_list, cur, ship_buttons, ships_placed, done_lab))
 
        #ships [name, width, length]
        ship_list = [['s1','1','2'],['s2','1','3'],['s3','1','4'],['s4','1','5'],['s5','2','3'],['s6','2','4'],['s7','2','5']]
        #list from server with index ||| set now for testing !!!!!
        ran_ships = [0, 2, 3, 5, 6]

        #rotation info for user
        rot_list = ['horizontal']
        rot_lab = QLabel(self)
        rot_lab.setText("current rotation: {}".format(rot_list[0]))
        layout.addWidget(rot_lab,1,11,Qt.AlignmentFlag.AlignCenter)
        #button to rotate ship
        rot_but = QPushButton('rotate ship')
        layout.addWidget(rot_but,2,11,1,4)
        rot_but.clicked.connect(lambda : self.rotate_ship(rot_list, rot_lab))

        #info for user on selected ship
        cur_placing = [' ', 0, 0, 0] #[name, length, width, (button)]
        cur = QLabel(self)
        cur.setText("currently placing: {}".format(cur_placing[0]))
        layout.addWidget(cur,3,11)

        #buttons to select which ship to place
        ship_buttons = []
        for i in range(0,5,1):
            ship = QPushButton("{} ({}x{})".format(ship_list[ran_ships[i]][0],ship_list[ran_ships[i]][1],ship_list[ran_ships[i]][2]))
            layout.addWidget(ship,i+4,11,1,4)
            ship_buttons.append(ship)
        print(ship_buttons)
        for i in range(0,5,1):
            ship = ship_buttons[i]
            ship.clicked.connect(lambda _, x=i: self.selected_ship(x, ship_list, cur_placing, cur, ran_ships, ship_buttons))
            print(ship)
        
        #done
        ships_placed = [0]
        done_lab = QLabel(self)
        done_lab.setText("place ships to go on")
        layout.addWidget(done_lab,9,11)
        done_but = QPushButton('done placing')
        layout.addWidget(done_but,10,11,1,4)
        done_but.clicked.connect(lambda : self.done_placing(ships_placed, reset_button))


    #rotate ship
    def rotate_ship(self, rot_list, rot_lab):
        if (rot_list[0] == 'horizontal'):
            rot_list[0] = 'vertical'
        else:
            rot_list[0] = 'horizontal'
        rot_lab.setText("current rotation: {}".format(rot_list[0]))
    
    #info to which ship is selected
    def selected_ship(self, x, ship_list, cur_placing, cur, ran_ships, ship_buttons):
        cur_placing[0] = ship_list[ran_ships[x]][0]
        cur.setText("currently placing: {}".format(cur_placing[0]))
        cur_placing[1] = ship_list[ran_ships[x]][2]
        cur_placing[2] = ship_list[ran_ships[x]][1]
        cur_placing[3] = ship_buttons[x]

    #reset the field if u wanna replace ships   
    def reset_field(self, layout, cur_placing, rot_list, cur, ship_buttons, ships_placed, done_lab):
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
                field_button.clicked.connect(lambda _, x=i, y=j: self.try_place(x, y, field_buttons, pl_field, cur_placing, rot_list, cur, ships_placed, done_lab))
        for i in range(0,5,1):
            ship = ship_buttons[i]
            ship.setEnabled(True)
        done_lab.setText("place ships to go on")
        print(pl_field)
        ships_placed[0] = 0
             

    #check if able to place ship
    def try_place(self, x, y, field_buttons, pl_field, cur_placing, rot_list, cur, ships_placed, done_lab):
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

                if (rot_list[0] == 'vertical'):
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
                cur_placing[0] = ' '
                ships_placed[0] = ships_placed[0]+1
                print(ships_placed[0])
                if (ships_placed[0] == 5):
                    done_lab.setText("done placing all ships")
                cur.setText("currently placing: {}".format(cur_placing[0]))
                print(pl_field)

             
    def done_placing(self, ships_placed, reset_button):
        reset_button.setEnabled(False)
        if (ships_placed[0] == 5):
            print('done') #go on later
    




app = QApplication(sys.argv)
place = ship_placement()
place.show()
app.exec()