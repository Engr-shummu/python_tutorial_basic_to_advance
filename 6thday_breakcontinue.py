# enumerate
# break
#continue
# for elsepass

# l=[10,20,30,40]
# key=300
# for value in l:
#     if value == key:
#          print("element found")
#          break # break will terminate the for loops and it will return all statement outide for loop
#     else:
#     	continue
# else:
# 	print("element not found") 

# print('element after for loop')

#if u want to get index numbers too use enumerate 
#for ondex, value in enumerate(l)
 #   print(index, value)

# l=[10,20,30,40]
# key=30
# for index,value in enumerate(l):
#     if value == key:
#          print("element found",index)
#          break # break will terminate the for loops and it will return all statement outide for loop
#     else:
#     	continue # remeber if u r writing in continue its unreachable 
# else:
# 	print("element not found") 

# print('element after for loop')

# l=[10,20,30,40]
# key=30
# for index,value in enumerate(l):
#     if value == key:
#          print("element found",index)
#          break # break will terminate the for loops and it will return all statement outide for loop
#     else:
#     	continue # remeber if u r writing in continue its unreachable 
# else:
# 	pass
# 	print("element not found") 

# print('element after for loop')

l=[10,20,30,40]
key=300
for index,value in enumerate(l):
    if value == key:
         print("element found",index)
         break # break will terminate the for loops and it will return all statement outide for loop
    else:
    	pass  #pass will be shown when no function is executed
    	print("pass block")
else:

	print("element not found") 

print('element after for loop')



