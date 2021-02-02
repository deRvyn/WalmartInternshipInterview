# importing modules
import math
import os

# initializing variables
sfile = ""
dRowB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
dRowD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
dRowF = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
dRowH = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
dRowJ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
dRequests = {}
dAssignments = {}
aKeys = {}

# functions

# function that chooses the seats on empty rows
def ChooseSeatsEmptyRow(dRow, cLetter):
    output = ""
    
    # ensures that the seats are perfectly surrounding the middle, always grabbing one of the two best seats
    pos = 10 - math.ceil((dRequests[key]/2))
    while dRequests[key] > 0:
        if dRequests[key] > 1:
            output += cLetter + str(dRow.pop(pos)) + ", "
            dRequests[key] -= 1
        else:
            output += cLetter + str(dRow.pop(pos))
            dRequests[key] -= 1
    # getting rid of 3 seats on the right side of the requested
    for n in range(3):
        try:
            dRow.pop(pos)
        except:
            pass
    # getting rid of 3 seats on the left
    pos -= 1
    for n in range(3):
        try:
            dRow.pop(pos)
            pos -= 1
        except:
            pass
    # assigns output to seating assignment dictionary
    dAssignments[key] = output

# function that chooses seats when the row isn't empty (starts on the left, and goes to the right)
def ChooseSeats(dRow, cLetter):
    output = ""
    
    # starts on the left, goes to any available seat
    pos = 0
    while dRequests[key] > 0:
        if dRequests[key] > 1:
            output += cLetter + str(dRow.pop(pos)) + ", "
            dRequests[key] -= 1
        else:
            output += cLetter + str(dRow.pop(pos))
            dRequests[key] -= 1
    # gets rid of 3 seats on the right side, if any
    for n in range(3):
        try:
            dRow.pop(pos)
        except:
            pass
    # assigns output to seating assignment dictionary
    dAssignments[key] = output

# print out input message
print("Which file would you like to use?")

# get file input for assigning seats, and open it
sFile = input()
file = open(sFile, 'r')

# assigning the request file contents to a dictionary, 
# and creating a dictionary to overwrite
for line in file:
    (key, val) = line.split()
    dRequests[str(key)] = int(val)

# opens the file and reads it into the seating assignments dictionary
file = open(sFile, 'r')

for line in file:
    (key, val) = line.split()
    dAssignments[str(key)] = val

# going through each request and assigning seats, starting with the middle of each available row, and then restarting on the edges of the most central row
for key in dRequests:
    if len(dRowF) == 20 and len(dRowF) >= dRequests[key]:
        ChooseSeatsEmptyRow(dRowF, "F")
    elif len(dRowH) == 20 and len(dRowH) >= dRequests[key]:
        ChooseSeatsEmptyRow(dRowH, "H")
    elif len(dRowD) == 20 and len(dRowD) >= dRequests[key]:
        ChooseSeatsEmptyRow(dRowD, "D")
    elif len(dRowJ) == 20 and len(dRowJ) >= dRequests[key]:
        ChooseSeatsEmptyRow(dRowJ, "J")
    elif len(dRowB) == 20 and len(dRowB) >= dRequests[key]:
        ChooseSeatsEmptyRow(dRowB, "B")        
    elif len(dRowF) >= dRequests[key]:
        ChooseSeats(dRowF, "F")
    elif len(dRowH) >= dRequests[key]:
        ChooseSeats(dRowH, "H")
    elif len(dRowD) >= dRequests[key]:
        ChooseSeats(dRowD, "D")
    elif len(dRowJ) >= dRequests[key]:
        ChooseSeats(dRowJ, "J")
    elif len(dRowB) >= dRequests[key]:
        ChooseSeats(dRowB, "B")

# clear any old file contents
open('output.txt', 'w').close()

# loops through the dictionary, printing the movie seats for each request
for key, value in dAssignments.items():
    with open('output.txt', 'a') as f:
        print(key, value, file=f)

# closes the file
file.close()

# return the path
print("Output File Path:")
print(os.path.abspath("output.txt"))