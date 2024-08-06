import socket

def client_program():
    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # get the local machine name
    host = socket.gethostname()
    port = 12345
    
    # connect to the server
    client_socket.connect((host, port))
    
    while True:
        # send data to the server
        message = input(" -> ")
        client_socket.send(message.encode())
        
        if message.lower() == 'bye':
            break
        
        # receive data from the server
        data = client_socket.recv(1024).decode()
        print(f"Received from server: {data}")
        
        if data.lower() == 'bye':
            break
    
    client_socket.close()

if __name__ == '__main__':
    client_program()
