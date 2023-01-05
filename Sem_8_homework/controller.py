from view import ui as ui
from module import readData
from module import findEmployee
from module import salarySelection
from module import addNewEmployee
from module import deleteEmployee
from module import updateInfo
from module import exportData
from module import exportDataJson

def controller():
    position = -1
    while position != 0:
        position = ui()
        data = readData()
        if position == 1:
            print("Search by last name:")
            findEmployee(data)
        if position == 2:
            print("Search by position:")
            findEmployee(data)
        if position == 3:
            print("3: Select by salary rate. Input the salary amount for search: ")
            salarySelection(data)
        if position == 4:
            print("4: Add a new employee")
            addNewEmployee(data)
        if position == 5:
            print("5: Delete employee")
            deleteEmployee(data)
        if position == 6:
            print("6: Update the info about employee")  
            updateInfo(data)
        if position == 7:
            print("7: Export data into json")
            exportDataJson(data)
        if position == 8:
            print("8: Export data into csv")
            exportData(data)
        if position == 9:
            print("9: End of work")