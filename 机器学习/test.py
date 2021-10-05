import numpy as np
w=np.array([0,1,0])
w1=np.array([1,1,1])
w2=w+w1
s=[(w1,1),(w2,1)]
print(s[1][1]*s[1][0])
print(w2)
print(np.dot(w,w1))
X_train = np.array([[3, 3], [4, 3], [1, 1]])
print(X_train.shape[0])