'''
This script will run a Newtonian simulation of the orbits of Earth, Mars,
Mercury, and Venus around the Sun. It will run for a period of just over 5
years with an update timestep of 25,000 seconds. The Sun is assumed to be fixed
and the planets are not assumed to influence each other - only the gravitational
influence of the Sun on each planet is considered/calculated.

Each of the planets' initial x- and y-positions, x- and y- velocities, and
masses are hardcoded in lists at the start of the script. At each timestep of
the simulation, the distance in the x-direction, y-direction, and radially will
be computed, so that the x- and y- components of F_gravity and acceleration can
be calculated. The classical kinematic equations are then used to update each
planet's position and velocity for each timestep, and when the simulation 
is complete the script will print out the positions, velocities, and masses
of each planet out to 4 decimal places in scientific notation.
'''

RUNTIME = 157_788_000 # Total simulation runtime, seconds
dt = 25_000 # Simulation timestep, seconds

# Planet_data = [x_pos, y_pos, x_vel, y_vel, mass]
earth = [1.4960e+11, 0.0000e+00, 0.0000e+00, 2.9800e+04, 5.9740e+24]
mars = [2.2790e+11, 0.0000e+00, 0.0000e+00, 2.4100e+04, 6.4190e+23]
mercury = [5.7900e+10, 0.0000e+00, 0.0000e+00, 4.7900e+04, 3.3020e+23]
sun = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.9890e+30]
venus = [1.0820e+11, 0.0000e+00, 0.0000e+00, 3.5000e+04, 4.8690e+24]

planets = [earth, mars, mercury, sun, venus]
SUN_IDX = 3 # Position of sun in above list
M_SOL = planets[SUN_IDX][-1] # Solar mass
G = 6.67e-11 # Gravitational constant

t = 0 # Current simulation time, seconds
while t < RUNTIME:
    for i in range(len(planets)):
        # Assume sun is fixed, only calculate its influence on other planets
        if i == SUN_IDX:
            continue
        
        dx = planets[SUN_IDX][0] - planets[i][0] # X distance, sun to planet
        dy = planets[SUN_IDX][1] - planets[i][1] # Y distance, sun to planet
        r = (dx**2 + dy**2)**(0.5) # Radial distance, sun to planet
        m = planets[i][-1] # Mass of current planet

        F = G * M_SOL * m / (r**2) # Gravitational force

        # X and y components of F
        F_x = F * (dx / r)
        F_y = F * (dy / r)

        # X and y components of planet's acceleration
        acc_x = F_x / m
        acc_y = F_y / m

        # New x and y components of planet's velocity
        x_vel = planets[i][2] + acc_x * dt
        y_vel = planets[i][3] + acc_y * dt

        # New x and y components of planet's position
        x_pos = planets[i][0] + x_vel * dt
        y_pos = planets[i][1] + y_vel * dt

        # Updating x and y components of planet's position and velocity
        planets[i][0] = x_pos
        planets[i][1] = y_pos
        planets[i][2] = x_vel
        planets[i][3] = y_vel

    # Updating current simulation time
    t += dt

# For each planet, concatenate calculated final values to correct output format
# and print
for planet in planets:
    output_str = ''
    for attribute in planet:
        output_str += f'{attribute:0.4e} '
    output_str = output_str[:-1] # Strip trailing space from end of string
    print(output_str)
