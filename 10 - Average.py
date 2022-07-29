first_name = input("First Name: ")
last_name = input("Last Name: ")
field_1 = int(input("Field 1: "))
field_2 = int(input("Field 2: "))
field_3 = int(input("Field 3: "))
average = (field_1 + field_2 + field_3) / 3
if average>=17:
    print("Great")
elif average>=12:
    print("Normal")
else:
    print("Fail")