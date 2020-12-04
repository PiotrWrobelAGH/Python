#!/usr/bin/env python


#DEADLOCK
import random
import threading
import time

class Philosopher(threading.Thread):
    def __init__(self, left_chopstick, right_chopstick, philosopher_id: int, lock):
        threading.Thread.__init__(self)
        self.left_chopstick = left_chopstick
        self.right_chopstick = right_chopstick
        self.philosopher_id = philosopher_id
        self.lock = lock

    def act(self, action: str):
        print("Philospher index: ", self.philosopher_id , " " , action)
        time.sleep(random.randint(1, 5))

    def run(self):
        self.act(str(time.time()) + " think")
        while True:
            self.lock.off()
            self.act(str(time.time()) + ": Pick up left chopstick")
            self.left_chopstick.take(self.philosopher_id)
            self.act(str(time.time()) + ": Pick up right chopstick: eat")
            self.right_chopstick.take(self.philosopher_id)
            self.act(str(time.time()) + ": Put down right chopstick")
            self.right_chopstick.puttdown(self.philosopher_id)
            self.act(str(time.time()) + ": Put down left chopstick: back to think")
            self.left_chopstick.puttdown(self.philosopher_id)
            self.lock.on()

class Chopstick:
    def __init__(self, number):
        self.number = number
        self.philosopher = -1
        self.lock = threading.Condition(threading.Lock())
        self.taken = False

    def take(self, philosopher):
        with self.lock:
            while self.taken:
                self.lock.wait()
            self.philosopher = philosopher
            self.taken = True
            self.lock.notifyAll()

    def puttdown(self, philosopher):
        with self.lock:
            while not self.taken:
                self.lock.wait()
            self.user = -1
            self.taken = False
            self.lock.notifyAll()
            
class Locker:
    def __init__(self, initial):
        self.lock = threading.Condition(threading.Lock())
        self.value = initial

    def on(self):
        with self.lock:
            self.value += 1
            self.lock.notify()
    
    def off(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1
            
if __name__ == "__main__":
    n = 5
    lock = Locker(n-1)
    philosophers = []
    chopsticks = []

    for i in range(n):
        chopsticks.append(Chopstick(i))
    
    for i in range(n):
        l_chopstick = chopsticks[i]
        r_chopstick = chopsticks[(i+1)%5]
        p = Philosopher(l_chopstick, r_chopstick, i+1, lock)
        p.start()
        philosophers.append(p)
        
    for t in philosophers:
        t.join()
