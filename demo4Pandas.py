import os
import pandas as pd
import requests


PATH = r'C:\Users\35163\Desktop\力\课程\机器学习\PYTHON 练习'

r = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

with open(PATH+'iris.data', 'w') as f:
    f.write(r.text)

os.chdir(PATH)

df = pd.read_csv(PATH+'iris.data', names=['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])

print(df.head)

print(df['sepal length'])

print(df['class'].unique())

print(df[df['class']=='Iris-virginica'])

print(df[(df['class']=='Iris-virginica')&(df['petal width']>2.2)])

print(df.describe())

print(df.corr())