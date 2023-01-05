
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

# find employee by name:
def findEmployee(data):
    print(data)
    # print(data[0]["position"])