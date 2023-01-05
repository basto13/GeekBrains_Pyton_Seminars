
# read database from "txt" file
def readData():
    employees = []
    db_file = open("data.txt", "r", encoding='utf-8')
    lines = db_file.readlines()
    for line in lines:
        tempList = line.replace("\n", "").split(" ")
        temp ={}
        temp["id"] = int(tempList[0])
        temp["last_name"] = str(tempList[1])
        temp["first_name"] = str(tempList[2])
        temp["position"] = str(tempList[3])
        temp["phone_number"] = str(tempList[4])
        temp["salary"] = int(tempList[5])
        employees.append(temp)  
    db_file.close()
    print(employees)
    return employees

# search employee by name or position:
def findEmployee(data):
    search = str(input("Input last name or position for search: "))
    for person in data:
        if search == person["last_name"] or search == person["position"]:
            print(person)

# select by salary range function
def salarySelection(data):
    search = int(input("insert the approximate salary to search: "))
    list = []
    minDist = 1000000
    for person in data:
        tempDist = abs(search - person["salary"])
        if minDist > tempDist:
            minDist = tempDist
    for person in data:
        if minDist >= (abs(search - person["salary"])):
            list.append(person)
    print(list)
    return list

# add new person
def addNewEmployee():

    print(list)


   