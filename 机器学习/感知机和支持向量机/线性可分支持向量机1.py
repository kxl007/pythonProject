import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from sklearn.linear_model import Perceptron #训练
from cvxopt import matrix,solvers

df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

y=df.iloc[0:100,4].values
y=np.where(y=='Iris-setosa',1,-1)
y=np.array(y)
x=df.iloc[0:100,[0,2]].values #训练数据集
x2=x[49]
x1=np.argwhere(x[0:50,0]>=6) # 获取满足条件的数组索引
x[49]=[5,1]


plt.figure()
plt.scatter(x[0:50,0],x[0:50,1],color='red',marker='o',label='setosa')
plt.scatter(x[50:100,0],x[50:100,1],color='blue',marker='x',label='versicolor')
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12) #中文标题乱码问题
plt.title('鸢尾花散点图', fontproperties=font_set)
plt.xlabel("花瓣长度", fontproperties=font_set)
plt.ylabel("萼片长度", fontproperties=font_set)
plt.legend(loc='upper left')



#定义x的内积

k = []
for i in range(x.shape[0]):
    k.append([])
    for j in range(x.shape[0]):
        k[i].append(np.inner(x[i], x[j]))

k=np.array(k)



#定义y的内积
l=np.inner(y,y)


#定义凸优化pq函数
p=matrix(l*k)             #定义二次项系数
q=matrix(np.ones(100)*-1)  #定义一次项系数


A=matrix(y.reshape(1,-1) )#定义等式约束
A = matrix(A, (1, 100), 'd')
b=matrix(0.)              #数据应为同类型


g=matrix(np.eye(100)*-1)    #定义不等式约束
h=matrix(np.zeros(100).reshape(-1, 1))


solution = solvers.qp(p, q, g, h, A, b)
#print(solution['x'])
#print(solution['primal objective'])

a=np.ravel(solution['x'])  #解
y=y.reshape(-1,1)

sv = []
for i in range(len(a)):
    if a[i] > 1e-6:
        sv.append(i)

a = [a[i] for i in sv]

x = [x[i] for i in sv]
y = [y[i] for i in sv]
print(a)
print(x)
print(y)
w_best=[0,0]
for i in range(len(a)):
    w_best += a[i] * y[i][0] * x[i]

#w的最优解

#w_best=np.sum(a.reshape(-1,1)*y*x,axis=0)   #转化为矩阵进行乘积
print(w_best)


#b的最优解
b=0
#b1=y[0]-np.sum(y * a.reshape(-1,1)* np.inner(x, x[0].T).reshape(-1,1))
#for j in range(x.shape[0]):
#   b_best += y[j] - np.sum(y * a.reshape(-1, 1) * np.inner(x, x[j].T).reshape(-1, 1))
#b_best=b_best/x.shape[0]

for j in range(len(a)):
    b += y[j][0] - np.dot(x[j] ,w_best)
b = b / len(a)
print(b)
#print(b1)






x2=np.linspace(4,7,50)
x3=-w_best[0] / w_best[1]*x2-b/w_best[1]

plt.plot(x2,x3,color='green')
plt.show()












