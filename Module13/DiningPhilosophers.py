'''
Utilizes the Fork and Philosopher classes to implement the DiningPhilosophers
problem.
'''

import time

from fork import Fork
from philosopher import Philosopher

def DiningPhilosophers():
    '''
    Creates 5 philosophers, assigns them each a left and right fork, then
    starts a thread for each philosopher. Once started, all threads will run for
    10 seconds before exiting.
    '''
    
    names = ['Plato', 'Aristotle', 'Buddha', 'Marx', 'Nietzsche']
    
    # Create 1 fork for each philosopher and assign them numbers, then
    # add to 'forks' dict
    forks = {}
    for i in range(len(names)):
        forks[f'fork_{i}'] = Fork()

    # Create each philosopher and assign them a left and right fork
    philosophers = {}
    for i in range(len(names)):
        name = names[i]
        left_fork = f'fork_{i}'

        # Making sure the last philosopher's right fork is index 0
        # i.e., the left fork of the first philosopher
        if name == names[-1]:
            i = -1
        right_fork = f'fork_{i+1}'
        
        # Create Philosopher and add to dict
        philosophers[name] = Philosopher(name, forks[left_fork], forks[right_fork])

    # Start all Philosopher threads
    for name in names:
        philosophers[name].start()
    
    # Create time delay to let all threads run for 10 secs
    time.sleep(10)
    
    # Set running to False for all philosophers so they all clean up
    Philosopher.running = False
    
    # Exit all threads
    for name in names:
        philosophers[name].join()


if __name__ == '__main__':
    DiningPhilosophers()
