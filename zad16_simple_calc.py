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
inputstring = input("Podaj dzialanie w stylu a,b+c,d  gdzie liczba zespolona to a+b*i\n")
com1 = Complex_numb(int(inputstring[0]), int(inputstring[2]))
#Parsowanie
sign = inputstring[3]
com2 = Complex_numb(int(inputstring[4]), int(inputstring[6]))
if(sign == "+"):
    com3 = com1+com2
elif(sign == "-"):
    com3 = com1-com2
elif(sign == "*"):
    com3 = com1*com2
elif(sign == "/"):
    com3 = com1/com2
print("Wynik to:")
print(com3)
