from view import user_ui as ui
from module import readData
from module import addData
from module import findContact


def controller():
    position = -1

    while position != 0:
        position = ui()
        data = readData()
        print(data)
        if position == 1:
            print("1: input new data")
            addData(data)
        if position == 2:
                print("2: find data")
                findContact(data)
        if position == 3:
                print("3: import data")
        if position == 4:
                print("4: export data")
        if position == 5:
                print("5: print data")
    else:
        print("end of work")