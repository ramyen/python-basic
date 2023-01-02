
from datetime import datetime, timedelta
from time import sleep

# 변수, 함수 들을 포함하는 녀석

# 전원 On : 팬이 돌아간다, 기본값 제일 약한 단계로
# 바람 단계를 조절할 수 있다.
# 꺼지는 시간을 정할 수 있다. 단위 ex) 분, 시간.
# 회전 On / Off 할수 있다. 좌우 특정 각도까지만 회전이 가능하고, 왕복한다.
# 취침모드, 자연풍 등 옵션이 있다.
class fan():
    def __init__(self) -> None:
        self.power = 0
        self.timeleft = -1
        self.angle = 0

    def setPower(self, power:int):
        self.power = power
    
    def setOnOff(self, on:bool):
        if on:
            self.setPower(1)
            print("Fan turned on")
        else:
            self.setPower(0)
            print("Fan turned off")

    def setTimer(self, min:int):
        self.timeleft = min * 60 * 1000


    def run(self, deltaTime:timedelta):
        
        if self.timeleft > 0:
            sec = deltaTime.seconds
            microsec = deltaTime.microseconds
            totalMilisec = sec * 1000
            totalMilisec += round(microsec / 1000) 
            self.timeleft -= totalMilisec
            print(f"Time Left : {self.timeleft}")
        if self.timeleft < 0:
            self.setOnOff(False)

# 1초 = 1000 ms

# 1분 = 60초



testFan = fan()
testFan.setOnOff(True)
testFan.setTimer(1)

nowTime = datetime.now()
print(nowTime)

while True:
    sleep(1)
    deltaTime = datetime.now() - nowTime
    testFan.run(deltaTime)
    nowTime = datetime.now()





