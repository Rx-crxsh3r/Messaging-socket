import socket

def server_program():
    # create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # get the local machine name
    host = socket.gethostname()
    port = 12345
    
    # bind the socket to the port
    server_socket.bind((host, port))
    
    # configure how many clients the server can listen simultaneously
    server_socket.listen(2)
    print("Server is listening...")
    
    # accept a connection
    conn, address = server_socket.accept()
    print(f"Connection from {address} has been established!")
    
    while True:
        # receive data from the client
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Received from client: {data}")
        
        # send data to the client
        message = input(" -> ")
        conn.send(message.encode())
        
        if message.lower() == 'bye':
            break
    
    conn.close()
    server_socket.close()

if __name__ == '__main__':
    server_program()
