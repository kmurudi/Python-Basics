import re

input_num = input("ENTER STRING: ")
# creating a match object for phone number
# pattern 1 -> xxx-xxx-xxxx
# pattern 2 - (xxx)-xxx-xxxx

matchObj1 = re.match(r'[0-9]{3}-[0-9]{3}-[0-9]{4}', input_num)
matchObj2 = re.match(r'[(][0-9]{3}[)]-[0-9]{3}-[0-9]{4}', input_num)
if matchObj1:
    print("This phone number is of pattern 1!")
elif matchObj2:
    print("This phone number is of pattern 2!")
else:
    print("Not a valid phone number!")

