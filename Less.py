def division():
    try:
        a = int(input("Enter first number :"))
        b = int(input("Enter second number : "))
        result = a/b 
        print("result",result)
    except (ValueError,ZeroDivisionError) as err:
        print("Error: ", err)

division()