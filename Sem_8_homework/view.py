def user_ui():
    print("Employees' list.")
    print("1: Find an employee")
    print("2: Select by position")
    print("3: Select by salary range")
    print("4: Add a new employee")
    print("5: Delete employee")
    print("6: Update the info about employee")
    print("7: Export data into json")
    print("8: Export data into csv")
    print("9: End of work")
    position = int(input("choose the action: "))
    
    while position < 0 or position > 9:
        print("Error. Choose among the options")
        position = int(input("choose the option: "))
    return position