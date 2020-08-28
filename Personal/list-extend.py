lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["mochi", "bori", "ally", "ally", "brandon", "max"]

# individual append
friends.append("Creed")
print(friends)

# to add into middle
friends.insert(1, "Kelly") # adding kelly to the index 1 and shift everything else

# to remove
friends.remove("Creed")

# to pop an last item
friends.pop()

# to check if value is in the list
print(friends.index("ally"))

# to sort the list
friends.sort()
print("this is after sorted ")
print(friends)

# to reverse
friends.reverse()

# to copy a list
friends2 = friends.copy()
print("this is from friends2 ")
print(friends2)
# extend append list to another list
friends.extend(lucky_numbers)
print(friends)

# show how many time this item is showing
print(friends.count("ally"))

# to get rid off everything
friends.clear()
print(friends)

