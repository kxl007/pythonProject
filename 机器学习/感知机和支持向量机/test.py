import numpy as np

from cvxopt import matrix,solvers
y=[1,1,1,1]
y=np.array(y)
s=[[1,2,3]]
y.reshape(1,-1)  #①若是a.reshape(x, -1)则是将矩阵a变成行数为x，列数不规定的矩阵，具体列数按照总元素个数除行数，均分得到。
                 #②若是a.reshape(-1, x)则是将矩阵a变成列数为x，行数不规定的矩阵，具体行数按照总元素个数除列数，均分得到。
print(y)

x=np.inner(s,s) #定义内积运算
print(np.eye(40)) #构造单位矩阵
print(x)
print(np.vstack((np.eye(40)*-1, np.eye(40))))

print(np.ones(40)) #构造全为1的向量

print(np.zeros(10)) ##构造全为0的向量

h = np.vstack((np.zeros(5).reshape(-1,1 ), np.ones(5).reshape(-1, 1) * 3))


print(h)
a = np.array([[1, 2], [2, 3]])  #a.ravel() #ravel()方法将数组维度拉成一维数组
a=np.ravel(a)
print(a)

s1=np.array([[1,2],[3,4]])

print(s1.shape)


s1=np.array([1,2,3])
print('xxxxxxxxxx')
print(np.sum(s1))


g=matrix(np.vstack((np.eye(5)*-1, np.eye(5))))
print(g)



y=[[[1.]], [[1.]], [[1.]], [[1.]], [[1.]], [[1.]], [[1.]],[[1.]], [[1.]], [[1.]], [[-1.]], [[-1.]], [[-1.]], [[-1.]], [[-1.]],[[-1.]], [[1.]], [[-1.]], [[-1.]], [[-1.]]]


