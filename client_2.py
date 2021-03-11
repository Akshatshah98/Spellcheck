# Client_2.py : Second Client FIle.
# Name : Akshat Shah
# Student ID : 1001872075

# Importing necessary packages
from tkinter import*
from tkinter import filedialog
# Import socket module
import socket

# Initializing variables
filename = ""
filename1 = ""
fileData = ""

# Create a socket object
s = socket.socket()                     # Author : Geeks for Geeks
# Get local machine Name                # Title : Socket Programming
host = socket.gethostname()             # URL : https://www.geeksforgeeks.org/socket-programming-python/
# Reserve a port for the service
port = 12345
# Connecting with the server
s.connect((host, port))
name = input("Enter your username : ")

# # defining buttons and label for the client form page.

def UploadAction(event=None):               # Calling function in line: 40
    filename: object = filedialog.askopenfilename()
    print('Selected:', filename)            # Author : Tutorials Point
    global filename1                        # Title : Uploading files in Python
    filename1 = filename                    # URL : https://www.tutorialspoint.com/file-upload-example-in-python


# Create windows object
app = Tk()


# root = tk.Tk()
UploadAction_btn = Button(app, text='Select a file', width=25, command=UploadAction)
UploadAction_btn.grid(row=4, column=12, pady=20)

# Defining form Windows size.
app.title('Spell Check')
app.geometry('900x550')

# Start Program
app.mainloop()


# Defining a variable named result
result = ""

# Prompting user to enter username
# name = input("Enter your username : ")
# print("", filename1)

# Sending name of the user in bytes to the server
s.send(bytes(name, 'utf-8'))

# Reading and accessing the user's uploaded file
f = open(filename1, "r")                    # Author : w3schools
fileData = f.read()                         # Title : Python read write file
s.send(bytes(fileData, 'utf-8'))            # URL : https://www.w3schools.com/python/python_file_write.asp
# Terminating the socket connection
s.close()
