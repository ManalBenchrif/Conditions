#The "in" operator is used to check if a specified object exists within an iterable object container (expl :a list)

name=input("enter your name: ")
list_name=['manal','asmae','mouna']
if name in list_name:
    print("^_^ your name exist in: ",list_name)
else:
    print("!!! your name doesn't exist in %s" %list_name)

