# write a program to understand the order of execution of methods in several base classes according to method resolution order(MRO).

class A(object):
    def method(self):
        print("A class method called")
        super(A, self).method()

class B(object):
    def method(self):
        print("B class method called")
        super(B, self).method()

class C(object):
    def method(self):
        print("C class method called")
        super(C, self).method()

class X(A, B):
    def method(self):
        print("X class method called")
        super(X, self).method()

class Y(B, C):
    def method(self):
        print("Y class method called")
        super(Y, self).method()

class P(X, Y):
    def method(self):
        print("P class method called")
        super(P, self).method()

newp = P()
print(P.mro())
newp.method()

