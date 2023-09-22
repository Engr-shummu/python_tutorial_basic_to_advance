#help(str) #provides all documentation of that method
#print (dir(str)) # all directory is shared
# format - it is a function for formattig the output

num1=100
num2=200
print("the value of num1 is",num1,"value of num2 is ",num2)
print ("the value of num1 is {} the value of num2 is {}".format(num1,num2))
print ("the value of num1 is {val1} the value of num2 is {val2}".format(val1=num1,val2=num2))
print ("the value of num1 is {0} the value of num2 is {1}".format(num1,num2))

# functipon capitalize

s="python is a language"
s1=s.capitalize() # remember strings are immutable u cannot mosidfy originial string u need to assign to another string even if u modify in same variable it will work but new capitalize string will be at diffenet location
print(s1) 

s2="python is a best language"
print(s2)
print(id(s2))
s2=s2.capitalize()
print(s2)
print(id(s2))
print(s2.upper())
print(s2.lower())
print(s2.title())
