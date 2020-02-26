## 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[-2:-1])

## 迭代
for i in range(0,12):
    print(i)

##列表生成式
a=[m + n for m in 'ABC' for n in 'ABC']
print(a)

##生成器
print("===============生成器==============")
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o=odd()

print(next(o))


###迭代器
#凡是可作用于for循环的对象都是Iterable类型；
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
from typing import Iterator, Iterable

print(isinstance('abc', Iterable))
print(isinstance(o, Iterator))