## 使用__slots__ 对属性进行限制,只有slots添加的属性才可以被实例赋值，对继承的子类不起作用
class Student(object):
    __slots__ = 'age','name'

s=Student()
s.name='LuoHao'
print(s.name)


## @property 针对某个属性加上property注解,代表读，@属性.setter 代表写操作。用来简化赋值操作
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score=60

print(s.score)


### 定制类,提供一些方法帮助我们更好的使用类

##__str__ 帮助我们在打印类的时候使用自定义的信息模版
##__repr__ 和str一样，但是可以用来在传递值的时候也保证了打印出来的是自定义信息模版

class Animal(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
    __repr__=__str__

print(Animal('LuoHao'))

## 一个类想要被for遍历，那么需要实现__iter__方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

class Calculate(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.b+self.a
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

for i in Calculate():
    print(i)


## 枚举类

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.Jan.value)

## 动态的定义类

class Hello(object):
    pass

h=Hello()

print(type(Hello))
print(type(h))



class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list,metaclass=ListMetaclass):
    pass


my=MyList()
my.add(1)
print(my)


