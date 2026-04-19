#Code for Leap Year

# l=int(input("Enter a Year:  "))

# if l%100==0 and l%400==0:
#     print("Leap Year")
# elif l%4==0:
#     print("Not a leap year")
# else:
#     print("Not a leap year")

# def fizzbuzz(n):
#     l=[]
#     for i in range(1,n+1):
#         if i%3==0 and i%5==0:
#             l.append(i)
#             print("Fizz Buzz")
#         elif i%3==0:
#             l.append(i)
#             print("Fizz")
#         elif i%5==0:
#             l.append(i)
#             print("Buzz")
#         else:
#             l.append(i)
#             print(i)
# fizzbuzz(20)
            
#Create code where u wanna reverse list

# def reverse_list():
#     a=[]
#     for i in range(5):
#         b=input("Enter a value: ")
#         a.append(b)
#     g=[]
#     for b in a:
#         c=""
#         for d in b:
#             c=d+c
#         g.append(c)
#     e=[]
#     for f in range(len(g)-1,-1,-1):
#         e.append(g[f])
#     print(e)
# reverse_list()

#Create a code that checks for a palindrome

def Palindrome():
    word=str(input("Enter a word: "))
    reversed_word=""
    for i in word:
        reversed_word=i+reversed_word
    print(reversed_word)
    palindrome=True
    for i in range(len(word)):
        if word[i]!=reversed_word[i]:
            palindrome=False
            break
    if palindrome==True:
        print(word,"is a palindrome.")
    else:
        print(word,"is not a palindrome.")
Palindrome()