from tkinter import *
from tkinter import ttk
import copy
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot
import csv
import math
import copy
from dataclasses import dataclass

def setDOF():
  dof=int(variable1.get())
  return ''
class point:
    xPos:float
    yPos:float
    zPos:float
    def __init__(self,x,y,z):
        self.xPos=x
        self.yPos=y
        self.zPos=z

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
    ax.plot(xPoints, yPoints, zPoints, color = 'b',linewidth=2)
    matplotlib.pyplot.show()


def calc(*dhParams):
    dof=int(len(dhParams)/4)
    dhTable= np.reshape(dhParams,(dof,4))
    origin= point(0,0,0)
    newPoint= point(0,0,0)
    plotPoints=[]
    plotPoints.append(origin)
    a= np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    for i in range(0,dof):

        j=0

        while j<3:
            if j==0:
                a=np.dot(a,zRotation(math.radians(dhTable[i][j])))
                j=j+1

            if j==1:
                a=np.dot(a,zTranslation(dhTable[i][j]))
                j=j+1

            if j==2:
                a=np.dot(a  ,xTranslation(dhTable[i][j]))
                j=j+1

            if j==3:
                a=np.dot(a,xRotation(math.radians(dhTable[i][j])))
                j=j+1

            newPoint.xPos= a[0][3]
            newPoint.yPos= a[1][3]
            newPoint.zPos= a[2][3]
            appendPoint= copy.deepcopy(newPoint)
            plotPoints.append(appendPoint)



    drawGraph(*plotPoints)

def inputDH(dof):
    dhParams=[]
    rows = []
    Label(text="\u03F4").grid(row=1,column=0)
    Label(text="z").grid(row=1,column=1)
    Label(text="x").grid(row=1,column=2)
    Label(text="\u03B1").grid(row=1,column=3)
    for i in range(dof):
        cols = []
        for j in range(4):
            e = Entry(relief=RIDGE)
            e.grid(row=i+2, column=j, sticky=NSEW)
            e.insert(END, '%d' % (0))
            cols.append(e)
        rows.append(cols)

    def onPress():
        for row in rows:
            for col in row:
                dhParams.append(int(copy.deepcopy(col.get())))
        calc(*dhParams)

    Button(text='Plot', command=onPress).grid()
    root1.mainloop()

root1=Tk()
variable1=StringVar()
def setDOF():
  dof=int(copy.deepcopy(variable1.get()))
  inputDH(dof)
ttk.Entry(width=7, textvariable=variable1).grid(column=1, row=0)
ttk.Label(text="Enter DOF:").grid(column=0, row=0)
ttk.Button(text="Set", command=setDOF).grid(column=2, row=0)
root1.mainloop()
