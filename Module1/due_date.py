'''
This script will ask for a series of user inputs to construct
a date and time. It then concatenates those inputs into a Module 1 due date 
message in the format of:
"Module 1 Assignment is due on <MM>/<DD>/<YYYY> at <HH>:<MM>:<SS> PM EST"

For zero-padded format output, the user must enter
zero-padded format inputs (e.g., 05 instead of 5).

If the user enters non-padded inputs, the output will not be padded.
'''
month = input("Month: ")
day = input("Day: ")
year = input("Year: ")
hour = input("Hour: ")
minute = input("Minute: ")
second = input("Seconds: ")

output_str = 'Module 1 Assignment is due on ' \
              +month+'/'+day+'/'+year+' at ' \
              +hour+':'+minute+':'+second+' PM EST'

print(output_str)
