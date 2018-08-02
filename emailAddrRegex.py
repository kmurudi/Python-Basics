import re

str = input('Enter email ID: ')
# Pattern 1 to match  -> xxxx@XXXX.com
# Pattern 2 to match -> xxxx@XXXX.edu

matchObj1 = re.match(r'^[a-z][a-z0-9_]*[@][a-z]+.com', str)
matchObj2 = re.match(r'^[a-z][a-z0-9_]*[@][a-z]+.edu', str)
if matchObj1:
    print("Yes, this is a commercial domain email ID!")
elif matchObj2:
    print("Yes, this is a educational org email ID!")
else:
    print("NOT A VALID EMAIL ID!")


