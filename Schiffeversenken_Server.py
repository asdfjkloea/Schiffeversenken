import Network
from threading import Thread
import os

global queue
queue = []

def increase_playedrounds(username):
    fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "r+")
    data = []
    for i in fobj:
        data.append(i.strip("\n").split(","))
        for i in range(0, len(data)):
            if (data[i][0] == username):
                password = data[i][1]
                thread_number = data[i][2]
                playedrounds = int(data[i][3])
                playedrounds_new = playedrounds +1
                wins = data[i][4]
                losses = data[i][5]
                online_status = data[i][6]
                combined = f"{username},{password},{thread_number},{playedrounds},{wins},{losses},{online_status},"
                combined_new = f"{username},{password},{thread_number},{playedrounds_new},{wins},{losses},{online_status},"
                fobj.close()
                fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "r")
                text = fobj.read()
                fobj.close()
                fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "w")                
                fobj.write(text.replace(combined,combined_new))
                fobj.close()
                return True

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
    print("error")
    fobj.close
    return -99

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
    #print("wrong password / Username")
    fobj.close()
    return False

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
                players_online.append([i[0], "100%"])
            elif(wins == 0 and losses > 0):                        #player has 0 wins and x losses = 0%winrate
                players_online.append([i[0], "0%"])
            elif(wins > 0 and losses > 0):                        #player has x wins and x losses = specific winrate
                players_online.append([i[0], round(wins/losses,2)])
            else:                                               #player has 0 wins and 0 losses = no games played yet
                players_online.append([i[0], "No Games played yet"])
    fobj.close()
    return players_online
    
def get_ID(username):   #Get Thread number
    fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "r")
    data = []
    for i in fobj:
        data.append(i.strip("\n").split(","))
        for i in range(0, len(data)):
            if(data[i][0] == username):
                fobj.close()
                return data[i][2]       #return threadNo
    print("error")      #no threadnumber found at this username
    fobj.close
    return -99
   
def user_pw_übergeben(username, password, thread_number=99, playedrounds=0, wins=0,losses=0, online_status=True):
    fobj = open(os.path.dirname(os.path.abspath(__file__))+"\\testablage.txt", "a")     #Create new file (if not existing yet) in the same directory as the code
    fobj.write(f"{username},{password},{thread_number},{playedrounds},{wins},{losses},{online_status},\n")
    fobj.close()

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
        self.client = client
        self.threadNr = threadNr
        self.username = None
        self.message = []

    
    def run(self):
        while(1):
            try:
                for data_queue in queue:
                    data = data_queue.split(";")
                    print(data[0], self.threadNr)
                    if(int(data[0]) == self.threadNr):
                        if(data[1] == "I"):
                            print(data)
                            player_data = get_Player_invite(data[2])
                            self.message.append(f"I;{data[2]};{player_data[0]};{player_data[1]}")
                data = self.server.receive(self.client)
                data = data.split(";")
                print(data[0])
                if data[0] == "L":
                    if check_passwort(data[1],data[2],self.threadNr) == True:
                        print("Passwort korrekt")
                        self.username = data[1]
                        self.server.send(self.client, True)
                    else:
                        self.server.send(self.client, False)

                elif data[0] == "R":
                    if user_pw_übergeben(data[1],data[2]) == True:
                        print("Registrieren erfolgreich")
                        self.username = data[1]
                        self.server.send(self.client, True)
                    else:
                        self.server.send(self.client, False)

                elif data[0] == "B":
                    online = get_user_online()
                    print(online)
                    for player in online:
                        self.server.send(self.client, f"{player[0]};{player[1]};{player[2]}")
                    self.server.send(self.client, "E")

                elif data[0] == "I":
                    ID = get_ID(data[1])
                    queue.append(f"{ID};I;{self.username}")
                
                elif data[0] == "G":
                    for message in self.message:
                        m = message.split(";")
                        if(m[0] == "I"):
                            self.server.send(self.client, self.message[0])
                            self.message.pop(0)
                    self.server.send("E")

            except:
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