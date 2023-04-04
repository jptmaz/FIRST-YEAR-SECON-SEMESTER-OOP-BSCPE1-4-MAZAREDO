#Jasmin Paige T. Mazaredo - OOP Assignment no. 2 (B.)

# Create a  program that will accept encrypted text and the program will decrypt it using the given character substitute

# Ask the user for the encrypted text

print("Hello! What shall we decrypt today?")
encrypted_text = input("Enter the message to be decrypted: ")

# Decrypt it using the program

decrypted_text = encrypted_text.replace("*", "a").replace("&","e").replace("#", "i").replace("+", "o").replace("!", "u")

# Print the output

print("Your encrypted text was " + encrypted_text)
print("The decrypted message is " + decrypted_text)