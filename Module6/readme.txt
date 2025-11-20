Name: Max McKie (mmckie2)

Module Info: Module 6 Assignment: Space Domain Awareness & Approximating Pi
                                  due on 10/04/2025 at 11:59 PM EST

Approach: 

sda.py - First itertools is imported and then the read_telemetry() function is
defined to accept a string 'file_name' as input. The file is opened in read only
mode and all the lines are stored in a variable called data using readlines().
A variable 'n_satellites' is read in from the first line of the file, and then
an empty list called 'all_satellites' is created to store the data contained in
the input file. Each line of the input is then parsed using
line.strip().split(',') and assigned to variables representing each satellite's
country of origin, altitude, and orbital velocity. The altitude and velocity are
casted to an int and float respectively, and a tuple of 
(country, altitude, velocity) is appended to 'all_satellites'. Once 
'n_satellites' lines of data have been parsed and added to the list then
'all_satellites' is returned. A second function called check_collisions() is
defined to accept the list returned by read_telemetry(). Inside this function, a
dict called 'collision_risks' is instantiated and all satellite countries are
added as keys with empty lists as the values by iterating over the input list.
Then, for each unique pair of satellites obtained by calling
itertools.combinations(satellites, 2), the country names of the first and second
satellites in the pair are obtained by indexing the 0th element of each tuple,
and then the altitudes are obtained by indexing the 1st element of each. If the
altitudes are not the same, then the satellites are not at risk of collision and
a continue statement skips to the next pair. Otherwise, the velocities are
accessed by indexing the 2nd element of each tuple, and if they are not the same
then each satellite is added to the other's list in 'collision_risks'. Once all
pairs of satellites have been iterated over, the function returns
'collsion_risks'. Lastly, the main() function is created, which is only executed
if this module is run as a script (or called externally). In main(), a list 
containing each of the two input files is instantiated and then a variable called
'file_num' is created to track which of these files is currently being processed.
For each input file, read_telemetry() is called and its output is assigned to a
variable called 'all_satellites'. This is then passed to check_collisions() and
the new output is assigned to a variable called 'collision_risks'. Once this is
obtained, an output string is formatted according to the assignment specifications.
First there is a header stating which simulation has been processed based on 
'file_num', and then for each country in 'collision_risks', if its list of
collision risks is empty, then an fstring will be concatenated to the output
string stating so. If its list of collision risks is not empty, then a different
fstring will be concatenated to the output string containing a list of all of its
collision risks. This output will then be written to a file, and if there are
still more files to process (determined by comparing 'file_num' to the length of
the list of input files), a newline will be added to the output string before
printing the output to terminal in order to provide a line of separation between
printed outputs in the terminal for each file. Finally, 'file_num' will be
incremented and this loop will repeat until all input files have been processed.

bbp.py - First the math module is imported and then recursive_pi() is defined
with type hints for an int input for 'n' and a float output. Four variables are
created to represent each term of the BBP series for readability, and then these
terms are composed with the leading factor to implement the formula for the nth
term of the BBP series. The value of the nth term contribution is calculated and
assigned to 'series_element' and is then printed in the required format using \t
to place a tab character between n and the current contribution.
Next there is an if statement that determines if there are more iterations left
or if n has reached the base case of zero. If n > 0, the series sum will be
recusively calculated as the contribution of the current term plus the
contribution of the n-1 case, which will accumulate for decreasing n until the
final contribution at n = 0 is returned and then all contributions can be summed
together. After this function, the main() function is defined. Inside main(),
the unicode escape sequence for lowercase pi is assigned to the variable
'pi_char'. A variable called 'pi' is assigned to the value of recursive_pi(10)
(i.e., the value of pi as calculated by the BBP series for n = 0 to 10), and
then the returned value is printed along with the value of pi given by the math
module in math.pi for comparison. At the bottom of the script, an if statement
checks the file's namespace so that the main() function is only executed when
this file is run as a script.

Known Bugs:
There are no known bugs.

Citations:
https://docs.python.org/3/library/itertools.html
https://www.rapidtables.com/code/text/unicode-characters.html