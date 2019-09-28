from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot
import csv
import math
import copy
from dataclasses import dataclass

class point:
    xPos:float
    yPos:float
    zPos:float
    def __init__(self,x,y,z):
        self.xPos=x
        self.yPos=y
        self.zPos=z

##WORKING#########################################################
def zTranslation(transZ):
    zTransMatrix= np.array([[1,0,0,0],[0,1,0,0],[0,0,1,transZ],[0,0,0,1]])
    return zTransMatrix

def xTranslation(transX):
    xTransMatrix= np.array([[1,0,0,transX],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    return xTransMatrix

def zRotation(rotZ):
    zRotMatrix= np.array([[round(np.cos(rotZ),2),round(-np.sin(rotZ),2),0,0],[round(np.sin(rotZ),2),round(np.cos(rotZ),2),0,0],[0,0,1,0],[0,0,0,1]])
    return zRotMatrix

def xRotation(rotX):
    xRotMatrix= np.array([[1,0,0,0],[0,round(np.cos(rotX),2),round(-np.sin(rotX),2),0],[0,round(np.sin(rotX),2),round(np.cos(rotX),2),0],[0,0,0,1]])
    return xRotMatrix

def drawGraph(*plotPoints):
    fig = matplotlib.pyplot.figure()
    ax  = fig.add_subplot(111, projection = '3d')


    xPoints= []
    yPoints= []
    zPoints= []
    for i in plotPoints:
        xPoints.append(i.xPos)
        yPoints.append(i.yPos)
        zPoints.append(i.zPos)
    print(xPoints,yPoints,zPoints)
    ax.scatter(xPoints,yPoints,zPoints,color='r',marker='x')
    ax.plot(xPoints, yPoints, zPoints, color = 'b')
    matplotlib.pyplot.show()
dhTable= np.array([[0,10,0,0],[0,0,20,0],
                   [0,10,0,0],[0,0,20,0]])
origin= point(0,0,0)
newPoint= point(0,0,0)
plotPoints=[]
plotPoints.append(origin)
a= np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
for i in range(0,4):

    j=0

    while j<3:
        if j==0:

            print(zRotation(math.radians(dhTable[i][j])))
            a=np.dot(a,zRotation(math.radians(dhTable[i][j])))
            j=j+1

        if j==1:
            print(zTranslation(dhTable[i][j]))
            a=np.dot(a,zTranslation(dhTable[i][j]))
            j=j+1

        if j==2:
            print(xTranslation(dhTable[i][j]))
            a=np.dot(a  ,xTranslation(dhTable[i][j]))
            j=j+1

        if j==3:
            print(xRotation(math.radians(dhTable[i][j])))
            a=np.dot(a,xRotation(math.radians(dhTable[i][j])))
            j=j+1

        newPoint.xPos= a[0][3]
        newPoint.yPos= a[1][3]
        newPoint.zPos= a[2][3]
        appendPoint= copy.deepcopy(newPoint)
        plotPoints.append(appendPoint)
        print("NEWPOINT", newPoint.xPos,newPoint.yPos,newPoint.zPos,"NEWPOINT")


drawGraph(*plotPoints)
