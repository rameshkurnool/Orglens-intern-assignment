# get input number from user
num = int(input("Enter a number: "))

# set the 2 most significant bits to 1
result = num | 0b11000000

# print the result in decimal and binary format
print("Result in decimal: ", result)
print("Result in binary: ", bin(result))
