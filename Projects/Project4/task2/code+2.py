import Tax
import Tip,Bill_amt,Bill_generator
count_people=0
names_list=[]
total_food=0
tip_amt=0
total_price=0

def people_count():
    global count_people
    import sys
    count_people=int(input("How many people are there?: "))
    if count_people<2 or count_people>10:
        print("Sorry, We don't cater with",count_people,"person/people")
        sys.exit()
    else:
        print("Welcome to our restaurant, hope you have a good time with us")
people_count()

def people_name():
    global names_list
    names_list=[]
    for i in range(count_people):
        name=input("Enter your name: ")
        names_list.append(name)
    print("These are the names of you people:",names_list)
people_name()

def mode_and_total_price():
    global total_food
    global choice
    import sys
    menu = {
        1: ("Pizza", 350),
        2: ("Pasta", 300),
        3: ("Naan + Sabji", 500),
        4: ("Paneer Tikka", 250)
    }
    choice_mode=int(input("Enter your mode of order: 1) Individual, 2) Group: "))
    total_food=0
    if choice_mode==1:
        print("You have selected individual order!")
        for person in names_list:
            choice=int(input(f"{person}, choose item (1-4): "))
            if choice in menu:
                item,price=menu[choice]
                print(f"{person} ordered: {item}-Rs.{price}")
                total_food+=price
            else:
                print("Invalid choice")
                sys.exit()
    elif choice_mode==2:
        choice=int(input("Enter item for group (1-4): "))
        if choice in menu:
            item,price=menu[choice]
            print(f"Group ordered: {item}-Rs.{price}")
            total_food=price*count_people
        else:
            print("Invalid choice")
            sys.exit()
    else:
        print("Invalid mode")
        sys.exit()
    print("Total Amount: Rs.", total_food)
mode_and_total_price()

print("Tax amount: ",Tax.tax())
print("Tip amount: ",Tip.tip())
print("Total_Price: ",Bill_amt.bill_amt())
print("Bill: ",Bill_generator.bill())


def thank_you_note():
    print("Thank you for paying us a visit, we hope that you come back in the future.")
    print("Hope you have a good day ahead.")
thank_you_note()
