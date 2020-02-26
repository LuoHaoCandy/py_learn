###map()
## map的作用是传入两个参数，一个是函数，一个是Iterable 把每个元素都作用在map上

def fun(num):
    num=num+1
    return num

for i in map(fun,[1,3,4,5]):
    print(i)

### reduce()
##  reduce的作用是传入一个函数【此函数的入参必须是两个】, 然后把每次计算的结果作为下一次的入参之一进行计算

from functools import reduce

def sumTotal(x,y):
    return x+y

a=reduce(sumTotal,[1,3,5,7,9])
print(a)



##练习 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
    str = name.title()
    return str

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


## filter
## filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def getOdd(num):
    return num%2==1

for i in filter(getOdd,[1,2,3,4,5]):
    print(i)


## 返回函数

def fun(num):
    def sum():
        return num
    return sum

a=fun(1)
result=a()
print(result)


## 匿名函数

a=map(lambda x:x*x,[1,2,3,4])

for i in a:
    print(i)


## 装饰器 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
print('======装饰器======')
def text(name):
    def log(func):
        def wrapper(*args, **kw):
            print(name+'call %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper
    return log



@text('a')
def now():
    print('2015-3-25')

now()


## 偏函数 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。


