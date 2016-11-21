import threading
import time
import numpy

exitFlag = 0


class MemoryRunThread(threading.Thread):
    def __init__(self, threadID, name, A, B):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.A = A
        self.B = B

    def run(self):
        #print("Starting " + self.name)
        self.execute()
        #print(self.res)
        #print("Exiting " + self.name)

    def execute(self):
        self.res = self.A * self.B


class ArithmeticRunThread(threading.Thread):
    def __init__(self, threadID, name, numberOfSteps):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.steps = numberOfSteps

    def run(self):
        self.execute()

    def execute(self):
        a = numpy.random.random()
        b = numpy.random.random()
        for i in range(0, self.steps):
            a = a * b



# Create new threads
dim = 4000000
sqrtDim = 2000

matrixA = numpy.random.random_sample(dim).reshape(sqrtDim, sqrtDim)
matrixB = numpy.random.random_sample(dim).reshape(sqrtDim, sqrtDim)
matrixC = numpy.random.random_sample(dim).reshape(sqrtDim, sqrtDim)
matrixD = numpy.random.random_sample(dim).reshape(sqrtDim, sqrtDim)

mainThread = threading.main_thread()
thread1 = MemoryRunThread(1, "Thread-1", matrixA, matrixB)
thread2 = MemoryRunThread(2, "Thread-2", matrixB, matrixC)
thread3 = MemoryRunThread(3, "Thread-3", matrixC, matrixD)
thread4 = MemoryRunThread(4, "Thread-4", matrixD, matrixA)


count = 0
processTime = time.time()
wallTime = currentTime = time.clock()
while currentTime - wallTime < 600:
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    currentTime = time.clock()
    count += 1
    #print("Ending iteration " + str(count) + " after " + str(currentTime - wallTime) + " seconds")
    thread1 = MemoryRunThread(1, "Thread-1", matrixA, matrixB)
    thread2 = MemoryRunThread(2, "Thread-2", matrixB, matrixC)
    thread3 = MemoryRunThread(3, "Thread-3", matrixC, matrixD)
    thread4 = MemoryRunThread(4, "Thread-4", matrixD, matrixA)

print("Completed " + str(count) + " iterations in " + str(currentTime - wallTime) + "seconds")