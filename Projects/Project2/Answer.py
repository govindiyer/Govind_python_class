"""ANS:"""
menu={1:["Paneer Tikka",150],2:["Nachos",200],3:["Spring Roll",70],4:["Parata with Paneer Sabji",500,"for 2 pieces"],5:["Pizza and Pasta",500,"per plate(Large)"],6:["Noddles with French Fries",750,"per plate(Extra large)"]} 
def menu1():
    print(menu)
def billsplitter(menu):
    # global people
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
    tax1=(15/100)*totalbill
    print(f"The amount of tax is {tax1}")
tax()
def totalwithouttax():
    global pricewithouttax
    pricewithouttax=totalbill+tax1
    print(f"Price with tax is {pricewithouttax}")
totalwithouttax()
def tip():
    global choice
    choice=int(input("We would greatly appreciate you if you can give us a small tip.It is OK is you don't give us:Please give the tip price over here :  "))
    print(f"The tip amount is",choice)
    print("Total price is",totalbill)
    print("Thank you very much.If you have a problem with us, please tell us.We will try our best to fix it")
tip()

    

    


        

    
        
    

