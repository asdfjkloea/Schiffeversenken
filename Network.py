#import libraries
import socket
import pickle

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
        print(str(TOF))
        return TOF

    def register(self, username, password):
        #send
        self.send("R;{};{}".format(username,password))
        TOF = self.receive()
        print(TOF)
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
        print(clist)
        return clist
        

    def request_player(self, username):
        client.send("I;{}".format(username))

    def check_Request(self):
        pass

    def got_invitet(self):
        client.send("G")
        invites = []
        while(1):
            invite = client.receive()
            if(invite == "E"):
                break
            invite = invite.split(";")
            invites.append([invite[1], invite[2], [invite[3]]])
        return invites

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
        return client_connection, client_address


#testing
if __name__ == '__main__':
    import threading
    IP = "localhost"
    PORT = 65500
    
    def serverTest():
        server = Server_Net()
        client1 = server.server_Listen(IP,PORT)
        print(server.receive(client1))
        server.send(client1, "Hello from Server!")
    t = threading.Thread(target=serverTest)
    t.start()
    
    client = Client_Net()
    client.client_Connect(IP,PORT)
    client.send("Hello from Client!")
    print(client.receive())
    t.join()