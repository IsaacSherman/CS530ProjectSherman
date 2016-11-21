import threading
import time
import numpy

class ArithmeticRunThread(threading.Thread):
    def __init__(self, threadID, name, numberOfSteps):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.steps = numberOfSteps

    def run(self):
        self.execute()

    def execute(self):
        num = []
        for i in range(0, 8):
            num.append(numpy.random.random())

        for i in range(0, self.steps):
            num[0] = num[3] * num[0] + num[1] * num[0]
            num[2] = num[5] * num[2] + num[2] * num[7]
            num[4] = num[7] * num[4] + num[3] * num[6]
            num[6] = num[1] * num[6] + num[4] * num[5]
            num[1] = num[2] * num[1] + num[5] * num[4]
            num[3] = num[4] * num[3] + num[6] * num[3]
            num[5] = num[6] * num[5] + num[7] * num[2]
            num[7] = num[0] * num[7] + num[0] * num[1]


numSteps = 10000000
mainThread = threading.main_thread()
thread1 = ArithmeticRunThread(1, "Thread-1", numSteps)
thread2 = ArithmeticRunThread(2, "Thread-2", numSteps)
thread3 = ArithmeticRunThread(3, "Thread-3", numSteps)
thread4 = ArithmeticRunThread(4, "Thread-4", numSteps)
thread5 = ArithmeticRunThread(5, "Thread-5", numSteps)
thread6 = ArithmeticRunThread(6, "Thread-6", numSteps)
thread7 = ArithmeticRunThread(7, "Thread-7", numSteps)
thread8 = ArithmeticRunThread(8, "Thread-8", numSteps)


count = 0
processTime = time.time()
wallTime = currentTime = time.clock()
while currentTime - wallTime < 600:
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    currentTime = time.clock()
    count += 1
    #print("Ending iteration " + str(count) + " after " + str(currentTime - wallTime) + " seconds")
    thread1 = ArithmeticRunThread(1, "Thread-1", numSteps)
    thread2 = ArithmeticRunThread(2, "Thread-2", numSteps)
    thread3 = ArithmeticRunThread(3, "Thread-3", numSteps)
    thread4 = ArithmeticRunThread(4, "Thread-4", numSteps)
    thread5 = ArithmeticRunThread(5, "Thread-5", numSteps)
    thread6 = ArithmeticRunThread(6, "Thread-6", numSteps)
    thread7 = ArithmeticRunThread(7, "Thread-7", numSteps)
    thread8 = ArithmeticRunThread(8, "Thread-8", numSteps)

print("Completed " + str(count) + " iterations in " + str(currentTime - wallTime) + "seconds")