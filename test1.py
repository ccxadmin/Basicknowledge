import sys
from types import MethodType


class Student(object):
    staticcount=0
   # __slots__ = ('name', 'age','set_age','score')  # 用tuple定义允许绑定的属性名称,定义一个特殊的__slots__变量，来限制该class实例能添加的属性
    def __init__(self,name):
       self.name=name
       self._birth=1991
       self._score=100;
       Student.staticcount=Student.staticcount+1

    staticName="xiaoming"

#另一个机制，那就是写一个__getattr__()方法，动态返回一个属性,返回函数也是完全可以的：
    #注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


    def __str__(self):
        return 'Student object (name: %s)' % self.name

    def __call__(self):
        print('My name is %s.' % self.name)

    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth=value

    # @property
    # def age(self):
    #     return 2015 - self._birth
    @property
    def Score(self):
        return self._score

    @Score.setter
    def Score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value



def set_score(self, score):
    self.score = score
    print('实例绑定方法，动态语言特性', str(self.score))


def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age
    print('实例绑定方法，动态语言特性',str(self.age))

def TestClass():
    ss= Student('xiaohong')
    ss2=Student('xiaohei')
    ss3 = Student('xiaoxin')
    print(ss3())

    # 给实例绑定name属性
    ss3.Name="temname"
    print(ss3.Name, '\n')

    print( ss3.age(), '\n')
    print(ss.staticName,'\n')
    print(ss.name,'\n')
    print(Student.staticName, '\n')
    print(Student.staticcount, '\n')

    ss.set_age = MethodType(set_age, ss)  # 给实例绑定一个方法
    ss.set_age(100)
    print(ss.age, '\n')

    # ss2.set_age(100)
    Student.set_score = set_score#实例绑定方法，
    ss2.set_score(60)
    print(ss2.score, '\n')
    print(ss2.Score, '\n')

if __name__=="__main__":
    TestClass()
