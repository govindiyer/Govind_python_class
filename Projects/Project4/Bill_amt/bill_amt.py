def total_bill():
    global total_price,total_food,tax_amt,tip_amt
    total_price=total_food+(total_food*tax_amt)+tip_amt 
    print("The total price of the food is:",total_price)
total_bill()