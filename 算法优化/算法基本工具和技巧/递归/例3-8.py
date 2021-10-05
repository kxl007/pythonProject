#递归 后入先出
import pysnooper
@pysnooper.snoop()
def highTolow(s): #
    if s>1:
        highTolow(int(s / 10))# c除到最高位---压栈
    print(s % 10)             # 回溯输出

highTolow(1000)


