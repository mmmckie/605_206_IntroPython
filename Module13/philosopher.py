'''
Implementation of Philosopher class for DiningPhilosophers problem.
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

    def think(self):
        '''Makes philosopher think for a random time, then get hungry.'''

        # Set 3-5 second random thinking time and print result
        thinking = random.uniform(3, 5)
        print(f'{self.name} is thinking for {thinking} seconds.')
        
        # Make thread idle while Philosopher is thinking
        time.sleep(thinking)

        # Done thinking, time to eat
        print(f'{self.name} is now hungry.')

    def eat(self):
        '''Attempt to acquire left and right forks so the Philosopher can eat.'''
        
        # If Philosopher can acquire both left and right forks
        if self.left_fork.acquire_fork():
            if self.right_fork.acquire_fork():
                    # Then begin eating for a random 3-5 second time and print
                    eating = random.uniform(3, 5)
                    print(f'{self.name} is eating for {eating} seconds.')

                    # Make thread idle while Philosopher is eating
                    time.sleep(eating)

                    # Done eating, put down right fork
                    self.right_fork.release_fork()
                    print(f'{self.name} has put down his right fork.')
            
            # Put down left fork if done eating or if couldn't get right fork
            self.left_fork.release_fork()
            print(f'{self.name} has put down his left fork.')
