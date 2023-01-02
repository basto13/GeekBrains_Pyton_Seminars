def user_ui():
    print("contact book")
    print("1: Add a new contact")
    print("2: Find a contact")
    print("3: Import data")
    print("4: Export whole database")
    print("5: Print the whole contact book")
    print("0: End of work")
    position = int(input("choose the option: "))
    
    while position < 0 or position > 5:
        print("Error. Choose among the options")
        position = int(input("choose the option: "))
    return position