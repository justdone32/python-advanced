## 类进阶

实例属性,实例对象独有的属性

类属性,类名访问类属性

实例中无同名属性时，可访问到类属性，当定义同名实例属性时，则无法访问

>使用实例属性去修改类属性十分危险，原因在于实例拥有自己的属性集，修改类属性需要使用类名，而不是实例名。 



vars : 查看实例内属性(自定义的属性)
dir : 显示类属性和所有实例属性
type : 显示类型



__doc__属性子类不继承，每个类均有自己的__doc__属性

### 类的方法
而在Python中，方法分为三类实例方法、类方法、静态方法。代码如下：

```python

　class Test(object):
    def instancefun(self):
        print("InstanceFun")
        print(self)

    @classmethod
    def classfun(cls):
        print("ClassFun")
        print(cls)

    @staticmethod
    def staticfun():
        print("StaticFun")
```

+ 实例方法隐含的参数为类实例self
+ 类方法隐含的参数为类本身cls
+ 静态方法无隐含参数，主要为了类实例也可以直接调用静态方法。
+ 类名可以调用类方法和静态方法，但不可以调用实例方法


### 私有化

+ xx: 公有变量
+ _x: 单前置下划线,私有化属性或方法，from somemodule import *禁止导入,类对象和子类可以访问
+ __xx：双前置下划线,避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)

+ \_\_xx\_\_:双前后下划线,用户名字空间的魔法对象或属性。例如:__init__ , __
不要自己发明这样的名字
+ xx_:单后置下划线,用于避免与Python关键词的冲突

通过name mangling（名称改编(目的就是以防子类意外重写基类的方法或者属性)，即前面加上“单下划线”+类名,eg：_Class__object）机制就可以访问private了。

```python
#coding=utf-8

class Person(object):
    def __init__(self, name, age, taste):
        self.name = name
        self._age = age 
        self.__taste = taste

    def showperson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    def dowork(self):
        self._work()
        self.__away()


    def _work(self):
        print('my _work')

    def __away(self):
        print('my __away')

class Student(Person):
    def construction(self, name, age, taste):
        self.name = name
        self._age = age 
        self.__taste = taste

    def showstudent(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    @staticmethod
    def testbug():
        _Bug.showbug()

#模块内可以访问，当from  cur_module import *时，不导入
class _Bug(object):
    @staticmethod
    def showbug():
        print("showbug")

s1 = Student('jack', 25, 'football')
s1.showperson()
print('*'*20)

#无法访问__taste,导致报错
#s1.showstudent() 
s1.construction('rose', 30, 'basketball')
s1.showperson()
print('*'*20)

s1.showstudent()
print('*'*20)

Student.testbug()
```
![私有变量](media/private.png)

### 分析一个类

```python
class Person(object):
    pass
```

python2.7中类的内建属性和方法
![py2class](media/py2class.png)

python3.5中类的内建属性和方法
![py3class](media/py3class.png)

python2.7中经典类(旧式类)的内建属性和方法
![py2class2](media/py2class2.png)

>经典类(旧式类),早期如果没有要继承的父类,继承里空着不写的类


```python
#py2中无继承父类，称之经典类,py3中已默认继承object
class Person:
    pass
```

子类没有实现__init__方法时，默认自动调用父类的。如定义__init__方法时，需自己手动调用父类的__init__方法。

####__slots__

合理使用__slots__属性可以节省一个对象所消耗的空间。一个普通对象使用一个dict来保存它自己的属性，你可以动态地向其中添加或删除属性，但是如果使用__slots__属性，那么该对象用来保存其自身属性的结构一旦创建则不能再进行任何修改。因此使用slot结构的对象节省了一部分开销。虽然有时这是一个很有用的优化方案，但是它也可能没那么有用，因为如果Python解释器足够动态，那么它完全可以在向对象添加属性时只请求该对象所使用的dict。