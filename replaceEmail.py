import re

str = input('Enter email ID: ')
# Pattern to match  -> xxxx@XXXX.com
# Task -> Change end of email, domains to ncsu.edu

matchObj1 = re.match(r'(^[a-z][a-z0-9_]*)[@]([a-z]+).(com)', str)
# Use of groups() function to obtain different parts of an email id to easily replace them
if matchObj1:
    print(matchObj1.group(1))
    # If you want to check the type of a variable
    #print(type(matchObj1.group(1)))
    newEmail = matchObj1.group(1)+'@ncsu.edu'
    print(newEmail)
else:
    print('Not a valid email ID!')