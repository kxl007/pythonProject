import numpy as np
import matplotlib.pyplot as plt
def KdTree(nums):
    plt.figure()
    ax=plt.axes()
    #绘制各个样本点
    [plt.scatter(x[0],x[1],c='black')for x in nums]
    #绘制过某个样本点的垂线

    plt.axvline(x=3, color='r', linestyle='--', label='xxx')

    #绘制水平线
    plt.axhline(y=2, ls="-.", c="b")


    plt.legend()
    plt.show()

nums=[[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]]
KdTree(nums)
