import threading
import time
import random

exitFlag = 0


class MemoryRunThread(threading.Thread):
    def __init__(self, threadID, name, A, B):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.A = A
        self.B = B

    def run(self):
        # print("Starting " + self.name)
        self.execute()
        # print(self.res)
        # print("Exiting " + self.name)

    def execute(self):
        result = [[0 for i in range(len(self.A))] for i in range(len(self.B[0]))]
        for i in range(0, len(self.A)):
            for j in range(0, len(self.B[0])):
                res = 0
                for k in range(0, len(self.B)):
                    res += self.A[i][k] * self.B[k][j]
                result[i][j] = res
        del result


# Create new threads
dim = 160000
sqrtDim = 400
random.seed = 13

matrixA = [[random.random() for a in range(sqrtDim)] for a in range(sqrtDim)]
matrixB = [[random.random() for a in range(sqrtDim)] for a in range(sqrtDim)]
matrixC = [[random.random() for a in range(sqrtDim)] for a in range(sqrtDim)]
matrixD = [[random.random() for a in range(sqrtDim)] for a in range(sqrtDim)]

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
    thread1 = MemoryRunThread(1, "Thread-1", matrixA, matrixB)
    thread2 = MemoryRunThread(2, "Thread-2", matrixB, matrixC)
    thread3 = MemoryRunThread(3, "Thread-3", matrixC, matrixD)
    thread4 = MemoryRunThread(4, "Thread-4", matrixD, matrixA)

print("Completed " + str(count) + " iterations in " + str(currentTime - wallTime) +
      " seconds, \n with " + str(sqrtDim ** 3 * 4) + " floating point operations")
