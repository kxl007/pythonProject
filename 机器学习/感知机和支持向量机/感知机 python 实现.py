import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from sklearn.linear_model import Perceptron



#获取训练数据集
df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

y=df.iloc[0:100,4].values
y=np.where(y=='Iris-setosa',1,-1)
x=df.iloc[0:100,[0,2]].values #训练数据集
x2=x[49]
x1=np.argwhere(x[0:50,0]>=6) # 获取满足条件的数组索引
x[49]=[5,1]
#print(x[1])
#print(x2)
#np.delete(x,x1)
#np.delete(y,x1)




#绘制散点图
plt.figure()
plt.scatter(x[0:50,0],x[0:50,1],color='red',marker='o',label='setosa')
plt.scatter(x[50:100,0],x[50:100,1],color='blue',marker='x',label='versicolor')
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12) #中文标题乱码问题
plt.title('鸢尾花散点图', fontproperties=font_set)
plt.xlabel("花瓣长度", fontproperties=font_set)
plt.ylabel("萼片长度", fontproperties=font_set)
plt.legend(loc='upper left')

#训练数据
# 定义感知机

clf = Perceptron(eta0=0.0001, max_iter=10)
# 使用训练数据进行训练
clf.fit(x, y)
# 得到训练结果，权重矩阵
print(clf.coef_)
# 输出为：[[-0.38478876,4.41537463]]

# 超平面的截距，此处输出为：[0.]

print(clf.n_iter_)
print(clf.intercept_)

x2=np.linspace(3,7,50)
x3=(-clf.coef_[0][0] / clf.coef_[0][1])*x2-clf.intercept_
print(x2.shape)
print(len(x3))
plt.plot(x2,x3,color='green')
plt.show()

