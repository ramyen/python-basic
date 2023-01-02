

# templist = ["dk", "jh", "asdasd", 9]

# for element in templist:
#     if type(element) == str:
#         print(element)


class sampleClass():
    def __init__(self, name) -> None:
        self.name = name
        self.age = 0
        self.address = ""
        self.div = ""




tempDict = {"123":sampleClass("태은"), "456":sampleClass("경진"), "789":sampleClass("조아")}

for element in tempDict:
    tempValue = tempDict[element]
    tempDict[element] = sampleClass("올리")
    print(f"{element} : {hash(element)}")
    
