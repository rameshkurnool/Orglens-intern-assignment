# get input amount from user
amount = int(input("Enter the amount: "))

# define the list of available denominations
denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

# initialize an empty list to store the counts of each denomination
counts = []

# loop through the denominations and find the count of each denomination
for d in denominations:
    count = amount // d
    counts.append(count)
    amount -= count * d

# print the results in a horizontal table format
print("Notes: ", end="")
for d in denominations:
    print("{:<5}".format(d), end="")
print()
print("Count: ", end="")
for c in counts:
    print("{:<5}".format(c), end="")
print()
