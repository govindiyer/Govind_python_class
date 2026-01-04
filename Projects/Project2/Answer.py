"""ANS"""
menu={1:["Paneer Tikka",150],2:["Nachos",200],3:["Spring Roll",70],4:["Parata with Paneer Sabji",500,"for 2 pieces"],5:["Pizza and Pasta",500,"per plate(Large)"],6:["Noddles with French Fries",750,"per plate(Extra large)"]}
def menu1():
    print(menu)
def billsplitter(menu):
    global people
    global orderlist
    global menulist
    global ordernumber
    global choice
    global order
    print("Welcome to the Restraunt in the jungle")
    print("Here is the menu")
    menu1()
    people=int(input("How many people do you have(Between 2 to 10):  "))
    print(f"The amount of people are {people}")
    order=int(input("What would you prefer,1 (common order) or 2(individual order)?:Enter your choice:     "))
    orderlist=[]
    if order==1:
        choice=int(input("What dish does your group/team want, Enter the menu number:  "))
        orderlist.append(menu[choice])
    elif order==2:
        menulist=[]
        for numofppl in range(people):
            ordernumber=int(input("Enter the menu number for your choice:  "))
            menulist.append(menu[ordernumber])
        print(menulist)
        orderlist.extend(menulist)     
    return orderlist
billsplitter(menu)
def billamt():
    global totalbill
    orderlist=billsplitter(menu)
    print(orderlist)
    totalbill=0
    for ordernumber in range(len(orderlist)):
        totalbill+=orderlist[ordernumber][1]
    print(f"The total bill without tax is {totalbill}")
billamt()
def tax():
    global tax1
    tax1=(5/100)*totalbill
    print(f"The amount of tax is {tax1}")
tax()
def totalwithouttax():
    global pricewithtax
    pricewithtax=totalbill+tax1
    print(f"Price with tax is {pricewithtax}")
totalwithouttax()
def tip():
    global choice1
    choice1=int(input("We would greatly appreciate you if you can give us a small tip.It is OK is you don't give us:Please give the tip price over here :  "))
    print("The tip amount is",choice1)
    print("Total price is",pricewithtax)
    global actualprice
    actualprice=pricewithtax+choice
    print("Total price with tip and tax is",actualprice)
    print("Thank you very much.If you have a problem with us, please tell us.We will try our best to fix it")
tip()
def splitter():
    global i
    for i in range(people):
        i=input("Enter your name:  ")
    split=int(input("Enter number 1 for an equal splitter and number 2 for a variable splitter:  "))
    if split==1:
        global price
        price=(actualprice/people)
        print("Each person owes rupees",price)
        print("Thanks, Please come again next time")
    elif split==2:
        global personshare
        global x
        print("Choice 2")
        spllit=[]
        for j in range(people):
            j=int(input("What percentage each person should spend:  "))
            spllit.append(j)
        print(spllit)
        total=sum(spllit)
        if total==100:
                for personshare in range(len(spllit)):
                    print(spllit[personshare])
                    x=(spllit[personshare]/100)*pricewithtax
                    print(x,"Thanks, Please come again next time")
        else:
            print("NOT OK, add or remove numbers to make the sum 100")    
    print("Saving To FILE")
    fileadding()
def fileadding():
    try:
        file = open('Bill_Split.txt', 'a')
        file.write(str(actualprice))
        file.write(str(price))
        file.write(str(people))
        file.write(str(orderlist))
        file.write(str(menulist))
        file.write(str(order))
        file.write(str(ordernumber))
        file.write(str(choice))
        file.write(str(choice1))
        file.write(str(tax1))
        file.write(str(personshare))
        file.write(str(x))
        file.close()
        print("Append mode completed successfully.")
    except Exception as e:
        print("Append error:", e)
splitter()
























































































































