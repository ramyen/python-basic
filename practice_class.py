
# from time import sleep
# class motor():
#     __manufactor = "Samsung" 
#     def __init__(self) -> None:
#         self.power = 0
#         print("Create a motor")

#     def setPower(self, power:int):
#         self.power = power

#     def round(self):
#         if self.power > 0:
#             print(f"[motor] Round with power({self.power})")

#     def getBrandName() -> str :
#         return motor.__manufactor

# class wing():
#     def __init__(self) -> None:
#         print("Create a wing")

# # 전원을 키고 끌 수 있다. 디폴트 파워 1
# # 파워를 조절할 수 있다.
# # 파워에 따라 모터의 회전 속도를 다르게 할 수 있다.
# class fan():
#     def __init__(self) -> None:
#         self.motor = motor()
#         self.wing = wing()
#         self.power = 0
#         print("Create a fan")

#     def setTurn(self, on:bool):
#         self.turnOn = on

#         if self.turnOn:
#             self.setPower(1)

#     def update(self):
#         self.motor.round()
    
#     def setPower(self, power:int):
#         self.power = power
#         self.motor.setPower(self.power)

# print(motor.getBrandName())
# tempFan = fan()
# tempFan.setTurn(True)
# while True:
#     tempFan.update()


# 타워 디펜스
# 터렛, 스나이퍼, 화염방사기, 
# 농장 

class baseObject():
    def __init__(self, id:int, name:str) -> None:
        self.id = id
        self.name = name



class updatable():
    def __init__(self) -> None:
        pass

    def update(self):
        pass

class renderable():
    def __init__(self) -> None:
        pass

    def render(self):
        pass

class attackable():
    def __init__(self) -> None:
        pass

    def attack(self):
        pass

class landable():
    def __init__(self) -> None:
        self.pos = (0, 0)

    def land(self, pos:tuple[int, int]):
        self.pos = pos

class building(baseObject, updatable, renderable, landable):
    def __init__(self, id: int, name: str, cost:int) -> None:
        baseObject.__init__(self, id, name)
        updatable.__init__(self)
        renderable.__init__(self)
        landable.__init__(self)
        self.cost = cost

class turret(building, attackable):
    def __init__(self, id: int, name: str, cost: int) -> None:
        building.__init__(self, id, name, cost)
        attackable.__init__(self)


class movable():
    def __init__(self, speed:int, pos:tuple(int, int)) -> None:
        self.moveSpeed = speed
        self.direction = (0,0)
        self.pos = pos

    def move(self):
        pass

    def setDirection(self, dir):
        self.direction = dir

class enemy(baseObject, updatable, renderable, movable, attackable):
    def __init__(self, id: int, name: str, speed:int) -> None:
        baseObject.__init__(self, id, name)
        updatable.__init__(self)
        renderable.__init__(self)
        movable.__init__(self, speed, (0,0))
        attackable.__init__(self)

    def update(self):
        movable.move(self)
        return super().update()

turret0 = turret(0, "turret0", 1000)
turret1 = turret(1, "turret1", 1000)

enemy0 = enemy(2, "enemy0", 10)

turret0.land((3,4))
turret1.land((3,5))


while True:
    turret0.update()
    turret1.update()
    enemy0.update()

    turret0.render()
    turret1.render()
    enemy0.render()



        