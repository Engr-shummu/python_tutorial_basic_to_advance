#python operators
#Arithmetic operators +,-,*,/,//,%,**

num1= 10
num2= 20
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2) #it gives float answer
print(num1//num2) # gives answer only in integers
print(num1%num2)

print(10 ** 2)#its a power operator

#comparison operators <,>,<=,>=,==,!=

num3=100
num4=50
print(num3==num4)
print(num3!=num4)
print(num3>num4)
print(num3<num4)

#identity operators (is is not) itthe memory location whereas comparison operators will compare thevalues

num5= 70
num6= 70

print(num5 == num6) #answer is true bcz integer values provide same memory location for 2 different variables having same values
print(num5 is num6) #answer is true bcz the memory is same

l=[10,20,30]
l2=[10,20,30]

print(l==l2) #answer is true bcz its comparing values
print(l is l2) #answer is false bcz its comparing the memory location but its list so it provides different memory locations
#assignment operators =, +=,-=,*=,/=

num7 = 100
num7 = num7 + 5
print(num7)
num7-=5
print(num7)

#bitwise operators &, |, << ,>>

num8 =1
num9 = 2
print(bin(num8), bin(num9))
print(num8 & num9) #performing and operation
print(num8 | num9) #performing or operation
print(num8>>1) #shift right  1 bit 
print(num9<<1) #shift left 1 bit

#logical operators "and" "or"  "not"

print(10==10 and 10==20) #and operators returns true when both condition is true
print(10==10 and 20==20)

print(10==20 or 10==10) #or operatos returns trues if any 1 is true
print(10==10 or 20==20)
print(20==30 or 40==50)

print(not(10==10)) #note operators give negation of answer
print(not(10==20))

#membership operator "in" "not in"
s = "python is language"
print("python" in s) #remember it is casesensitive
print("Python" in s)
print("Python" not in s)
print("python" not in s)

























