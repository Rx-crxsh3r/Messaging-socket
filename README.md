This project is created to furthur understand the usages of the socket library by implementing a messaging processes.<br />
To use the project, run the sendersocket.py first then run the recieversocket.py<br />

How each work:<br />
(Sendersocket.py)<br />
```
-Create a socket object.<br />
-Bind it to a port (12345 in this case).
-Put the socket into listening mode.
-Accept a connection from a client.
-Continuously receive data from the client and print it.
-Prompt the server user to send a message to the client.
-Break the loop and close the connection if the message is "bye".
```
(Recieversocket.py)<br />
```
-Create a socket object.
-Connect to the server.
-Continuously prompt the client user to send a message to the server.
-Receive data from the server and print it.
-Break the loop and close the connection if the message is "bye".
```
