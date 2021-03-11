#Serv.py : Spellcheck (Server File)
#Name: Akshat Shah
#Student ID: 1001872075

#Importing the socket package
import socket

# Create a socket object                          # Author : Geek for geeks
s = socket.socket()                               # Title : Socket Programming in Python
# Get local machine name                          # URL : https://www.geeksforgeeks.org/socket-programming-python/
host = socket.gethostname()
# Reserve a port for your service
port = 12345
# Bind to the port
s.bind((host, port))
# Now wait for client conncetion request.
s.listen(4)
# Created required arrays
arr = []
usr = []
lex = []
# Checking conditions for the username
while True:
    # Accepting the connection request from the client
    c, addr = s.accept()
    # Establish connection with the client
    userName = c.recv(1024).decode()
    fileData = c.recv(1024).decode()
    flag = 0

    # For loop verify the user credentials            # Author : tutorialspoint
    print("file data = ", fileData)                   # Title : for Loops for python
    for i in range(0, len(usr)):                      # URL : https://www.tutorialspoint.com/python/python_for_loop.htm
        if (userName == usr[i]):
            flag = 1
            break

    if flag == 0:
        usr.append(userName)
    else:
        msg = "User already exixts !!!"
        # Printing the Error Message that the user exists
        print(msg)
        s.close()

    # Printing the connected users and their network information
    print("The conncected Users are : ", usr)
    print("Got connection from ", addr)

    # Reading the user supplied text file
    data = fileData
    words = data.split()

    # Reading the server lexicon file
    file = open("Lexicon.txt")
    data = file.read()
    lexicons = data.split()
    # Initializing a variable "finalString" to store the output of the updated file

    finalString = ""

    # For loop for comparing the objects of both the lexicon and the user file
    for i in range(0, len(words)):                     # Author : tutorialspoint
        flag = 0                                       # Title : for Loops for python
        for j in range(0, len(lexicons)):              # URL : https://www.tutorialspoint.com/python/python_for_loop.htm
            if (words[i]==lexicons[j]):
                flag = 1
                break

        if flag ==1:
            finalString += "[" + words[i] + "]"

        else:
            finalString += words[i] + " "

    finalString = finalString[:-1]                  # Author : w3schools.com
    f = open("update.txt", "x")                     # Title : Python file write
    f.write(finalString)                            # URL : https://www.w3schools.com/python/python_file_write.asp
    f.close()

 # Printing the output into the finalString
    print("Final String = ", finalString)

# Terminating the connection.
s.close()





