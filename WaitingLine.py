def addToLine(line):
    if line[0] == 0:
        line.append(1)
        del line[0]
        print(line[0])
    
    else:
        nextNum = len(line) + 1
        line.append(nextNum)
    return line

def displayLineCount(line):
    for x in range(len(line)):
        print(line[x])

    return line

def removeFromLine(line, number):
    lineSpot = int(number) - 1
    del line[lineSpot]
    for x in range(lineSpot, len(line)):
        line[x] = x + 1

    return line
    
waitingLine = [0, ]

option = None
while option != "4":
    print("1) Add to the line")
    print("2) Display the current line")
    print("3) Remove from the line")
    print("4) Exit the program")
    option = input("> ")
    if option == "1":
        addToLine(waitingLine)

    elif option == "2":
        displayLineCount(waitingLine)

    elif option == "3":
        number = input("Input number to remove: ")
        removeFromLine(waitingLine, number)

    print()
