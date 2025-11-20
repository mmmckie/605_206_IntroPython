Name: Max McKie (mmckie2)

Module Info: Module 4 Assignment: N-body Simulation due on 09/21/2025 at 11:59 EST

Approach: 

nbody.py - First the total simulation runtime, simulation timestep, and lists
containing the initial x-position, y-position, x-velocity, y-velocity, and mass,
respectively, for Earth, Mars, Mercury, the Sun, and Venus are initialized. Each
of the lists containing the planets' data is stored in another list called
'planets' in the same order. Three constants - 'SUN_IDX', 'M_SOL', and 'G' - are
also initialized here representing the index of the Sun's data in the 'planets'
list, the mass of the Sun (retrieved by indexing the Sun's data from the 'planets'
list), and the gravitational constant. A counter variable 't' is then initialized
at 0 to track the current timestep throughout the simulation runtime. The
simulation begins with a while loop which checks at each iteration whether the
simulation has completed. If not, then for each timestep there is a for loop which
iterates through the indices of the 'planets' list. If the index is equal to
'SUN_IDX', then a continue statement will move to the next iteration to avoid
calculating the Sun's influence on itself. If it is the index of any other planet,
then the x-distance, y-distance, and radial distance between that planet and the
sun will be callculated and the planet's mass will be retrieved by indexing its
data from the 'planets' list. The gravitational force will then be calculated
using 'G', 'M_SOL', the planet's mass, and the calculated radial distance. The 
x- and y-components of the gravitational force are then computed using dx/r and
dy/r, and these are used to calculate the x- and y-components of the planet's
acceleration. The updated values for the planet's x- and y-velocity and x- and 
y-position are then calculated according to the kinematic equations using 
the simulation timestep, the computed accelerations, and the planet's current
position and velocity values. The planet's data is then updated in-place in
the 'planets' list, and once all planets have been iterated over, the simulation
time is incremented by the timestep to continue the simulation until t is >=
'RUNTIME', at which point the simulation will terminate. Once the simulation
is complete, a for loop will iterate over each planet's list of data contained
in the 'planets' list. At the start of each iteration, an empty string will be
instantiated, and then each attribute stored in that planet's list of data will
be iterated over in another for loop. For each attribute, an f-string will format
the value to scientific notation with 4 decimal places with an additional space
after to separate each successive attribute in the output string. Each of these
formatted attributes will be concatenated onto the initially empty string to
form the final output, and then the trailing space from the last attribute 
will be trimmed by slicing off the very last character. Finally, the output
string will be printed for each planet to produce 5 total lines of printed
outputs to the terminal.

Known Bugs:
There are no known bugs.

Citations:

- https://zetcode.com/python/fstring/