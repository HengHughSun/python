# Classinfo-basic: 
int，float，bool，complex，str(字符串)，list，dict(字典)，set，tuple
##Loop
- 在python中 None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False
- is，is not是地址比较
  == ，!= 是值比较
## function 函数 
- Built-in Function 
		print（）  sorted（） len()
		yield() 生成器generator ---next()
        isinstance()isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。isinstance(object, classinfo)
            isinstance() 与 type() 区别：
            type() 不会认为子类是一种父类类型，不考虑继承关系。
            isinstance() 会认为子类是一种父类类型，考虑继承关系。
            如果要判断两个类型是否相同推荐使用 isinstance()。isinstance((1, 2, 3), (list, tuple))  True
        dir()  获取一个对象的所有属性和方法,配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
                        一个正确的用法的例子如下：

                            ```
                            def readImage(fp):
                                if hasattr(fp, 'read'):
                                    return readData(fp)
                                return None

                            ```
        bin()二进制
        hex()把一个整数转换成十六进制表示的字符串
        ord()取出string对应的num
    高级用法
        递归
        切片
        迭代
        列表生成式即List Comprehensions [x * x for x in range(1, 11)]
                                    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    

statement/sentence 声明/句子、命题  def   del  for 
attribute 属性
---函数 优点:便于理解和重复使用
    class 类,对象  
        python内置的类 
            math、functools、
        
        method 类函数，方法 | 给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法Method
                        换种说法就是方法是与‘实例’绑定的函数，和普通函数不同，方法可以<直接>访问实例的数据
        .pop（）  .sort（） .remove()

    

        数据封装：
            将一个对象的多个状态写为一个函数
        继承和多态：
            继承Son(Father)    多重继承，一个子类就可以同时获得多个父类的所有功能。 命令格式XXXMixIn
            多态：子态 覆盖 父态  父态 无法覆盖 子态
                多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，
                因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，
                因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：


        实例属性和类属性
            实例属性属于各个实例所有，互不干扰；

            类属性属于类所有，所有实例共享一个属性；

            不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
        
        __slots__
        为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
        对继承的子类并不生效

        
        @property
        @property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，
        此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，
        于是，我们就拥有一个可控的属性操作：


        还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

## 错误处理，调试，单元测试，文档测试
### 错误处理： 
1. 高级语言通常都内置了一套
        try...except...finally...的错误处理机制 
                    用raise抛出
              2、 logging模块 记录到file或console  分debug info warning error
    调试：  就用IDE的断点测试 或者 logging模块
    单元测试： unittest模块
            编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。

        以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
        对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，
        我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()：

            setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，这时，
            就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码：


    文档测试：
        Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
        if __name__ == '__main__':
            import doctest
            doctest.testmod()



<h1>文件</h1>
    open() read(size)/readline()/write()  close() 
        建议用 with 不建议将open()赋值给某个人
        open(encoding='gbk', errors='ignore')
            r
            rb 
            w 
            wb
                a append 已追加模式写入
        
        readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list
        如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；
        如果是配置文件，调用readlines()最方便
（1）以r或R开头的python中的字符串表示（非转义的）原始字符串
f = open(r'C:\Program Files\Adobe\Reader 9.0\Setup Files\setup.ini','r')

（2）以u或U开头的字符串表示unicode字符串
            
类名应采用驼峰命名法 ,即将类名中的每个单词的首字母都大写,而不使用下划线。
实例名和模块名都采用小写格式,并在单词之间加上下划线。
正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；

类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

///类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

我们要添加自己的搜索目录，有两种方法：

一是直接修改sys.path，添加要搜索的目录：
```
>>> import sys
>>> sys.path.append('/Users/michael/my_py_scripts')
```
这种方法是在运行时修改，运行结束后失效。

第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

组合:支持嵌套 key具有唯一性
        list 列表，数组
        tuple 固定列表，固定数组
        dict  dictionary字典
        set  集合 类似于列表,但输出的每个元素都必须是独一无二的

------------
**print**

print() 是等内容全部执行完，在输出的#print(2,3,1/2)  2,3,0.5

'''XXXX加回车'''表示多行内容

    print('''line1
    line2
    line3''')
r'XXXX'  表示‘’内部的字符串不转义、转义字符\后必须跟东西不能是单个

多行和r可以联用
    print(r'''hello,\n
    world''')

设定 sep 参数来修改分隔符

    print(sep( )) 以空格分割
    >>> print("Hello","World", sep="***")
    Hello***World
    每一行输出都默认以新行字符(>>>)结束, 使用 end 参数也能改变结束方式
    >>> print("Hello","World", end="***")
    Hello World***>>>
格式化字符串
    print("%s is %d years old." % (aName, age))
