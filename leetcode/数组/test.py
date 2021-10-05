import sys
import string
nums=[0,0]
#nums.remove(2)# 删除第一个匹配的数据

for item in nums[:]:
    if item==0:
        nums.remove(item)
print(nums)

array=['aa','bb','cc','dd']
matrix=[array]*3

print(matrix[0][1])
print(matrix[0])

arr1=[[1 for j in range(5)]for i in range(5)]
print(arr1)

print(int(5/2))

x=-123
if x<0:
    print('true')
print(str(x)[3])

z='-123'
y=2**3
print(y)

print(int(z))

#for i in range(4, 0, -1):
    #print(i)

s='llal'
s1=s.replace('l','')
s2='abcdefhijklmnopqrstuvwxyz'
print(len(s2))
print(s1)
m=''
m=''.join([m,'1'])
print(m)

m1='gggod'
m2='lllllllll'
#if len(m1) != len(m2):
   # sys.exit(0)


k=m1.count(m1[0])
print('11111')

s1='1   lls '
s1.lstrip('')
print(len(s1))
print(s1[0].isalnum())

s2='-00 13'

#s3=int(s2)
print(s2)
#print(s3)
kkk=1
c=2
print(str(kkk)+str(c))

print(1/2)

numss=[1]
if not numss:
    print(113131)

a=[1,1,1,2,3]
print(type(a))
print(list(set(a)))


if 0==-0:
    print(131321)
aksd=[1,2,3,4]




print(aksd[1:4])# 列表拆分

matrix = ['adbc']

d=list(matrix[0])
d.sort()
print(type(d))
print(d)


m2=['qweqe','1dadadqw','1','1']
#x231=list(enumerate(m2))


m3=[1,2,3,2,3]
print(list(set(m3)))


m4=[1,2]
print(m4.clear())
print(m3[1:])


print('....')

i=9
print('%d'%i+'its factors are'+'%d'%m3[0])

strs='1'
strs=','.join([strs,'3'])
print(strs)

st1={'a':1,'b':3,'a':2}
print('........')

print(st1['a'])

m5=[x for x in range (1,5)]
print(m5)
import numpy as np

# 将列表转换为numpy的数组
a = np.array(["a", "b", "c", "a", "d", "a"])
# 获取元素的下标位置
eq_letter = np.where(a == "a")
print(eq_letter[0])  # [0 3 5]

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]



for j in strs:
    print(j)

strs.pop(1)
print(strs)


m5=[0,1,2,3,0,0]
print(list(set(m5)))




strs1="Let's take LeetCode contest"
x=strs1[4]
strs1=strs1.replace('e','M')

print(strs1)

nums = [2,3,1,2,4,3]
nums=set(nums)
print('........')
print(nums)
