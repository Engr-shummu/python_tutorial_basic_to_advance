#string
#string= '', "", """ """
# strings are immutable 
s1="python"
print(id(s1)) # when u try to modify the value in same varieble it stores the in different locatiom

s1="java"
print(id(s1))

s2="python is a language"
#in python the string is an ordered list
#means it allows indexing and slicing
#indexing
print(s2[1])
print(s2[-2])

#slicing

print(s2[1:5])
print(s2[:7])
print(s2[7:])

#i want alternate character so use stride
print(s2[ : :2]) #iwant every 2nd character
print(s2[: :3]) # i want every 3rd character
print(s2[ : :-2]) #iwant every 2nd character from left side

# for loop on string

for value in s2:
	print(value)
