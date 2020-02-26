## 类和实例
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


stu=Student('name',60)
print(stu.name)


## 访问限制 __ (两个下划线代表对象是私有的)

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def name(self):
        return self.__name


stu=Student('name',60)
print(stu.name())


### 继承和多态

class Animal(object):
    def run(self):
        print('aaaa')


class Dog(Animal):
    pass

dog=Dog()
dog.run()

### 获取对象信息

class Test(object):
    def __init__(self,x):
        self.x=x
    def power(self):
        return self.x*self.x

test=Test(1)
print(test.power())
print(type(test))
print(isinstance(test,Test))
print(dir(test))

### 实例属性和类属性

class Student(object):
    name='LuoHao'

print(Student.name)