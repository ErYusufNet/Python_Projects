letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)
def encrypt(plain_text, key):
    ciphertext = ""
    for letter in plain_text:
        letter = letter.lower()
        if not letter == " ":
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= 26:
                    new_index -= 26
                ciphertext += letters[new_index]
def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == " ":
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index + key
                if new_index >= 26:
                    new_index -= 26
                plaintext += letters[new_index]




print("***CAESAR CIPHER PROGRAM***")
print('do you want to encrypt or decrypt?')


user_input = input("e/d: ").lower()
if user_input == 'e':
    print("Encryption mode selected")
    print()
    key = int(input("Enter a key to encrypt(1 through 26: "))
    text = input("Enter a message to encrypt: ")
elif user_input == 'd':
    print("Decryption mode selected")
    print()
    key = int(input("Enter a key (1 through 26: "))
    text = input("Enter a message to decrypt: ")
