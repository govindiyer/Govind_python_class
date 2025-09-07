##Tuples##
#creating a tuple
t=(1,2,3,4,5,6,7,8,9,0)
t1=(1,)
#Properties
#Always has a comma after the first element
#Index based
#oredered
#Immutable-Cant change/update elements
#in (Curved brackets)
#Duplicates are allowed
#Adding elements
t2=list(t)
t2.insert(5,"Hello")
t=tuple(t2)
print(t)
#Removing elements
t3=list(t)
t3.remove("Hello")
t=tuple(t3)
print(t)
#Updating elements
t4=t[0:]
t5=t[:10]
t6=t[0:10]
print(t4,t5,t6,t)
#Deleating
t7=list(t6)
del t7[4]
t6=tuple(t7)
print(t6)
