'''
This script will iterate through a list of text files containing COVID patient
data of the format:

----- input_file.txt -----
<max number of iterations>
<total number of patients>
<total number of clusters>
<patient 1 data>
...
<patient N data>
--------------------------

For each input file, this script will load the parameters/data and run a k-means
clustering algorithm to estimate which patients were infected from each of the
first k patients listed in the input file.

The k-means algorithm will run until either the sizes of each cluster do not
change, or the max number of iterations has been reached. The history of all
cluster sizes will be tracked in 'previous_cluster_sizes'. During each iteration,
the new centroids will be determined by taking the x_mean and y_mean of each
cluster, and then the clusters will be cleared to make way for the next
iteration.

Once the loop terminates, the initial patients, total number of iterations
executed, final centroid coordinates, number of patients in each cluster, and
the members of each final cluster will be printed as output.

This process will repeat until all input files have been processed.
'''

import math

input_files = ['points1.txt', 'points2.txt']

for file in input_files:
    # Open input file to read data
    f = open(file, 'r', encoding = 'utf-8')

    # Max number of iterations, number of patients, and number of clusters are
    # the first 3 lines of data in each input file
    max_iterations = int(f.readline().strip())
    num_patients = int(f.readline().strip())
    num_clusters = int(f.readline().strip())

    all_patients = [] # Empty list to store all of the patients' data

    # Grab next line containing patient data and continue doing so until there
    # are no more lines to read
    next_line = f.readline().strip()
    while next_line != '':
        coords = next_line.split(',')
        x_pos, y_pos = int(coords[0]), int(coords[1])
        all_patients.append([x_pos, y_pos])
        next_line = f.readline().strip()

    # Done reading from file, so close it
    f.close()

    # Initial centroids are the first k patients from input
    centroids = all_patients[:num_clusters]
    
    # Creating dictionaries to store each cluster's data points and cluster
    # sizes for each iteration
    clusters = {}
    previous_cluster_sizes = {}
    for idx in range(len(centroids)):
        clusters[idx] = []
        previous_cluster_sizes[idx] = []

    for i in range(max_iterations):

        # Iterate through all patients that were not the initial COVID patients
        for patient in all_patients[num_clusters:]:
            
            # Minimum distance from patient to any centroid and closest centroid
            # Initially set to infinity and None as placeholders
            min_dist = math.inf
            closest_centroid = None

            # For each cluster centroid...
            for centroid in centroids:
                # Calculate dx, dy, and Euclidean distance from the patient to
                # the current centroid
                dx = patient[0] - centroid[0]
                dy = patient[1] - centroid[1]
                dist = (dx**2 + dy**2)**(0.5)

                # If this is the closest centroid so far, update min_dist
                # and closest_centroid
                if dist < min_dist:
                    min_dist = dist
                    closest_centroid = centroid

            # Once done checking all centroids, add the patient data to closest
            # centroid's cluster
            which_cluster = centroids.index(closest_centroid)
            clusters[which_cluster].append(patient)
        
        # Check if any cluster sizes have changed. Create boolean variable for
        # break condition and check cluster sizes
        break_loop = True
        for cluster in clusters:

            # Get size of new cluster and add it to cluster sizes list
            new_cluster_size = len(clusters[cluster])
            previous_cluster_sizes[cluster].append(new_cluster_size)
            
            # Need to have at least 1 prior iteration to compare cluster sizes
            # If so, then break_loop is based on whether or not they have changed
            if i == 0 or new_cluster_size != previous_cluster_sizes[cluster][-2]:
                break_loop = False
        
        # If cluster sizes are the same, break loop to stop early
        # Else, compute new centroids and update the centroids list
        if break_loop:
            break
        else:
            for clust in clusters:
                cluster_x_sum = 0
                cluster_y_sum = 0

                for data in clusters[clust]:
                    cluster_x_sum += data[0]
                    cluster_y_sum += data[1]

                # New centroid x- and y-coords
                new_x_mean = cluster_x_sum / len(clusters[clust])
                new_y_mean = cluster_y_sum / len(clusters[clust])
                
                # Update centroid value and clear cluster for next iteration
                centroids[clust] = [new_x_mean, new_y_mean]
                clusters[clust].clear()

            # Setting number of iterations completed so far
            iterations_executed = i+1
    
    # Finally, print output info in desired format
    print(f'Initial COVID-19 Patients: {all_patients[:num_clusters]}')
    print('')
    print(f'Iterations to achieve stability: {iterations_executed}')
    print('')
    print('Final Centroids:')
    
    for centroid in centroids:
        print(centroid)

    for clust in clusters:
        print('')
        print(f'Number of patients in Cluster {clust}: {len(clusters[clust])}')
        print(clusters[clust])
    