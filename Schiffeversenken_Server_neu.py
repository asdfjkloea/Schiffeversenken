import Network
from threading import Thread
import os

global queue
queue = []

def check_win(pl_list):
    for i in range(0,10,1):
        for j in range(0,10,1):
            if(pl_list[i][j] != ' '):
                won = 0
                return won
            else:
                won = 1   
    return won

def check_hit(pl_list, data):
    check_hit_list = [] #list which will be sent to client
    #pl_hit = [0,1] #temp list with hit coords
    pl_hit = data[1]
    if(pl_list[pl_hit[0]][pl_hit[1]] != ' '):
        hit = 1                                  
        hit_ship = pl_list[pl_hit[0]][pl_hit[1]]
        pl_list[pl_hit[0]][pl_hit[1]] = ' '
        check_hit_list.append(pl_hit)           #hit coords
        check_hit_list.append(hit)              #variable if ship is hit || 1=ship hit  0=ship not hit
        check_hit_list.append(hit_ship)         #which ship is hit
        #loop to check if ship sunken or not
        for i in range(0,10,1):
            for j in range(0,10,1):
                if(pl_list[i][j] == hit_ship):
                    sunken = 0
                    check_hit_list.append(sunken) 
                    return check_hit_list
                else:
                    sunken = 1
                    win_check = check_win(pl_list)
        check_hit_list.append(sunken)           #ship sunken || 0=not sunken    1=sunken
        check_hit_list.append(win_check)        #variable if won || 0=didnt win     1=won 
    else:
        hit = 0                                 
        check_hit_list.append(pl_hit)           #hit coords
        check_hit_list.append(hit)              #variable if ship is hit || 1=ship hit  0=ship not hit
    return check_hit_list #check_hit_list = [[coords], didnt hit ship] ||| gui need to check check_hit_list[1]

def get_Player_invite(username):
    fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "r")
    data = []
    for i in fobj:
        data.append(i.strip("\n").split(","))
        for i in range(0, len(data)):
            if(data[i][0] == username):
                wins=int(data[i][4])
                losses=int(data[i][5])
                if(wins > 0 and losses == 0):                        #player has x wins and 0 losses = 100%winrate
                    winrate = "100%"
                elif(wins == 0 and losses > 0):                        #player has 0 wins and x losses = 0%winrate
                    winrate = "0%"
                elif(wins > 0 and losses > 0):                        #player has x wins and x losses = specific winrate
                    winrate = round(wins/losses,2)
                else:                                               #player has 0 wins and 0 losses = no games played yet
                    winrate = "No Games played yet"
                fobj.close()
                return data[i][3], winrate
    fobj.close
    return -99

def user_pw_übergeben(username, password, thread_number=99, playedrounds=0, wins=0,losses=0, online_status=True):
    fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "r")
    data = []
    for i in fobj:
        data.append(i.strip("\n").split(","))
        for i in range(0, len(data)):
            if (data[i][0] == username):        #check if username already exists, because redundancy = bad
                fobj.close
                return False
    fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "a")
    fobj.write(f"{username},{password},{thread_number},{playedrounds},{wins},{losses},{online_status},\n")
    fobj.close()
    return True

def get_user_online():      #look for Players that are currently online (return username & winrate)
    fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "r")
    data = []
    players_online = []
    for i in fobj:
        data.append(i.strip("\n").split(","))
    for i in data:
        if(i[6] == "True"):
            wins=int(i[4])
            losses=int(i[5])
            if(wins > 0 and losses == 0):                        #player has x wins and 0 losses = 100%winrate
                players_online.append([i[0], i[3],"100%"])
            elif(wins == 0 and losses > 0):                        #player has 0 wins and x losses = 0%winrate
                players_online.append([i[0], i[3],"0%"])
            elif(wins > 0 and losses > 0):                        #player has x wins and x losses = specific winrate
                players_online.append([i[0], i[3], round(wins/losses,2)])
            else:                                               #player has 0 wins and 0 losses = no games played yet
                players_online.append([i[0], i[3],"100%"])
    fobj.close()
    return players_online


