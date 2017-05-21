#-------------------------------------------------------------------------------
# Name:         Plotter
# Purpose:      Plotter script for the singlecore and multicore scripts
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt

x=[]
y=[]
x1=[]
y1=[]

with open('singlecore.txt', 'r')as textFile:
        line=textFile.read()[:-1].split('|')
        for pair in line:
            val=pair.split(',')
            x.append(val[0])
            y.append(val[1])

with open('multicore.txt', 'r')as textFile:
        line=textFile.read()[:-1].split('|')
        for pair in line:
            val=pair.split(',')
            x1.append(val[0])
            y1.append(val[1])

fig=plt.figure()
graph=fig.add_subplot(1,1,1)
graph.plot(x, y, 'red')
graph.plot(x1, y1, 'blue')
graph.set_title('A Graph Of N Against Time')
graph.set_xlabel('Value of N(000s)')
graph.set_ylabel('Time in Seconds')
plt.show()
