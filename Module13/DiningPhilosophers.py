'''

'''

import time

from fork import Fork
from philosopher import Philosopher

def DiningPhilosophers():
    names = ['Plato', 'Aristotle', 'Buddha', 'Marx', 'Nietzsche']
    
    forks = {}
    for i in range(len(names)):
        forks[f'fork_{i}'] = Fork()

    philosophers = {}
    for i in range(len(names)):
        name = names[i]
        left_fork = f'fork_{i}'

        # Making sure the last philosopher's right fork is index 0
        if name == names[-1]:
            i = -1
        right_fork = f'fork_{i+1}'
        philosophers[name] = Philosopher(name, forks[left_fork], forks[right_fork])

    for name in names:
        # TODO: make sure these are non-blocking (?)
        philosophers[name].start()
    
    time.sleep(10)
    
    # Set running to False for each philosopher
    for name in names:
        philosophers[name].running = False
    
    # Exit all threads
    for name in names:
        philosophers[name].join()

if __name__ == '__main__':
    DiningPhilosophers()