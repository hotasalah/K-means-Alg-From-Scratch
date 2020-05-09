import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('E:\Software\Coursera-ML\IV. Linear Regression with Multiple Variables (Week 2)\ex1\ex1data1.txt' , delimiter = ',')

def plotData(arr, xlabel, ylabel):
    plt.scatter(arr[:,0], arr[:,1], s=15 , c='black' , marker='o')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xlim(arr[:,0].min() , arr[:,0].max())
    plt.ylim(arr[:,1].min() , arr[:,1].max())
plotData(data ,'x1','x2')

def k_means(k,x):
    k1 = (5,8)
    k2 = (7,2)
    c10 = []
    c11 = []
    c20 = []
    c21 = []
    c1 = []
    c2 = []
    m = len(x)
    for j in range(10):
        for i in range(m):
            dis1 = np.sqrt( (x[i][0]-k1[0]) * (x[i][0]-k1[0]) + (x[i][1]-k1[1]) * (x[i][1]-k1[1]) )
            dis2 = np.sqrt( (x[i][0]-k2[0]) * (x[i][0]-k2[0]) + (x[i][1]-k2[1]) * (x[i][1]-k2[1]) )
            if (dis1 > dis2):
                c1.append(x[i])
                plt.scatter(x[i][0], x[i][1], s=15 , c='darkblue' , marker='o')
            else:
                c2.append(x[i])
                plt.scatter(x[i][0], x[i][1], s=15 , c='red' , marker='o')
        for z in range(len(c1)):
            c10.append(c1[z][0])
        for q in range(len(c1)):
            c11.append(c1[q][0])
        for r in range(len(c2)):
            c20.append(c2[r][0])
        for t in range(len(c2)):
            c21.append(c2[t][0])
        k1 = ( np.average(c10), np.average(c11) )
        k2 = ( np.average(c20), np.average(c21) )
        
k_means(2,data)








