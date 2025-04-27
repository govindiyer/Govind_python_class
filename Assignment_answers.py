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

