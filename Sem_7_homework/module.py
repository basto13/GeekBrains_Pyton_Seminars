# read database from "txt" file
def readData():
    db_list = []
    db_file = open("data.txt", "r", encoding='utf-8')
    
    lines = db_file.readlines()
    for line in lines:
        if line != "":
            db_list.append(line.replace("\n", "").split(" "))

    db_file.close()
    return db_list

# rewrite database function
def rewriteData(data):
    db_file = open("data.txt", "w", encoding='utf-8')
    for line in data:
        db_file.write(" ".join(line)+"\n")

# add new data function
def addData(data):
    last_name = input("add last name: ").strip()
    first_name = input("add first name: ").strip()
    father_name = input("add father name: ").strip()
    phone_number = input("add phone number: ").strip()

    line = (last_name, first_name, father_name, phone_number)
    data.append(line)
    rewriteData(data)

# find contact by first or last name
def findContact(data):
    user_search = input("Insert first or last name for searching: ")
    for line in data:
        if line[0] == user_search or line[1] == user_search:
            print("contact found: last name: ", line[0], "first name: ", line[1], "father name: ", line[2], "phone number: ", line[3])
        else:
            print("There is no such contact.")

