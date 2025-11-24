import add , sub , mul , div
print("Welcome to Calculator:")
firstNum = int(input("Enter the first number : "))
secondNum = int(input("Enter the second number : "))

print("What do operation you want to preform : 1. Add 2. Sub 3.Mul 4.Div ")
choice = int(input("Enter your choice: "))

if choice == 1:
    print(add.add(firstNum,secondNum))
elif choice ==2:
    print(sub.sub(firstNum,secondNum))
elif choice ==3:
    print(mul.mul(firstNum,secondNum))
elif choice==4:
    print(div.div(firstNum,secondNum))
else:
    exit()
