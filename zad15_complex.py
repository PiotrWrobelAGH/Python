#!/usr/bin/env python

class Complex_numb:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return Complex_numb(self.a+other.a, self.b+other.b)
    def __sub__(self, other):
        return Complex_numb(self.a-other.a, self.b-other.b)
    def __mul__(self, other):
        return Complex_numb(self.a*other.a-self.b*other.b, self.a*other.b+self.b*other.a)
    def __truediv__(self, other):
        othermin = other
        othermin.b = -othermin.b
        temp = self*othermin
        temp.a = temp.a/(other.a**2+other.b**2)
        temp.b = temp.b/(other.a**2+other.b**2)
        return temp
    def __str__(self):
        return f"{self.a}, {self.b}i"

Ob1 = Complex_numb(1,8)
Ob2 = Complex_numb(2,3)
Ob3 = Ob1 / Ob2
print(Ob3)