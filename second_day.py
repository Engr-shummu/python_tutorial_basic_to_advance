#datatypes:
# intergers, string and float are immutable datatypes
num1 = 100
print(type(num1))
num2 = 200.2
print(type(num2))
s = "python"
t = 'djangp'
print(id(s),id(t))

#list datatypes are mutable means python allow adding, updtae and deletion at same memory location

l = [20,30,40,50,'python',"django"]
print(id(l))
#append allows adding 1 element

l.append(60)

print(l)

#tuple is immutable its likelist but its immutable the only difference you cannot edit 
tuplee= (10,30,70)

 #dictionary: its called hashmap we will provide keys and value pairs its mutable data types


d= {"name":"shumaila", "email":"shummukhan8@gmail.com"}

 #set can be used for set operations like union and all

set = {10,20,30,40}

print(set)

 #boolean has two values True False

