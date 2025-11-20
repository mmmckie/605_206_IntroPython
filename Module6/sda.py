'''
This module iterates over a list of two input files of satellite data containing
country of origin, altitude, and velocity. It will then call read_telemetry() to
read these files and return the input data, then call check_collisions() to
determine if any two satellites are at risk of collision in orbit and return the
results. This output will then be written to one text file for each input file
as well as print the same information to the terminal.
'''

import itertools

def read_telemetry(file_name: str) -> list:
    '''Reads satellite telemetry data from an input file and returns a list
    containing tuples of each satellite's data.

    Arguments:
    file_name --> string path of input file containing satellite data.

    Returns:
    all_satellites --> list of tuples of type (str, int, float) containing the
                        the values (country, altitude, velocity) for each
                        satellite.
    '''
    with open(file_name, 'r') as f:
        data = f.readlines()

    # Number of satellites to read from file
    n_satellites = int(data[0].strip())
    
    # Store data for each satellite in list as tuples
    all_satellites = []
    for line in data[1:]:
        attributes = line.strip().split(',')

        country = attributes[0]
        altitude = int(attributes[1])
        velocity = float(attributes[2])

        all_satellites.append((country, altitude, velocity))

        # Keep going until all satellites have been processed
        if len(all_satellites) == n_satellites:
            break

    return all_satellites

def check_collisions(satellites: list) -> dict:
    '''Checks input satellite data for possible collision risks and returns a
    dict of all potential satellite collisions.
    
    Arguments:
    satellites --> list of tuples of type (str, int, float) containing the
                        the values (country, altitude, velocity) for each
                        satellite.
    
    Returns:
    collision_risks --> dict with str country names as keys and lists of str 
                        country names as values. Values are empty lists if the
                        satellite is not at risk of collision with others and
                        otherwise are populated with the country names of
                        satellites they are at risk of colliding with.
    '''
    collision_risks = {}
    for sat in satellites:
        collision_risks[sat[0]] = []
    
    # Iterate over all unique combinations of satellites
    for pair in itertools.combinations(satellites, 2):
        # First and second satellite in the pair
        sat_1 = pair[0]
        sat_2 = pair[1]

        # Each satellite's altitude
        alt_1 = sat_1[1]
        alt_2 = sat_2[1]

        # If different altitudes, not at risk of collision
        if alt_1 != alt_2:
            continue
        
        # Each satellite's velocity
        vel_1 = sat_1[2]
        vel_2 = sat_2[2]

        # If velocities are not the same, at risk of collision
        if vel_1 != vel_2:
            collision_risks[sat_1[0]].append(sat_2[0])
            collision_risks[sat_2[0]].append(sat_1[0])
    
    return collision_risks

def main():
    input_files = ['satellites1.txt', 'satellites2.txt']

    file_num = 1 # To track which file is currently being processed
    for file in input_files:
        # Read and process data
        all_satellites = read_telemetry(file)
        collision_risks = check_collisions(all_satellites)

        # Format output results
        output = f'##### Space Command Simulation {file_num} #####\n'
        for country in collision_risks:
            if len(collision_risks[country]) == 0:
                output += f'{country} is not at risk for a collision.\n'
            else:
                output += f'{country} is at risk of colliding with '\
                          + f'{collision_risks[country]}\n'
        
        output = output[:-1] # Strip final newline character

        # Write outputs to file
        alert_filename = f'satellites{file_num}_alerts.txt'
        with open(alert_filename, 'w') as f:
            f.write(output)
        
        # If there are more files left, add newline to separate printed outputs
        if file_num < len(input_files):
            output += '\n'

        # And print current output to terminal 
        print(output)

        file_num += 1

if __name__ == '__main__':
    main()