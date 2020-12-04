#!/usr/bin/env python
import random as rand
import threading as thrd
import matplotlib.pyplot as plt
out = {}

def calculate(first, last, lock, data):
    lock.acquire()
    temp = {}
    for x in data[first:last]:
        if not int(x) in temp:
            temp[int(x)] = 1
        else:
            temp[int(x)] += 1
            
    for key, value in temp.items():
        if key in out:
            out[key] += value
        else:
            out[key] = value
            
    lock.release()

if __name__ == "__main__":
    data = []
    for i in range(1000):
        data.append(rand.random()*100)
    thrd_arr = []
    lock = thrd.Lock()
    for i in range(4):
        t = thrd.Thread(target=calculate, args=(0 + i*250, 250 + i*250, lock, data))
        thrd_arr.append(t)
        t.start()
    for thread in thrd_arr:
        thread.join()
    out = dict(sorted(out.items()))
    out_list = [out[k] for k in out]
    plt.stem(out_list)
    plt.show()
    plt.hist(data,100)
    plt.show()
    