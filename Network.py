#import libraries
import socket
import pickle
import time

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

    def login(self, username, password):
        #send info
        self.send("L;"+username+";"+password)
        #receive True Or  False
        TOF = self.receive()
        return TOF

    def register(self, username, password):
        #send
        self.send("R;{};{}".format(username,password))
        TOF = self.receive()
        return TOF

    def get_Players(self):
        clist = []
        self.send("B")
        while(1):
            data = self.receive()
            if(data == "E"):
                break
            data = data.split(";")
            clist.append(data)
        return clist
        

    def request_player(self, username):
        self.send("I;{}".format(username))

    def check_Request(self):
        self.send("C")
        msg = self.receive()
        if msg == "True":
            msg = self.receive()
            return msg
        else:
            return False

    def got_invited(self):
        self.send("G")
        invites = []
        while(1):
            invite = self.receive()
            #print(invite)
            if(invite == "E"):
                break
            invite = invite.split(";")
            invites.append([invite[1], invite[2], [invite[3]]])
        return invites

    def send_Ships(self, field):
        field2 = ""
        for x in range(10):
            for y in range(10):
                field2 += field[x][y] + ","
            field2 += "|"
        self.send(f"G1;{field2}")

    
    def accepted(self, username):
        self.send(f"A;{username}")

    def denied(self, username):
        self.send(f"D;{username}")
    
    def send_hit(self, coords_hit):
        self.send(f"CF;{coords_hit}")
        hit_list = self.receive()
        print(hit_list)
        hit_list = hit_list.split("|")
        for i in range(len(hit_list)):
            hit_list[i] = hit_list[i].split(",")
        hit_list[0][0] = int(hit_list[0][0])
        hit_list[0][1] = int(hit_list[0][1])
        for i in range(1, len(hit_list)-1):
            try:
                print(hit_list[i])
                hit_list[i] = int(hit_list[i][0])
            except:
                pass
        print(hit_list)
        return hit_list
    
    def get_hit_list(self):
        self.send("HL")
        hit_list = "True"
        while(hit_list == "True"):
            hit_list = self.receive()
        print(hit_list, "asdf")
        try:
            hit_list = hit_list.split("|")
            for i in range(len(hit_list)):
                hit_list[i] = hit_list[i].split(",")
        except:
            pass
        print(hit_list)
        hit_list[0][0] = int(hit_list[0][0])
        hit_list[0][1] = int(hit_list[0][1])
        for i in range(1, len(hit_list)-1):
            try:
                hit_list[i] = int(hit_list[i][0])
            except:
                pass
        print(hit_list)
        return hit_list

#server network class
class Server_Net(Network):
    def __init__(self, ip, port):
        super().__init__()
        self.ip = ip
        self.port = port
        self.connection.bind((self.ip, self.port))
        self.connection.listen(8)
    
    #send function for server, to choose client connection
    def send(self,conn,data):
        conn[0].send(pickle.dumps(data))
    
    #function to listen for incomming connections from clients
    def server_Listen(self):
        client_connection, client_address = self.connection.accept()
        client_connection.settimeout(100)
        return client_connection, client_address