import time


class StopWatch:
    def __init__(self):
        self.__startTime = time.time()

    def setStartTime(self):
        self.__startTime = time.time()

    def setEndTime(self):
        self.__endTime = time.time()

    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime

    def getElapsedTime(self):
        return (self.__endTime - self.__startTime) * 1000

x = 0
watch = StopWatch()
for i in range(1000000):
    x += 1
watch.setEndTime()
print("流逝时间",watch.getElapsedTime())