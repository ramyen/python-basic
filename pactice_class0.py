

# student class만들기
# member variables, functions 만들기

from datetime import datetime
from operator import truediv


class student():
    lastID = -1

    def __init__(self, data:dict[str, any]) -> None:
        student.lastID += 1
        self.dataDict = data

        self.dataDict["id"] = student.lastID

    def __del__(self):
        id = self.dataDict["id"]
        print(f"Destroy Student({id})")
        
    def getInfo(self) -> str:
        return str(self.dataDict)

    def getID(self) -> str:
        return self.dataDict["id"]

class studentManager():
    def __init__(self) -> None:
        self.studentDict = {}
        

    def addStudent(self, dataDict:dict[str, any]):

        newStudent = student(dataDict)
        id = newStudent.getID()

        if self.studentDict.get(id) == None:
            self.studentDict[id] = newStudent
        else:
            print("Can't add new student")
            del newStudent

    def getStudent(self, id:str):
        return self.studentDict.get(id)

    def getStudentAll(self) -> list[student]:
        return list(self.studentDict.values())


    def deleteStudent(self):
        pass

    def updateStudent(self, dataDict:dict[str, any]) -> bool:
        return True


    



testVal = str("hi")


# student0 = student("Joon Nam", 9, "None", datetime(2008,12,3))
# student1 = student("Noah", 0, "None", datetime(2017,9,19))

# student0 = student({"name":"Joon Nam", "grade": 9, "division":"None", "birth":datetime(2008,12,3)})
# student1 = student({"name":"Noah", "grade": 0, "birth":datetime(2018,9,19)})

manager = studentManager()
manager.addStudent({"name":"Joon Nam", "grade": 9, "division":"None", "birth":datetime(2008,12,3)})
manager.addStudent({"name":"Noah", "grade": 0, "birth":datetime(2018,9,19)})
manager.deleteStudent()

for element in manager.getStudentAll():
    print(element.getInfo())

# student0 = manager.getStudent(id = 0)
# student1 = manager.getStudent(id = 1)

# print(student0.getInfo())
# print(student1.getInfo())


# del student0
# del student1

print(student.lastID)
