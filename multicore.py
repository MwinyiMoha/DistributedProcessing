#-------------------------------------------------------------------------------
# Name:         MultiCore
# Purpose:      Demonstrate multicore based programming in python
#-------------------------------------------------------------------------------
import random
import time
import sys
from multiprocessing import Pool

random.seed()

def sumList(inList):
    finalSum=sum(inList)
    return finalSum

def genValues(size):
    randomList=[]
    for i in range(size):
        randomList.append(random.randint(0,10))
    return randomList

def writeToFile(Value, Time):
    with open('multicore.txt', 'a') as textFile:
        line='{},{} |'.format(Value, Time)
        textFile.write(line)

def doWork(N):
    myList=genValues(N)
    mySum=sumList(myList)
    return mySum


if __name__=='__main__':
    if len(sys.argv)==2 and sys.argv[1].isdigit():
        N=int(sys.argv[1])
        start=time.time()

        pool=Pool(processes=4)
        result=pool.map(doWork, [N/4, N/4, N/4, N/4])
        finalResult=sumList(result)

        end=time.time()
        duration=end-start
        writeToFile(N/1000, duration)

        print('Script Completed')
        print('Time Taken: {} seconds'.format(str(duration)))
        print('Final sum: {}'.format(str(finalResult)))
    else:
        raise ValueError('Provide N')
