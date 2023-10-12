original = [8, 20, -10, 55, -777]

# Create a new list to store the modified values
modified = []

# Iterate through the original list and replace negative numbers with their absolute values
for num in original:
    modified.append(abs(num))

# Print the modified list
for num in modified:
    print(num)
