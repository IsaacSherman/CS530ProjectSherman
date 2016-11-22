import threading
import time
import numpy



numpy.random.seed(13)

def FisherYatesShuffle(list):
    for i in range(len(list) - 1, 0, -1):
        fyj = numpy.random.random_integers(0, i)
        list[i], list[fyj] = list[fyj], list[i]
    return list



indices = []
indexSize = 32
for j in range(0, 4):
    indices.append(FisherYatesShuffle(list(range(0, indexSize))))


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

        for i in range(0, indexSize):
            num.append(numpy.random.random())

        for i in range(0, self.steps):
            for j in range(0, indexSize):
                num[j] = num[indices[0][j]]*num[indices[1][j]] + num[indices[2][j]] * num[indices[3][j]] + \
                    num[indices[0][j]] * num[indices[2][j]] + num[indices[1][j]] * num[indices[3][j]] + \
                    num[indices[0][j]]



numSteps = 1000000
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
print("The total number of flops for this run was " + str(numSteps * 8 * indexSize * 8))