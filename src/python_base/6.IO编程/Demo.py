## io读取文件
with open('/Users/luohao/Desktop/python.txt','r') as f:
    s=f.readline()
    while s:
        print(s)
        s=f.readline()

## io写文件
with open('/Users/luohao/Desktop/python.txt','a') as f:
    f.writelines('adadwadwd')


##StringIO和BytesIO

from io import StringIO,BytesIO

f=StringIO('hello')

print(f.getvalue())

b=BytesIO('中文'.encode())

print(b.getvalue())


import os

mainPath=(os.path.abspath('.'))
insertPath=os.path.join(mainPath, 'testdir')
os.mkdir(insertPath)
os.rmdir(insertPath)



## 序列化

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s, default=lambda obj: obj.__dict__))


