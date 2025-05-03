#1
"""
Story:
Amara, a curator at the Grand History Museum, is arranging artifacts for a new exhibit. She starts with a collection of items: "Vase", "Statue", and "Coin". She wants to add "Tablet" to the end of her arrangement, place "Mask" at the beginning, and organize the items alphabetically for the exhibit catalog.

Task:
Start with the collection "Vase", "Statue", "Coin", add "Tablet" to the end, place "Mask" at the beginning, and sort the collection alphabetically. Print the final arrangement.

"""



list=["Vase","Statue","Coin"]
list.append("Tablet")
list.insert(0,"Mask")
list.sort()
print (list)

#2
#Story:
# Jamil, a fruit vendor in the Sunrise Market, has two crates of fruits: one containing "Mango", "Apple", "Banana" and another with "Banana", "Orange", "Kiwi". He needs to create a single 
# collection of all unique fruits available for sale and add "Lemon" to it for his next order.
# Task:
# Take two collections "Mango", "Apple", "Banana" and "Banana", "Orange", "Kiwi", combine them into a single collection of unique items, add "Lemon", and print the resulting collection.

Tuple1 ={"Apple, "  
         "Mango, " 
         "Banana, "
}
Tuple2 ={"Banana, " 
         "Orange, " 
         "Kiwi, " 
}
Tuple1.add("Lemon")

print(Tuple1|Tuple2)

#3
"""
Lila, a tour guide in Wanderlust City, keeps a record of stops on her tour: "Museum", "Park", "Museum", "Bridge". For her tour report, she needs to find the position of the first "Museum"
stop and count how many times "Museum" appears in the sequence.
Task:
Use the sequence "Museum", "Park", "Museum", "Bridge", find the position of the first "Museum", count the occurrences of "Museum", and print both values.
"""
#1 part 
mylist=["Museum","Park","Museum","Bridge"]
print(mylist.count("Museum"))
#2 part
mylist.sort
print(mylist[0])


#4
"""
Kiran, a trader in the Silk Road Bazaar, maintains a ledger of goods: "Cloth" with a quantity of 100 and "Spice" with 50. A new shipment updates the ledger with "Spice" at 75 and adds "Jewelry" 
with 20. Kiran needs to combine the old and new ledgers (with new quantities taking precedence) and check the quantity of "Spice" for his sales log.

Task:
Start with a ledger of "Cloth": 100, "Spice": 50, combine it with a new ledger of "Spice": 75, "Jewelry": 20, get the quantity of "Spice", and print it.
"""
mydict={
    "Cloth":100,
    "Spice":50,
}
mydict.update({"Spice": 75})
mydict.update({"Jewelry":20})
mydict.get("Spice")
print(mydict)

#5

"""

Zara, a wedding planner, has two guest registries: one with "Sophia", "James", "Lily" and another with "James", "Ethan", "Mia". She needs to create a single, alphabetically organized collection
of all unique guests to finalize the seating chart.
Take two collections "Sophia", "James", "Lily" and "James", "Ethan", "Mia", combine them into a single collection of unique items, sort it alphabetically, and print the result.
"""
List1=["Sophia","James","Lily"]
List2=["Ethan","James","Mia"]
List3=(List1+List2)
List3.sort()
print(List3)
#6

"""
Omar, a librarian at the Eternal Library, keeps a catalog of books: "Novel" published in 1920 and "Poetry" in 1850. For a digital archive, he needs to convert the catalog into a fixed 
sequence of entries and retrieve the first entry for a library newsletter.

Task:
Start with a catalog of "Novel": 1920, "Poetry": 1850, convert it into a fixed sequence of entries, extract the first entry, and print it.
"""
dicad={
    "Novel":1920,
    "Poetry":1850
}
print(set(dicad))






