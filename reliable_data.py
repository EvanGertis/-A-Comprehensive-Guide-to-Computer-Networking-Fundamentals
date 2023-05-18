import socket 

# Create socket
s = socket.socket()  

# Bind socket to port 
port = 5001  
s.bind(('', port))  

# Listen for connections
s.listen(5)
print ("Listening on port {}".format(port))

while True:
    # Accept connection from client
    clientsocket, addr = s.accept()      
   
    # Receive data from client 
    data = clientsocket.recv(1024).decode()
    
    print("Data received: {}".format(data))
    
    # Check if data is corrupted
    if self.check_data(data):
        print("Data is corrupted!")
        
        # Resend data request
        clientsocket.send("Resend".encode())  
    
    else: 
        # Data is valid
        
        # Send confirmation to client
        clientsocket.send("Data received".encode())
        
    clientsocket.close()