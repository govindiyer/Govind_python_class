# 
#         *                 #1
#       *   *               #2 --- 2*2 2*3 
#     *       *             #3 --- 3
#   *           *           #4 
# * * * * * * * * *         #5
# 1 2 3 4 5 6 7 8 9 

# 2    8 
# 3    7 
# 4    6 


# 2*4
# 1 row -- 1 * -- 7 Spaces
# 2      -- 2  - 6 
# 3         2     -5
#  
rows = 5
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ", end=" ")

    for k in range(2*i-1):
        if k==0 or i==rows or k== 2*i-2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



# Sqaure Pattern -- 

for i in range(6):
    for j in range(6):
        print("*", end=" ")
    print()

# * * * * * * 
# *         *
# *         *
# *         *
# *         * 
# * * * * * * 
rows =6
for i in range(6):
    for j in range(6):
        if i==0 or i==rows-1 or j==0 or j==rows-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()   
