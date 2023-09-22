#for loops
# for [variable] in [iterabale datatype]:
# statement
# iterable datatypes: str, list, tuple, dictionsry. set

l=[10,20,30,40]
for value in l:
	print(value)

#sum= 0+10=10
#10+20=30
#30+40=70

l1=[20,30,40,50]
sum=0
for value in l1:
	sum=sum+value
	print(sum)

#range(50) so it will be 0-49
#range(0,100,5) it will be 0-99 divisible by 5 5,10...95
#range(10,90)  10,11,...89

#i want sum of value from 0 to 99
sum=0
for value in range(0,100):
    sum = sum+value

    print(sum)
