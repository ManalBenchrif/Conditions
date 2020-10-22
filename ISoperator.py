#Unlike the double equals operator "==", 
#the "is" operator does not match the values of the variables, but the instances themselves. For example:
# is Check if two objects are the same object:

#Definition and Usage
#The is keyword is used to test if two variables refer to the same object.
#The test returns True if the two objects are the same object.
#The test returns False if they are not the same object, even if the two objects are 100% equal.
#Use the == operator to test if two variables are equal.

x=[1,2,3]
y=[1,2,3]
print(x==y) #out put true because it match the value
print(x is y) #out put false it match the instance @
print("*********************")
x=y
print(x is y) #True because now x & y are the same object

print("*********************")# here problm?
z="manal"
k="manal"
print(z is k) #whyyyyy?
print(z==k)
