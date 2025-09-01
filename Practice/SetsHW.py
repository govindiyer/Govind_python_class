# Return only unique even numbers 
# Count number of even and odd (unique)
# Find how many different elements in two lists --
# Give the list of numbers (unique) which are there 
# Find if all the characters in a string are different 
# Find if all the digits in a number are diffrent
#1--
l=[1,3,4,5,4]
def values(l):
    s=set()
    for i in l:
        
        if i not in s:
            s.add(i)
            
        else:
            continue
        
        if i%2==0:
            return i
        
    
    
print(values(l))


