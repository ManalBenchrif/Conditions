#Using "not" before a boolean expression inverts it:
print(False)
print(not False) #print out True
print(not True == False) #print out True

print('*********************************************')
list_name=["manal","salwa","rita"]
name=input("enter your name: ")
if name not in list_name:
    print (" %s not in" %name)