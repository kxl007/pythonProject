from cvxopt import matrix, solvers
import numpy as np
import matplotlib.pyplot as plt
def train(x, y, C):
    # 定义x内积计算
    k = []
    for i in range(x.shape[0]):
        k.append([])
        for j in range(x.shape[0]):
            k[i].append(np.inner(x[i], x[j]))
    k = np.array(k)

    # 定义y的内积
    l = np.inner(y, y)

    # 定义凸优化pq方法
    p = matrix(l * k)  # 定义目标函数
    q = matrix(np.ones(40) * -1)
    A = matrix(y.reshape(1, -1))  # 定义等式约束
    b = matrix(0.)
    # 定义不等式约束
    g = matrix(np.vstack((np.eye(40) * -1, np.eye(40))))
    h = matrix(np.vstack((np.zeros(len(y)).reshape(-1, 1), np.ones(len(y)).reshape(-1, 1) * C)))

    # 求解函数
    solution = solvers.qp(p, q, g, h, A, b)

    # 获得拉格朗日系数a
    a = np.ravel(solution['x'])
    print(a.reshape(-1, 1).shape)
    print(y.shape)
    print(x.shape)
    # 获得最优w与b
    w_best = np.sum(a.reshape(-1, 1) * y * x, axis=0)
    b_best = 0
    for j in range(x.shape[0]):
        b_best += y[j] - np.sum(y * a.reshape(-1, 1) * np.inner(x, x[j].T).reshape(-1, 1))
    b_best = b_best / x.shape[0]

    return w_best, b_best


def split_train_test_data(mean1, mean2, sdt, n):
    # 生成正例数据
    np.random.seed(529)
    x_p1 = np.random.normal(loc=mean1, scale=sdt,size=int(n/2)).reshape(-1,1)
    x_p2 = np.random.normal(loc=mean1, scale=sdt,size=int(n/2)).reshape(-1,1)
    y_p = np.ones(len(x_p1))[:,np.newaxis]
    X_p = np.hstack((x_p1, x_p2))

    # 生成负例数据
    x_n1 = np.random.normal(loc=mean2, scale=sdt,size=int(n/2)).reshape(-1,1)
    x_n2 = np.random.normal(loc=mean2, scale=sdt,size=int(n/2)).reshape(-1,1)
    y_n = (np.ones(len(x_n1))*-1)[:,np.newaxis]
    X_n = np.hstack((x_n1, x_n2))

    # 绘图
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x_p1, x_p2, color = "#ffb07c", s = 100, label = "1")
    ax.scatter(x_n1, x_n2, color = "#c94cbe", s = 100, label = "-1")
    plt.legend()
   # plt.show()

    # 整合正负例的数据与类别变量，并划分测试集与训练集
    F_train = np.vstack((X_n[:int(n/2*0.8)], X_p[:int(n/2*0.8)]))
    y_train = np.vstack((y_n[:int(n/2*0.8)], y_p[:int(n/2*0.8)]))
    F_test = np.vstack((X_n[int(n/2*0.8):], X_p[int(n/2*0.8):]))
    y_test = np.vstack((y_n[int(n/2*0.8):], y_p[int(n/2*0.8):]))

    return F_train, F_test, y_train, y_test

F_train, F_test, y_train, y_test = split_train_test_data(6, 1, 2, 50)
w, b = train(F_train,y_train,100)
x = np.linspace(-6, 10 , 50)
y = (-w[0]/w[1]*x - b/w[1]).ravel()

plt.plot(x, y, color="#087804")
plt.show()











