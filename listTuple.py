#LIst, tuple and dictionary (dict) in details.
#A list is a mutable datatype

myList = [0,1,2,3,4,5,6,7,8,9]
myList2 =[10,20,30,40,50]
osman = [100,[200]]
osman2 = [1000,[[2000,3000]]]
print(myList)


print (myList[5])
print (myList2[4])
print (myList2[-1])
print (osman[1][0])
print (osman2[1][0][1])
#Examlpe of a mutable list
osman.append(1000)
osman.pop()

fruits = ["oranges","pineapples"]
fruits.append ("apple")
fruits.pop()
print(osman)
print(osman)
print (fruits)
print (fruits)








#Tuples
#Tuples are immutable.

myTuple = (10,20,30,40,50)

#dictionary
#braces are identified using{},these are mutable

zebra = {"name":"tongs","legs":4,"color":"black & white","sex":"male"}
print(zebra.keys())
print(zebra)
zebra.__delitem__("name")
print(zebra)