def increase_losses(username):
    fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "r+")
    data = []
    for i in fobj:
        data.append(i.strip("\n").split(","))
        for i in range(0, len(data)):
            if (data[i][0] == username):
                password = data[i][1]
                thread_number = data[i][2]
                playedrounds = data[i][3]
                wins = data[i][4]
                losses = int(data[i][5])
                losses_new = losses + 1
                online_status = data[i][6]
                combined = f"{username},{password},{thread_number},{playedrounds},{wins},{losses},{online_status},"
                combined_new = f"{username},{password},{thread_number},{playedrounds},{wins},{losses_new},{online_status},"
                fobj.close()
                fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "r")
                text = fobj.read()
                fobj.close()
                fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "w")                
                fobj.write(text.replace(combined,combined_new))
                fobj.close()
                return True

def increase_wins(username):
    fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "r+")
    data = []
    for i in fobj:
        data.append(i.strip("\n").split(","))
        for i in range(0, len(data)):
            if (data[i][0] == username):
                password = data[i][1]
                thread_number = data[i][2]
                playedrounds = data[i][3]
                wins = int(data[i][4])
                wins_new = wins + 1
                losses = data[i][5]
                online_status = data[i][6]
                combined = f"{username},{password},{thread_number},{playedrounds},{wins},{losses},{online_status},"
                combined_new = f"{username},{password},{thread_number},{playedrounds},{wins_new},{losses},{online_status},"
                fobj.close()
                fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "r")
                text = fobj.read()
                fobj.close()
                fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "w")                
                fobj.write(text.replace(combined,combined_new))
                fobj.close()
                return True

def check_passwort(username,password,threadNr):     #compare sent username and password to file and set online status
    fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "r+")
    data = []
    for i in fobj:
        data.append(i.strip("\n").split(","))
        for i in range(0, len(data)):
            if (data[i][0] == username and data[i][1] == password):#compare sent username and password to file
                #Username and password correct
                thread_number = data[i][2]          #set the onlinestatus to True
                thread_number_new = threadNr        #user receives a unique Tread-Number
                playedrounds = data[i][3]
                wins = data[i][4]
                losses = data[i][5]
                online_status = data[i][6]
                online_status_new = 'True'
                combined = f"{username},{password},{thread_number},{playedrounds},{wins},{losses},{online_status},"
                combined_new = f"{username},{password},{thread_number_new},{playedrounds},{wins},{losses},{online_status_new},"
                fobj.close()
                fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "r")
                text = fobj.read()
                fobj.close()
                fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "w")                
                #print(combined_new)
                fobj.write(text.replace(combined,combined_new))
                fobj.close()
                return True

def get_ID(username):   #Get Thread number
    fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "r")
    data = []
    for i in fobj:
        data.append(i.strip("\n").split(","))
        for i in range(0, len(data)):
            if(data[i][0] == username):
                fobj.close()
                return data[i][2]       #return threadNo
    fobj.close
    return -99

def online_status_to_false(benutzer):
    fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "r+")
    data = []
    for i in fobj:
        data.append(i.strip("\n").split(","))
        for i in range(0, len(data)):
            if (data[i][0] == benutzer):#compare sent username and password to file
                password = data[i][1]
                thread_number = data[i][2]          #set the onlinestatus to True
                playedrounds = data[i][3]
                wins = data[i][4]
                losses = data[i][5]
                online_status = data[i][6]
                online_status_new = 'False'
                combined = f"{benutzer},{password},{thread_number},{playedrounds},{wins},{losses},{online_status},"
                combined_new = f"{benutzer},{password},{thread_number},{playedrounds},{wins},{losses},{online_status_new},"
                fobj.close()
                fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "r")
                text = fobj.read()
                fobj.close()
                fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "w")                
                #print(combined_new)
                fobj.write(text.replace(combined,combined_new))
                fobj.close()
                return True