|字符 |输出格式|
|-|-    |
|d,i|整型|
|u|  无符号整型|
|f|  浮点型,如 m.ddddd|
|e|  浮点型,如 m.ddddde+/-xx|
|E|  浮点型,如 m.dddddE+/-xx|
|g|  指数比-4 小或比 5 大时使用%e,否则使用%f|
|c|  单字符|
|s|  字符串或者是能通过 str()转为字符串的数据|
|%|  输入一个%|
除了转换字符之外,你也可以在%和转换字符之间插入格式修饰符。格式修饰符可以用一段给定
长度的空格使变量实现左对齐或者右对齐。格式修饰符也可在小数点后添加数字,来指定字段宽度。
表 10 给出了这些格式修饰符的使用。

|修饰符类型 |例子 | 描述|
|--|--|--|
|number  |%20d     |变量值占据 20 个字符宽度|
|-       |%-20d    |变量值占据 20 个字符宽度,左对齐|
|+       |%+20d    |变量值占据 20 个字符宽度,右对齐|
|0       |%020d    |变量值占据 20 个字符宽度,前置“0”|
|.       |%20.2f   |变量值占据 20 个字符宽度,且保留两位小数|
|(name) |%(name)d  |从字典中取 key 为 name 的值放在此处|

---
**string 字符串**
|   |   |
|---|---|
| rstrip(),lstrip() 和 strip() | 剔除后面、前面、前后的空白 |
|upper()          | # 把所有字符中的小写字母转换成大写字母 | 
|lower()          | # 把所有字符中的大写字母转换成小写字母 |
|capitalize()     |# 把第一个字母转化为大写字母，其余小写,即整句话的首字母大写|
|title()          |# 把每个单词的第一个字母转化为大写，其余小写，即每个单词的首字母大写|
|replace("","")   |# 从X字符替换为Y字符|
|split(",")       |# 如果找到分隔符的实例，将字符串拆分为子字符串|
|center(w)        |# 返回一个字符串,w 长度,原字符串居中|
|ljust(w)         |#居左|
|rjust(w)         |#居右 |
|find('item')     |#查询 item,返回第一个匹配的索引位置,给出下标  等同与list.index('')|
|count(item) |#返回原字符串中出现 item 的次数|


----
**list**
///range(101)相当于range(0,101)生成的序列是从0开始小于101的整数：==sequence Shell：seq((0..100)) 
//range()还可以指定步长range(0,101,2)生成的序列是从0开始小于101的偶数，步数支持负数 注意range只是生成数据 引用需要赋值
----
**random**
| | |
|--|--|
|随机数 |random.randint(a,b)|
|选择   |random.choice()|
在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。

如果知道最终要测试的条件,应考虑使用一个 elif 代码块来代替 else 代码块。这样,你就可以肯定,仅当满足相应的条件时,你的代码才会执行。
避免恶意尝试，或者攻击

as 可以为模块和函数取别名
import module_name (as X)
from module_name import function_name1,function_name2 
from module_name import function_name (as fn)
from module_name import * == import module_name

打开文件时,可指定读取模式 ( 'r' )、写入模式 ( 'w' )、附加模式 ( 'a' )或让你能够读取和写入文件的模式( 'r+' )

plot()折线图
scatter()散点图



数字处理方式
    ValueError: invalid literal for int() with base 10: '1127437398.85751'
可以选转换为float在转换为整数


生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

把list、dict、str等Iterable变成Iterator可以使用iter()函数：
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

##装饰器(Decorator)
Decorator 本身是一个函数，目的是在不改变待装饰函数代码的情况下，增加额外的功能，装饰器的返回值是**已装饰的函数对象**
    解释之前请理解
    1、 *实例化*
    - 变量指向了函数对象，这个过程可以被看作“实例化”
    2、 函数**带括号和不带括号**时的区别
    - 无括号仅代表一个函数对象，带括号如cal(1,2)，代表告诉编译器“执行cal这个函数”
@decorator的作用是把原foo函数（带装饰函数）赋值给dec函数（装饰器），然后将返回值wrapper函数（已装饰函数）重新赋值给foo函数。因此foo（2）语句实际执行情况是：
```python
def dec(f):
    n = 3
    def wrapper(*args,**kw):
        return f(*args,**kw) * n
    return wrapper
def foo(n):
    return n * 2

foo = dec(foo)
foo(2)
def wrapper(2):
    return foo(2)*3
```
*注：以上代码是为了方便理解，直接将实参n=2带入函数定义中，语法上并无实际意义。*
用数学符号表示的话，函数执行结果为foo(2)=wrapper(2)=foo(2)*3 = 2*2*3=12,其中前面的foo函数是已装饰函数，后面的foo函数是原来的待装饰函数。By the way,函数参数中的*args代表可变参数,**kw代表关键字参数
