import numpy as np
from numpy import linalg
from cvxopt import solvers,matrix

import pylab as pl
import matplotlib.pyplot as plt

class soft_Margin(object):
    def __init__(self,C=None):
        self.fig=plt.figure()
        self.C = C
        if self.C is not None:
            self.C = float(self.C)


    ####################################



    ####################################

    # 基于cvxopt库定义线性支持向量机的训练过程：

    ####################################
    def train(self,x_train, y_train):
        # 定义x的内积
        nsample, n_features = x_train.shape
        k = []
        for i in range(nsample):
            k.append([])
            for j in range(nsample):
                k[i].append(np.dot(x_train[i], x_train[j]))
        # 定义二次项系数矩阵  numpy.outer(a, b) 用来求外积的
        P = matrix(np.outer(y_train, y_train) * k)
        # 定义一次项系数矩阵
        q = matrix(np.ones(nsample) * -1)
        # 定义约束等式矩阵
        A = matrix(np.array(y_train),(1, nsample))
        print(A.size)
        b = matrix(0.)
        # 定义约束不等式
        if self.C is None:
            G = matrix(np.eye(nsample) * -1)
            h = matrix(np.zeros(nsample))
        else:
            G = matrix(np.vstack((np.eye(nsample) * -1, np.eye(nsample))))
            h = matrix(np.hstack((np.zeros(nsample), np.ones(nsample) * self.C)))


        solution =solvers.qp(P,q,G,h,A,b)
        # 拉格朗日乘子
        a = np.ravel(solution['x'])
        # 去除接近零的拉格朗日因子################3
        # Support vectors have non zero lagrange multipliers
        sv = []
        for i in range(len(a)):
            if a[i] > 1e-5:
                sv.append(i)
        self.a = [a[i] for i in sv]
        self.sv_x = [x_train[i] for i in sv]
        self.sv_y = [y_train[i] for i in sv]
        # 求w
        self.w_best = np.zeros(n_features)
        for i in range(len(self.a)):
            self.w_best += self.a[i] * self.sv_y[i] * self.sv_x[i]
        # 求b
        self.b = 0
        for j in range(len(self.a)):
            b += self.sv_y[j] - np.dot(self.sv_x[j] ,self.w_best)
        self.b = b / len(self.a)
        print(self.b)

    #预测数据
    def predict(self,x):
        if self.w_best is not None:
            return np.sign(np.dot(self.w_best,x)+self.b)


#，当你要导入某个模块，但又不想改模块的部分代码被直接执行，那就可以这一部分代码放在“if __name__=='__main__':”内部。
if __name__ == "__main__":
    ####################################
    # 生成示例数据
    def gen_non_lin_separable_data():
        mean_1 = [-1, 2]
        mean_2 = [1, -1]
        mean_3 = [4, -4]
        mean_4 = [-4, 4]
        cov = [[1, 0.8], [0.8, 1]]
        # 生成正态分布的数据
        x1 = np.random.multivariate_normal(mean_1, cov, 50)
        # 矩阵叠加
        x1 = np.vstack((x1, np.random.multivariate_normal(mean_3, cov, 50)))
        # 生成全为1 的向量
        y1 = np.ones(len(x1))

        x2 = np.random.multivariate_normal(mean_2, cov, 50)
        # 矩阵叠加
        x2 = np.vstack((x2, np.random.multivariate_normal(mean_4, cov, 50)))
        # 生成全为1 的向量
        y2 = np.ones(len(x2)) * -1

        return x1, y1, x2, y2


    def gen_lin_separable_overlap_data():
        # generate training data in the 2-d case
        mean1 = np.array([0, 2])
        mean2 = np.array([2, 0])
        cov = np.array([[1.5, 1.0], [1.0, 1.5]])
        X1 = np.random.multivariate_normal(mean1, cov, 100)
        y1 = np.ones(len(X1))
        X2 = np.random.multivariate_normal(mean2, cov, 100)
        y2 = np.ones(len(X2)) * -1
        return X1, y1, X2, y2


    ####################################

    ####################################
    # 生成训练数据集
    def split_train(x1, y1, x2, y2):
        x1_train = x1[:90]
        y1_train = y1[:90]
        x2_train = x2[:90]
        y2_train = y2[:90]
        x_train = np.vstack((x1_train, x2_train))
        y_train = np.hstack((y1_train, y2_train))
        return x_train, y_train


    ####################################
    # 生成测试数据集
    def split_test(x1, y1, x2, y2):
        x1_test = x1[90:]
        y1_test = y1[90:]
        x2_test = x2[90:]
        y2_test = y2[90:]
        x_test = np.vstack((x1_test, x2_test))
        y_test = np.hstack((y1_test, y2_test))
        return x_test, y_test

    # 绘制数据

    def visualize(clf,x1,x2):
        x0=np.linspace(-4,6,50)
        y0=-1*(clf.w_best[0]*x0+clf.b)/clf.w_best[1]
        y=y0.T
        print(x0.shape)
        print(len(y))

        [plt.scatter(x[0], x[1], c='r', marker='o', label='1') for x in x1]
        [plt.scatter(x[0], x[1], c='g', marker='x', label='-1') for x in x2]
        #x,y 维度，数量要一致
        plt.plot(x0,y,'-.g')
        #调整坐标轴的范围
        plt.xlim(-4,6)
        plt.ylim(-4,6)
        pl.axis("tight")
        plt.show()
    #预测数据



    def test_soft():
        X1, y1, X2, y2 = gen_lin_separable_overlap_data()
        X_train, y_train = split_train(X1, y1, X2, y2)
        X_test, y_test = split_test(X1, y1, X2, y2)
        clf = soft_Margin(C=1000.1)
        clf.train(X_train, y_train)
        y_predict=[]
        for i in X_test:
             y_predict.append(clf.predict(i)[0][0])
        correct = np.sum(y_predict == y_test)

        print("%d out of %d predictions correct" % (correct, len(y_predict)))
        print('correct rate is  {:.2%}'.format(correct / len(y_predict)))

        visualize(clf,X1,X2)


test_soft()








