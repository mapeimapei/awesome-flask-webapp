class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B,C):
    def __init__(self):
        print("D")
        super(D,self).__init__()

#既然我们重写B的构造函数，为什么还要去调用super？
#super到底执行顺序是什么样的？




if __name__ == "__main__":
    print(D.__mro__)
    d = D()











