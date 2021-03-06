import sys

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1   # 初始化两个计数器a，b

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b=self.b,self.a+self.b# 计算下一个值
        if self.a>1000:# 退出循环的条件
            raise StopIteration()
        return self.a #返回下一个值

    def __getitem__(self, n):  #要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


def TestFib():
    for n in Fib():
        print(n)

def TestFib2():
    for i in range(0,10):
        print(Fib()[i])

def TestFib3():
    print(Fib()[:10])

if __name__=="__main__":
    TestFib2()
    print('\r\n')
    TestFib3()