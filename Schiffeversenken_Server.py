import Network
from threading import Thread

global queue
queue = []

def get_Player_invite(player):
    return 30, 80

def user_pw_übergeben(benutzer, passwort):
    print (benutzer)
    print (passwort)
    return True

def get_user_online():
    return [["johannes",23,50],["elias",10,0],["jönsn",23,50],["luca",1,1]]

def check_passwort(benutzer, passwort):
    return True

def get_ID(benutzer):
    return 0

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
                    if check_passwort(data[1],data[2]) == True:
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