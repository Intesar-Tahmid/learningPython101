lucky_number = [89, 23, 65, 16, 77, 4]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Oscar", "Toby"]
print(friends)
friends.append("Creed")
# append adds new elements to the list
print(friends)
friends.extend(lucky_number)
# extend adds another list to the list left of the dot
print(friends)
friends.insert(1, "Kelly")
# this inserts a new element inside the list in the mentioned index number
# all the other elements gets pushed rightwards
print(friends)
friends.remove("Jim")
print(friends)
print(friends.index("Kevin"))
# this function above will output the index of the inputted string
print(friends.count("Oscar"))
# This function above counts the number of a specific element repeated in the list
lucky_number.sort()
# This function sorts the whole list. Literal sort. Not just printing
print(lucky_number)
lucky_number.reverse()
# This function reverses the whole list not just reverse print
print(lucky_number)
friends2 = friends.copy()
print(friends2)
# This is how to copy list to another list. This is not possible in C++. It's a great advantage
friends.clear()
print(friends)