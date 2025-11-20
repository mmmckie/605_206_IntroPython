Name: Max McKie (mmckie2)

Module Info: Module 5 Assignment: K-Means Clustering due on 09/28/2025 at 11:59 PM EST

Approach: 

kmeans.py - First the 'math' module is imported and a list of the input files is
created. A for loop opens to wrap the rest of the script so that all
subsequent operations are applied to each of the 2 input files. For each file,
the file is opened as 'f' in read only mode with utf-8 encoding specified. Then
3 calls to f.readline().strip() are made to pull the first 3 lines of the file
in succession and remove the newline character from each. These values are all
casted to int in-line and assigned to the variables 'max_iterations',
'num_patients', and 'num_clusters', respectively. An empty list is created to
store all of the patient data contained in the file. To populate this list, the
next line of the file is read with another call to f.readline().strip() and a
while loop is then opened that will only close once f.readline() returns an
empty string, which denotes the end of the file. Inside the while loop,
next_line.split(',') is called to return a list of length 2 containing the
current patient's data as [x, y]. Each of these values is then casted to an int,
and a list containing [x, y] as ints is appended to 'all_patients'. 'next_line'
is then reassigned using another call to f.readline().strip(), and this process
repeats until all of the data has been read and stored. The file is then closed
using f.close() to free up memory.

A list of the initial centroids is created using the first k patients of the
input data, and two dictionaries, 'clusters' and 'previous_cluster_sizes', are
created with the index of each cluster as the keys and empty lists as the values.
These are to store the populations of patients in each cluster and the sizes of
each cluster after each iteration. A for loop is created to run from 0 to
'max_iterations', and the k-Means clustering algorithm is run for each iteration.
Each iteration consists of a for loop that iterates over all patients not
including the initial k infected patients. For each of these patients, a
'min_dist' variable is instantiated to math.inf and a 'closest_centroid' variable
is instantiated to None. Then, for each of the k centroids, the Euclidean
distance from the current patient to that centroid will be computed, and
'min_dist' and 'closest_cluster' are updated with the values of the current
distance and centroid if and only if the new distance is less than the current
value of 'min_dist', which is always the case for at least the first centroid
considered. Once all centroids have been iterated over and the closest has been
found, the index of that centroid's cluster will be assigned to the
'which_cluster' variable, and the patient will be added to the list of that
cluster's members by calling 'clusters[which_cluster].append(patient)'.

Once all patients have been added to their respective clusters, a for loop over
all clusters will check if any cluster sizes have changed since the last iteration
to set a break condition. Just before this loop, a boolean variable 'break_loop'
is instantiated to True. If none of the cluster sizes have changed, then this
variable will trigger a break condition to stop the outer loop early before
'max_iterations' have been reached. To check if the cluster sizes have changed,
the new size of each cluster is saved as the length of the list of the cluster's
members and then appended to the corresponding list in 'previous_cluster_sizes'.
The 'break_loop' variable is then set to False conditionally based on 1 of 2
conditions in an or statement - (1) if it is the first iteration, since we must
have completed at least 1 prior iteration to have any cluster size history, or
(2) the new size of any cluster is different from the last iteration.

After this loop over the clusters, there will be an if statement to decide
whether to break the outer loop based on the value of 'break_loop'. If
'break_loop' was set to False for any of the clusters, then all clusters will be
iterated over again to get the new centroid values. This is done by adding all
of the x-values for each patient in the cluster and dividing by the size of the
cluster to get the x-value of the centroid, and likewise for the y-value. Each
centroid's previous value will be overwritten by assigning the element of the
'centroids' list at that cluster's index with the list [new_x_mean, new_y_mean],
and the list of the cluster's members in the 'clusters' dict will be emptied
with the clear() function.  Once this has been completed for each cluster,
'iterations_executed' will be set to i+1 (to account for 0-indexing) to track
how many iterations have been completed for the current input file.

Once either 'max_iterations' have executed or 'break_loop' has stopped the loop
early, a series of print statements will print information about the initial
patients, final centroids, and the size and members of each cluster as output.
This whole process will then repeat until it has been completed for all files in
the 'input_files' list.

Known Bugs:
There are no known bugs.

Citations:
None