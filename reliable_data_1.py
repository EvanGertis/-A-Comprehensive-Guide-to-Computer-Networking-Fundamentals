import socket

# Create socket
s = socket.socket()  

# Bind socket to port
port = 5001
s.bind(('', port))   

# Listen for connections
s.listen(1)

while True:
   # Accept connection
   clientsocket, addr = s.accept()  
        
   # Receive message
   msg = clientsocket.recv(1024).decode()
        
   print(f"Message received: {msg}")
          
   # Send response     
   clientsocket.send("Message received!".encode())