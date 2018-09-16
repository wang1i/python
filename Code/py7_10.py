import time as t


class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second

    def setTime(self, elapsedTime):
        self.__second = elapsedTime % 60
        minutes = elapsedTime // 60
        self.__minute = minutes % 60
        self.__hour = (minutes // 60) % 24


t = Time(12, 41, 6)
print("当前时间是", t.getHour(), ":", t.getMinute(), ":", t.getSecond())
elapsedTime = eval(input("输入当前流逝时间："))
t.setTime(elapsedTime)
print("流逝时间转换成时钟制即为：", t.getHour(), ":", t.getMinute(), ":", t.getSecond())