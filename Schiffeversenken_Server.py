import Network
from threading import Thread

def user_pw_übergeben(benutzer, passwort):
    print (benutzer)
    print (passwort)
    return True

def get_user_online():
    return [["johannes",23,50],["sandro",50,0]]

def check_passwort(benutzer, passwort):
    return True

def get_ID(benutzer):
    return 1

class Handle_connection(Thread):
    def __init__(self, server, client):
        super().__init__()
        self.server = server
        self.client = client
        self.connect_to_thread = False
        self.message = ""

    
    def run(self):
        while(1):
            try:
                data = self.server.receive(self.client)
                data = data.split(";")
                print(data[0])
                if data[0] == "L":
                    if check_passwort(data[1],data[2]) == True:
                        print("Passwort korrekt")
                if data[0] == "R":
                    if user_pw_übergeben(data[1],data[2]) == True:
                        print("Registrieren erfolgreich")
                if data[0] == "B":
                    online = get_user_online
                    print(online)
                if data[0] == "I":
                    
            except:
                break

IP = "127.0.0.1"
PORT = 44444

server = Network.Server_Net(IP, PORT)

threads=[]

while(1):
    client = server.server_Listen()
    t = Handle_connection(server, client)
    t.start()
    threads.append(t)