

#准备数据 可视化
import numpy as np
import matplotlib.pyplot as plt
class Svm:
    def __init__(self):
        self.markers = {-1: 'o', 1: 'x'}
        self.colors = {1: 'r', -1: 'g'}
        self.fig = plt.figure()


    def train(self,data):
        self.data=data
        # 参数字典 { ||w||: [w,b] }
        opt_dict = {}

        # 数据转换列表
        transform = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

        # 从字典中获取所有数据
        all_data = []
        for yi in self.data:
            for featureset in self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)

        # 获取数据中的最大值，最小值
        self.min_feature_value = min(all_data)
        self.max_feature_value = max(all_data)
        all_data=None

        # 定义一个步长列表
        step_size = [self.max_feature_value * 0.1, self.max_feature_value * 0.01, self.max_feature_value * 0.001]

        # 参数b的范围设置
        b_range_mutiple = 2
        b_mutiple = 5
        latest_optimum = self.max_feature_value * 10

        # 基于不同步长进行训练优化
        for step in step_size:
            w = np.array([latest_optimum, latest_optimum])
            optimized = False
            while not optimized:
                for b in np.arange(-1 * (self.max_feature_value * b_range_mutiple), self.max_feature_value * b_range_mutiple,
                                   step * b_mutiple):
                    for transformation in transform:
                        w_t = w * transformation
                        found_option = True
                        for i in data:
                            for xi in data[i]:
                                yi = i
                                # 判断是否满足条件
                                if not yi * (np.dot(w_t, xi) + b) >= 1:
                                    found_option = False
                        if found_option:
                            opt_dict[np.linalg.norm(w_t)] = [w_t, b]
                if w[0] < 0:
                    optimized = True
                else:
                    w = w - step
            norms = sorted([n for n in opt_dict])
            # ||w||: [w,b] 选取||w||最小的哪一个
            opt_choice = opt_dict[norms[0]]
            self.w = opt_choice[0]
            self.b = opt_choice[1]
            latest_optimum = opt_choice[0][0] + step * 2

        for i in data:
            for xi in data[i]:
                yi = i
                print(xi, ':', yi * (np.dot(w, xi) + b))



    # 定义预测函数
    def predict(self,features):
        # 模型 sign(w*x+b)
        classfication = np.sign(np.dot(np.array(features), self.w) + self.b)
        if classfication != 0:
            plt.scatter(features[0], features[1], s=200, marker='^', c=self.colors[classfication])
            print(classfication)
        return classfication

    def visualize(self):
        [[plt.scatter(x[0], x[1], color=self.colors[i], marker=self.markers[i]) for x in data_dict[i]] for i in data_dict]
        x=np.linspace(3,10,50)
        y=(-self.w[0] * x - self.b ) / self.w[1]
        plt.plot(x,y,c='b')
        plt.show()


#字典记录样本点和标记数据
data_dict={-1:np.array([[1,7],[2,8],[3,8]]),1:np.array([[5,-1],[6,-1],[7,3]])}
features=[[0,10],[1,3],[3,4],[3,5],[5,5],[5,6],[6,-5],[5,8],[2,5],[8,-3]]

svm=Svm()
svm.train(data=data_dict)
for p in features:
    svm.predict(p)
svm.visualize()


#定义模型主体和训练部分



#predict(features)