class Handle_connection(Thread):
    def __init__(self, server, client, threadNr):
        super().__init__()
        self.server = server
        self.game  = -1
        self.own_field=[]
        self.enemy_ID = None
        self.enemy_field=[]
        self.own_field_hidden=[]
        self.enemy_field_hidden=[]
        self.client = client
        self.threadNr = threadNr
        self.username = None
        self.message = []
        self.pl_list = []

    
    def run(self):
        while(1):
            try:
                for data_queue in queue:
                    data = data_queue.split(";")
                    if(int(data[0]) == self.threadNr):
                        if(data[1] == "I"):
                            player_data = get_Player_invite(data[2])
                            self.message.append(f"I;{data[2]};{player_data[0]};{player_data[1]}")
                            queue.remove(data_queue)
                        elif data[1] == "A":
                            self.message.append(f"A;{data[2]}")
                        elif data[1] == "D":
                            self.message.append(f"D;{data[2]}")
                        elif data[1] == "F":
                            self.message.append(f"F;{data[2]}")
                        elif data[1] == "H":
                            self.message.append(f"H;{data[2]}")
            except:
                break
            try:
                data = self.server.receive(self.client)
            except TimeoutError: 
                continue
            except:
                online_status_to_false(self.username)
                break
            try:
                data = data.split(";")
                print(data[0])
                if data[0] == "L":
                    if check_passwort(data[1],data[2], threadNr) == True:
                        self.username = data[1]
                        self.server.send(self.client, True)
                    else:
                        self.server.send(self.client, False)

                elif data[0] == "R":
                    if user_pw_übergeben(data[1],data[2]) == True:
                        self.username = data[1]
                        self.server.send(self.client, True)
                    else:
                        self.server.send(self.client, False)

                elif data[0] == "B":
                    online = get_user_online()
                    for player in online:
                        self.server.send(self.client, f"{player[0]};{player[1]};{player[2]}")
                    self.server.send(self.client, "E")

                elif data[0] == "I":
                    ID = get_ID(data[1])
                    self.enemy_ID = ID
                    queue.append(f"{ID};I;{self.username}")
                
                elif data[0] == "G":
                    for message in self.message:
                        m = message.split(";")
                        if(m[0] == "I"):
                            self.server.send(self.client, self.message[0])
                            self.message.remove(message)
                    self.server.send(self.client, "E")

                elif data[0] == "C":
                    for message in self.message:
                        m = message.split(";")
                        if(m[0] == "A"):
                            self.server.send(self.client, "True")
                            self.server.send(self.client, m[1])
                        elif(m[0] == "D"):
                            self.server.send(self.client, "False")

                
                elif data[0] == "A":
                    ID = get_ID(data[1])
                    self.enemy_ID = ID
                    queue.append(f"{ID};A;{self.username}")

                elif data[0] == "D":
                    ID = get_ID(data[1])
                    queue.append(f"{ID};D;{self.username}")

                elif data[0] == "G1":
                    self.own_field = data[1]
                    queue.append(f"{self.enemy_ID};F;{self.own_field}")
                
                elif data[0] == "CF":
                    if self.pl_list == []:
                        for message in self.message:
                            m = message.split(";")
                            if(m[0] == "F"):
                                a = m[1].split("|")
                                for i in range(10):
                                    a[i] = a[i].split(",")
                                self.pl_list = a
                                self.message.remove(message)
                    #check_hit(self.pl_list, data)
                    data[1] = data[1].split(",")
                    data[1][0] = int(data[1][0])
                    data[1][1] = int(data[1][1])
                    hit_list = check_hit(self.pl_list, data)
                    a = ""
                    a += str(hit_list[0][0]) + "," + str(hit_list[0][1]) + "|"
                    for i in range(1, len(hit_list)):
                        a += str(hit_list[i]) + "|"
                    self.server.send(self.client, a)
                    queue.append(f"{self.enemy_ID};H;{a}")
                
                elif data[0] == "HL":
                    print("b")
                    for data_queue in queue:
                        data = data_queue.split(";")
                        if(int(data[0]) == self.threadNr):
                            if data[1] == "H":
                                self.message.append(f"H;{data[2]}")
                                print(data[2])
                    for message in self.message:
                        m = message.split(";")
                        if(m[0] == "H"):
                            hit_list = m[1]
                            self.message.remove(message)
                                
                    print("a")
                    # print(hit_list)
                    # print(type(hit_list))
                    # a = ""
                    # a += str(hit_list[0][0])
                    # print(a, hit_list[0][0])
                    # for i in range(1, len(hit_list)):
                    #     a += str(hit_list[i]) + "|"
                    self.server.send(self.client, hit_list)
                    print(hit_list)


            except:
                print("aaaaaa")
                break

IP = "127.0.0.1"
PORT = 44444

server = Network.Server_Net(IP, PORT)

threads=[]

while(1):
    client = server.server_Listen()
    threadNr = len(threads)
    t = Handle_connection(server, client, threadNr)
    t.start()
    threads.append(t)