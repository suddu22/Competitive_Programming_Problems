import random
from pythonds.basic.queue import Queue


class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.time_left = 0
        self.current_task = None

    def busy(self):
        if self.current_task is None:
            return False
        return True

    def startNext(self, new_task):
        self.current_task = new_task
        self.time_left = new_task.getPages() * 60 / self.page_rate

    def tick(self):
        if self.busy():
            self.time_left = self.time_left - 1
            if self.time_left <= 0:
                self.time_left = 0
                self.current_task = None


class Task:
    def __init__(self, time, pages_number):
        self.time_stamp = time
        self.pages = random.randrange(1, pages_number + 1)

    def getStamp(self):
        return self.time_stamp

    def getPages(self):
        return self.pages

    def waitingTime(self, current_time):
        return current_time - self.time_stamp


def newPrintTask(students_number):
    st = (students_number * 2.0)
    se = 1 * 60 * 60
    rg = se / st
    ran = random.randrange(1, rg + 1)
    if ran == 180:
        return True
    return False


def simulation(num_seconds, page_rate):
    labPrinter = Printer(page_rate)
    printerQueue = Queue()
    waitingTime = []
    pages_number = 20
    students_number = 10

    for second in range(num_seconds):
        if newPrintTask(students_number):
            task = Task(second, pages_number)
            printerQueue.enqueue(task)

        if (not labPrinter.busy()) and (not printerQueue.isEmpty()):
            nextTask = printerQueue.dequeue()
            waitingTime.append(nextTask.waitingTime(second))
            labPrinter.startNext(nextTask)

        labPrinter.tick()
    averageWait = sum(waitingTime) / len(waitingTime)

    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printerQueue.size()))


for i in range(10):
    simulation(3600, 5)


###############


def hotPotato(namelist, num):
    q = Queue()
    for name in namelist:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()


print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
