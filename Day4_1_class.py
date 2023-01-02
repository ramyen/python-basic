
class eat():
    def eat(self, something):
        print("Eating " + something)


class person():
    def __init__(self, name:str, id:int, hp:int) -> None:
        self.name = name
        self.id = id
        self.hp = hp
        self.eat = eat()
        print(f"person 생성: 이름({self.name}) / id({self.id})")



    def sleep(self, hour:int):
        print("{} Sleeping for {} hour".format(self.name, str(hour)))

    def damaged(self, attackValue:int):
        print(self.name + " Damaged " + str(attackValue))
        self.hp -= attackValue
        if self.hp <= 0:
            print(self.name + " Dead ")
    

class attackable():
    def __init__(self, attackValue:int) -> None:
        self.attackValue = attackValue

    def attack(self, toPerson:person):
        toPerson.damaged(self.attackValue)


class solider(person, attackable):
    def __init__(self, name:str, id:int, hp:int, attackValue:int) -> None:
        person.__init__(self, name, id, hp)
        attackable.__init__(self, attackValue)




baseUnit0 = person("백경진", 820211, 100)
print(baseUnit0)


baseUnit1 = solider("송영근", 20110106, 200, 30)
print(baseUnit1)

baseUnit1.attack(baseUnit0)

