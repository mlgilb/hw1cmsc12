from socket import *

# Using the Wi-Fi IP address to connect to the server
serverName = '10.246.128.212'  # Server's IP address (Wi-Fi address)
serverPort = 12000  # Port the server is listening on

# Create a client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to the server
clientSocket.connect((serverName, serverPort))

# Get user input for the string and the operations
sentence = input('Input string: ')
options = input('Select operations (1 = upper, 2 = lower, 3 = length, 4 = vowels, 5 = words): ')

# Send the string and options to the server
message = f"{sentence},{options}"
clientSocket.send(message.encode())

# Receive the result from the server
modifiedSentence = clientSocket.recv(2048).decode()

# Display the result
print("\nServer Response:")
print(modifiedSentence)

clientSocket.close()
