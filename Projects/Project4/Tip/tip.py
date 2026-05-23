def tip():
    global tip_amt
    tip_input=input("Please add a tip (Optional, enter 0 or press Enter): ")
    tip_amt=int(tip_input) if tip_input.strip() else 0
    if tip_amt>0:
        print("Thank you for paying us a tip")
tip()