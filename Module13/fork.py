'''
Implements Fork class for Philosophers to use in DiningPhilosophers problem.
'''

import threading

class Fork:
    def __init__(self):
        # Creating a Lock instance variable
        self.lock = threading.Lock()

    def acquire_fork(self):
        '''Return True if lock acquired, False otherwise.'''
        
        # Make sure Lock is non-blocking to avoid deadlocks
        acquired = self.lock.acquire(blocking = False)
        return acquired

    def release_fork(self):
        '''Release lock on Fork.'''
        self.lock.release()