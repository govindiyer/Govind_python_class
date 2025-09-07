# 16. Write a program that finds the maximum and minimum values in a list.
# 17. Create a program that removes duplicates from a list.
# 18. Develop a program that sorts a list in ascending order without using the built-in sort function.
# 19. Write a program that merges two lists into one.
# 20. Create a program that checks if a list is a subset of another list.
# 21. Given a list of numbers, write a program to print all elements that are less than 5.
# 22. Given an integer, write a program to find and print all of its divisors.
# 23. Given two lists, write a program to return a new list containing only the elements common to both (without duplicates).
# 24. Write a one-line list comprehension that, given a list of numbers, produces a new list of only the even numbers.
# 25. Write a program (function) that takes a list and returns a new list with all duplicate elements removed.


#16--
"""
l=[7,8,6,5,4,5,3,4,6,1,4,7,9,10,22,345,3,567,647,1,0]
print(max(l))
print(min(l))
"""


#17--
"""


def remove_duplicates_set(input_list):

    return list(set(input_list))


my_list = [1, 2, 2, 3, 4, 3, 5]
unique_list = remove_duplicates_set(my_list)
print(f"Original list: {my_list}")
print(f"List after removing duplicates (using set): {unique_list}")
"""



#18--
"""

def bubble_sort(input_list):
    n = len(input_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted list:", my_list)
"""



#19--
"""
l=[1,2,3,5,4,543]
l1=[1,2,6,5,4,3,2,1]
l=l+l1
print(l)
"""



#20--
"""
i = [1, 2, 3]
x = [1, 2, 3, 4, 5]
is_subset = set(i).issubset(x)
print(is_subset)
"""



#21--
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i <= 5:
        print(i)
"""



#22--
"""
n=int(input("Enter a number:  "))
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
print(l)
"""



#23--
"""

"""



#23--
"""

"""



#24--
"""

"""



#25--
"""

"""