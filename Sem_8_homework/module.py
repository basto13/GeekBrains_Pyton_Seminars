
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

def rewriteData(data):
    db_file = open("data.txt", "w", encoding='utf-8')
    print("data in rewrite: ", data)
    for line in data:
        lineToAdd = []
        lineToAdd.append(str(line["id"]))
        lineToAdd.append(line["last_name"])
        lineToAdd.append(line["first_name"])
        lineToAdd.append(line["position"]) 
        lineToAdd.append(line["phone_number"])
        lineToAdd.append(str(line["salary"])) 
        db_file.write(" ".join(lineToAdd)+"\n")
    return data

# search employee by name or position:
def findEmployee(data):
    search = str(input("Input last name or position for search: "))
    for person in data:
        if search == person["last_name"] or search == person["position"]:
            print(person)
            return person

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
def addNewEmployee(data):
    newEmp = {}
    newEmp["id"] = (data[-1]["id"] + 1)
    newEmp["last_name"] = input("add last name: ").strip()
    newEmp["first_name"] = input("add first name: ").strip()
    newEmp["position"] = input("add position: ").strip()
    newEmp["phone_number"] = input("add phone number: ").strip()
    newEmp["salary"] = int(input("add salary: "))
    data.append(newEmp)
    rewriteData(data)

def deleteEmployee(data):
    person = findEmployee(data)
    approval = str(input("Write yes if you want to delete the employee: "))
    if approval == "yes":
        data.remove(person)
        print("Employee is deleted")
        rewriteData(data)
    return data


   