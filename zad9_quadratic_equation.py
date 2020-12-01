#!/usr/bin/env python
import math, sys

def main(argv):
    a = int(argv[0])
    b = int(argv[1])
    c = int(argv[2])
    delta = b**2 - 4*a*c
    if(delta < 0):
        print("Brak rozwiazan")
        return
    if(delta == 0):
        print(f"Rozwiazanie to x1 = {-b/2/a}")
        return
    sqrt_delta = math.sqrt(delta)
    print(f"Rozwiazanie to x1 = {(-b-sqrt_delta)/2/a}, x2 = {(-b+sqrt_delta)/2/a}")
    return
    
    
if __name__ == "__main__":
    main(sys.argv[1:])