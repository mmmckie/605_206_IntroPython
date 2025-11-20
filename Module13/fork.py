'''

'''

import threading

class Fork:
    def __init__(self):
        self.lock = threading.Lock()# TODO: add a lock as an instance variable
        pass

    def acquire_fork(self):
        '''Return True if lock acquired, False otherwise.'''
        acquired = self.lock.acquire(blocking = False)
        return acquired

    def release_fork(self):
        self.lock.release()