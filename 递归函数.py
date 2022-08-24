def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

#解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
#这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，
#都只占用一个栈帧，不会出现栈溢出的情况。
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式