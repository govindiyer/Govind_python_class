import Tax, Tip, Bill_amt


def bill_generator():
    print("Bill: order 23957: Restaurant order")
    # print("Total price (without tax or tip):",total_food)
    print("Tax amount:",Tax.total_food*Tax.tax_amt)
    print("Tip amount:",Tip.tip_amt)
    print("Total price (with tax and tip):",Bill_amt.total_price)
bill_generator()
