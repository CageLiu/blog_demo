1.位置参数
2.关键字参数
3.元组参数
4.字典参数

1.位置参数
	特点：不限个数；调用时必须提供个数和位置都与形参相同的实参；不灵活。
	示例代码:

#函数声明
#第三个参数要能转化为数字，否则将报错
def fn(a,b,c):
    sum = a + b + c
    num = int(c);

#函数调用
fn(1,2,3)			#正确的调用
fn(1)				#错误的调用
fn(1,2,'asd')		#错误的调用

2.关键字参数
    特点：不限个数；不用关心形参的顺序;当没有传递对应参数时，有默认值供函数使用。
示例代码：
#函数声明
def fn(a = 1,b = 2, c = 0):
    print a
    print b
    print c

#函数调用
fn()                            #正确,a = 1, b = 2, c= 3
fn(10,11,12)                    #正确,a = 10, b = 11, c = 12
fn(10,b = 21, c = 30)           #正确,a = 10, b = 21, c= 30
fn(10,c = 21, b = 30)           #正确,a = 10,b = 30, c = 21
fn(c = 2, b = 4, a = 7)         #正确,a = 7, b = 4, c = 2
fn(13, a = 2l, c =8)            #错误,函数传递的第一个参数没有使用关键字。那么默认会传递给函数声明的第一个形参
                                #后面再次给关键字参数 a 传递一个值，这时会触发 python 的 TypeError:
                                #multiple values for keyword argument 'a',即：关键字参数 a 有多个值
fn(a = 12,1,4)                  #错误，关键字参数不管是声明还是调用时，都应在位置参数的后面

3.元组参数
    特点：参数个数不固定(调用是不需要知道需要传递几个参数的)，实参的个数可以是 0 个，也可以是无数个。
    示例代码：
#函数声明
def fn(*args):
    for i in args:
        print i
#函数调用
fn(1,2,3)                   #正确，分别打印出1，2，3
fn(*(1,2,3))                #正确，打印出1，2，3

    说明：当函数的参数带有 ＊ 标志时，python 会对传入的参数在内部进行一下处理，即：把获得的参数转换为一个元组（tuple）。对于以上示例中的第一个调用，可分为两步来理解：
    step1：函数接收到了三个实参1，2，3
    step2：用这3个实参组成一个 tuple

    第二个调用中，函数接收到的参数本身就是一个 tuple，但调用时还是要给这个元组类型的实参加上＊号前缀，以说明这是一个元组参数


4.字典参数
    特点：类似于元组参数，不过和元组参数不同的是，字典参数相当于是不固定的关键字参数，而元组参数相当于个数不定的位置参数
    示例代码：
#函数声明
def fn(**keyargs):
    for k,v in keyargs.items():
        print k + "=>" + v

#函数调用
fn(a = 2, b = 3, c = 4)                 #正确，打印出 a => 2,b = > 3, c => 4
fn(**{'a':2,'b':3,'c':4})               #正确，打印出 a => 2,b = > 3, c => 4


    说明：和元组参数类似，函数将接收到的参数按 key ＝> value 的方式组成一个字典，以供函数内部使用


    最后需要注意的一点就是：
    当几种类型的参数混合使用时，要注意它们的书写顺序，正确的顺序应该是：
    位置参数 －》关键字参数 －》元组或字典参数
