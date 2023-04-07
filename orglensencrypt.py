# define the function to encrypt a string with Caesar cipher
def caesar_encrypt(text, shift):
    result = ""
    # loop through each character in the text
    for char in text:
        # check if the character is an uppercase or lowercase letter
        if char.isupper():
            # shift the character by the given number of places
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

# read the input file and get the string to be encrypted
filename = "C:/Users/Kurnool Ramesh/Desktop/VS Code/OrglensCSV"
with open(filename, "r") as f:
    text = f.read()

# get the number of places to shift for Caesar cipher and encrypt the text
shift = int(input("Enter the number of places to shift for Caesar cipher: "))
caesar_encrypted = caesar_encrypt(text, shift)

# get the salt for XOR encryption
salt = input("Enter the salt for XOR encryption: ")

# encrypt the Caesar cipher text with XOR and write the result to the output file
output_filename = filename.split(".")[0] + "_enc.txt"
with open(output_filename, "w") as f:
    for i in range(len(caesar_encrypted)):
        encrypted_char = ord(caesar_encrypted[i]) ^ ord(salt[i % len(salt)])
        f.write(chr(encrypted_char))
