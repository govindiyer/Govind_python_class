import sys
import Tax
import Tip
import Bill_amt
import Bill_generator

count_people=0
names_list=[]
total_food=0

def people_count():
    global count_people
    try:
        count_people = int(input("How many people are there?: "))
    except ValueError:
        print("Please enter a valid number.")
        sys.exit()
        
    if count_people<2 or count_people>10:
        print(f"Sorry, We don't cater to {count_people} person/people.")
        sys.exit()
    else:
        print("Welcome to our restaurant, hope you have a good time with us!")

def people_name():
    global names_list
    for _ in range(count_people):
        name=input("Enter your name: ")
        names_list.append(name)
    print("These are the names of the people in your party:", names_list)

def mode_and_total_price():
    global total_food
    menu = {
        1: ("Pizza", 350),
        2: ("Pasta", 300),
        3: ("Naan + Sabji", 500),
        4: ("Paneer Tikka", 250)
    }
    
    print("Menu: ",menu)
    for key,(item, price) in menu.items():
        print(f"{key}) {item}: Rs.{price}")
    
    try:
        choice_mode=int(input("Enter your mode of order: 1) Individual, 2) Group: "))
    except ValueError:
        print("Invalid input mode.")
        sys.exit()
        
    total_food=0
    
    if choice_mode==1:
        print("You have selected individual order!")
        for person in names_list:
            try:
                choice=int(input(f"{person}, choose item (1-4): "))
            except ValueError:
                print("Invalid input.")
                sys.exit()
                
            if choice in menu:
                item,price=menu[choice]
                print(f"{person} ordered: {item} - Rs.{price}")
                total_food+=price
            else:
                print("Invalid choice.")
                sys.exit()
                
    elif choice_mode==2:
        try:
            choice=int(input("Enter item for group (1-4): "))
        except ValueError:
            print("Invalid input.")
            sys.exit()
            
        if choice in menu:
            item,price=menu[choice]
            print(f"Group ordered:{item} - Rs.{price}")
            total_food=price*count_people
        else:
            print("Invalid choice.")
            sys.exit()
    else:
        print("Invalid mode.")
        sys.exit()
        
    print(f"Total Food Amount: Rs.{total_food}")

def thank_you_note():
    print("\nThank you for paying us a visit, we hope that you come back in the future.")
    print("Hope you have a good day ahead!")

people_count()
people_name()
mode_and_total_price()


tax_amount = Tax.tax(total_food)
tip_amount = Tip.tip(total_food)
final_bill = Bill_amt.bill_amt(total_food, tax_amount, tip_amount)

print("Tax amount: ", tax_amount)
print("Tip amount: ", tip_amount)
print("Total Price: ", final_bill)
print("Bill: ", Bill_generator.bill(names_list, total_food, tax_amount, tip_amount, final_bill))

thank_you_note()