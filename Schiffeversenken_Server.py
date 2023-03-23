import Network
from threading import Thread

class Handle_connection(Thread):
    def __init__(self, server, client):
        super().__init__()
        self.server = server
        self.client = client
    
    def run(self):
        while(1):
            try:
                data = self.server.receive(self.client)
                data = data.split(";")
                print(data[0])
            except:
                break

IP = "127.0.0.1"
PORT = 44444

server = Network.Server_Net(IP, PORT)

while(1):
    client = server.server_Listen()
    t = Handle_connection(server, client)
    t.start()