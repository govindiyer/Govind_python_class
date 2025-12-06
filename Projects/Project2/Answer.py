"""ANS:"""
menu={1:["Paneer Tikka",150],2:["Nachos",200],3:["Spring Roll",70],4:["Parata with Paneer Sabji",500,"for 2 pieces"],5:["Pizza and Pasta",500,"per plate(Large)"],6:["Noddles with French Fries",750,"per plate(Extra large)"]} 
def menu1():
    print(menu)
def billsplitter(menu):
    print("Welcome to the Restraunt in the jungle")
    print("Here is the menu")
    menu1()
    orderlist=[]
    people=int(input("How many people do you have(Between 2 to 10):  "))
    order=int(input("What would you prefer,1 (common order) or 2(individual order)?:Enter your choice:     "))
    if order==1:
        choice=int(input("What dish does your group/team want?:  "))
        orderlist.append(menu[order])
    elif order==2:
        menulist=[]
        for numofppl in range(people):
            ordernumber=int(input("Enter the menu number for your choice:  "))
            menulist.append(menu[ordernumber])
        print(menulist)     
    print(orderlist)
billsplitter(menu)
# def billamt():
#     print(sum())

