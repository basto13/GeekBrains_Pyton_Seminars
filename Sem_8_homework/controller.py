from view import ui as ui
from module import readData
from module import findEmployee

def controller():
    position = -1
    while position != 0:
        position = ui()
        data = readData()
        if position == 1:
            findEmployee(data)
        if position == 2:
            print("2: Select by position")
        if position == 3:
            print("3: Select by salary range")
        if position == 4:
            print("4: Add a new employee")
        if position == 5:
            print("5: Delete employee")
        if position == 6:
            print("6: Update the info about employee")      
        if position == 7:
            print("7: Export data into json")
        if position == 8:
            print("8: Export data into csv")
        if position == 9:
            print("9: End of work")
