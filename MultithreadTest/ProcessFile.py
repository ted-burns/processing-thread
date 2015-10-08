__author__ = 'ltdwkst1'
import math
import threading
import time

def transform(number):
    number *= 5
    number /= 3
    number += 2
    number /= 3.1415926
    return math.floor(number)

class processingThread(threading.Thread):
    def __init__(self, inQueue, outQueue, method):
        threading.Thread.__init__(self)
        self.stop = False
        self.inQueue = inQueue
        self.outQueue = outQueue
        self.method = method
    def run(self):
        inLock = self.inQueue.Lock()
        outLock = self.outQueue.Lock()
        while not(self.stop):
            with inLock:
                num = self.inQueue.get()
            num = self.method(num)
            with outLock:
                self.outQueue.put(num)

class fileHandleThread(threading.Thread):
    def __init__(self, file):
        threading.Thread.__init__(self)
        self.file = file
    def read(self, outputStructure):
        for line in self.file:
            outputStructure.push(line)

with open('data.txt', 'wr') as fileLoaded:
    fileHandleThread.run()




