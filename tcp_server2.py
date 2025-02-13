from socket import *

def process_string(user_input, options):
    result = {}
    if '1' in options:
        result['upper_case'] = user_input.upper()
    if '2' in options:
        result['lower_case'] = user_input.lower()
    if '3' in options:
        result['length'] = len(user_input)
    if '4' in options:
        result['vowel_count'] = sum(1 for char in user_input if char.lower() in 'aeiou')
    if '5' in options:
        result['word_count'] = len(user_input.split())
    return result

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while 1:
    print("Waiting ...")
    connectionSocket, addr = serverSocket.accept()
    print("accept")
    
    # Receive data from the client
    data = connectionSocket.recv(2048).decode()
    string_data, options = data.split(',')
    options = options.split()  # Split the options by spaces (e.g., '1 3 5')
    
    # Process the string based on the options
    results = process_string(string_data, options)
    
    # Format the results and send back to the client
    response = '\n'.join([f"{key}: {value}" for key, value in results.items()])
    connectionSocket.send(response.encode())
    
    connectionSocket.close()
