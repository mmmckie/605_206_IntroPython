'''

'''

import random
import threading
import time
from fork import Fork

class Philosopher(threading.Thread):
    running = True

    def __init__(self, name: str, left_fork: Fork, right_fork: Fork):
        super().__init__()
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while self.running:
            self.think()
            self.eat()
        print(f'{self.name} is cleaning up.')
        # self.thread.join() ?

    def think(self):
        thinking = random.uniform(3, 5)
        print(f'{self.name} is thinking for {thinking} seconds.')
        time.sleep(thinking)
        print(f'{self.name} is now hungry.')

    def eat(self):
        if self.left_fork.acquire_fork():
            # print(f'{self.name} has acquired left fork: {self.left_fork}')
            if self.right_fork.acquire_fork():
                    # print(f'{self.name} has acquired right fork: {self.right_fork}')
                    eating = random.uniform(3, 5)
                    print(f'{self.name} is eating for {eating} seconds.')
                    time.sleep(eating)

                    self.right_fork.release_fork()
                    print(f'{self.name} has put down his right fork.')
                
            self.left_fork.release_fork()
            print(f'{self.name} has put down his left fork.')
            
        else:
            return