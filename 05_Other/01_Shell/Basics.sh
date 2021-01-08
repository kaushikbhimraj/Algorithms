
#!bin/bash

# GLOBAL VARIABLE
# export global_temp
# global_temp = "Hello World"
# echo $global_temp

# LOCAL VARIABLE
# Initializing and declaring the varible
echo $temp
temp="Hello World"
echo $temp

# Removing the variable
unset global_temp
unset temp

# date give yo the date and time 
# who shows all the users currently logged on to the system.
date
echo "Current users that are logged on:"
who
