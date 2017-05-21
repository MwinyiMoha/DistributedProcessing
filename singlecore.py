#-------------------------------------------------------------------------------
# Name:         SingleCore
# Purpose:      Demonstrate singlecore based programming in python
#-------------------------------------------------------------------------------
import random
import time
import sys

random.seed()

def genValues(size):
    randomList=[]
    for i in range(size):
        randomList.append(random.randint(0,10))
    return randomList

def sumList(inList):
    finalSum=sum(inList)
    return finalSum

def writeToFile(Value, Time):
    with open('singlecore.txt', 'a') as textFile:
        line='{},{} |'.format(Value, Time)
        textFile.write(line)

if __name__=='__main__':
    if len(sys.argv)==2 and sys.argv[1].isdigit():
        N=int(sys.argv[1])
        startTime=time.time()

        myList=genValues(N)
        finalSum=sumList(myList)

        endTime=time.time()
        runTime=endTime-startTime
        writeToFile(N/1000, runTime)

        print('Script Completed')
        print('Time Taken: {} seconds'.format(str(runTime)))
        print('Final sum: {}'.format(str(finalSum)))
    else:
        raise ValueError('Provide N')






