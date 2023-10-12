# Creating a list 'list1' containing a mix of string and integer elements
list1 = ['physics', 'chemistry', 1997, 2000]

# Creating another list 'list2' containing integer elements
list2 = [1, 2, 3, 4, 5, 6, 7]

# Accessing and printing elements in 'list1' and 'list2'
# Printing the first element of 'list1' using indexing (index 0)
print("list1[0]:", list1[0])

# Printing a slice of 'list2' from index 1 to 4 (elements at indices 1, 2, and 3)
print("list2[1:5]:", list2[1:5])

# Updating elements in 'list1'
# Printing the value at index 2 in 'list1'
print("Value available at index 2:")
print(list1[2])

# Changing the value at index 2 of 'list1' to 2001
list1[2] = 2001
# Printing the updated value at index 2
print("New value available at index 2:")
print(list1[2])

# Adding an element to 'list1'
# Appending the integer 2020 to the end of 'list1'
list1.append(2020)
# Printing the updated 'list1' after appending
print("New List:", list1)

# Inserting an element into 'list1'
# Inserting the string 'Python' at the beginning (index 0) of 'list1'
list1.insert(0, 'Python')
# Printing 'list1' after the insertion
print("After inserting:", list1)
