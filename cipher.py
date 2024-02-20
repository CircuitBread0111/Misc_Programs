#///////////////////////////|
#//|File: cipher.py
#//|Author: Jerrin C. Redmon
#//|Language: Python 3.11.4
#//|Version: 2.0
#//|Date: August 25, 2023
#///////////////////////////|

# Description:
# Simple Caesar cipher with encryption,
# decryption, and brute-force functions

#//----------------------------------------------------------------

# All usable characters in the cipher #
alphabet_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphabet_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']

# Main function 
def main():
    prompt1 = input("[CEASER CIPHER]: Encrypt Message[1]/Decrypt Message[2]: ")
    if prompt1 == '1':
        message = input("Input message: ")
        key = int(input("Input key shift number: "))
        print(encryption(message, key))
    elif prompt1 == '2':
        prompt2 = input("Would you like to Decrypt message[1] or Brute Force it[2]?")
        if prompt2 == '1':
            message = input("Input encrypted message: ")
            key = int(input("Input key shift number: "))
            print(decryption(message,key))
        elif prompt2 == '2':
            message = input("Input encrypted message: ")
            brute_force(message)


# Encrypt a given message with provided key
# @param message
# @param key
# @return encrypted_msg
def encryption(message, key):
    encrypted_msg = []
    for letter in message:
        if letter in alphabet_upper:
            letter_value = alphabet_upper.index(letter)
            encryption = (letter_value + key)%26
            outcome = alphabet_upper[encryption]
            encrypted_msg.append(outcome)
        elif letter in alphabet_lower:
            letter_value = alphabet_lower.index(letter)
            encryption = (letter_value + key)%26
            outcome = alphabet_lower[encryption]
            encrypted_msg.append(outcome)
        elif letter in numbers:
            letter_value = numbers.index(letter)
            encryption = (letter_value + key)%10
            outcome = numbers[encryption]
            encrypted_msg.append(outcome)
        else:
            encrypted_msg.append(letter)
    return "".join(encrypted_msg)


# Decrypt a given message with provided key
# @param message
# @param key
# @return decrypted_msg
def decryption(message,key):
    decrypted_msg = []
    for letter in message:
        if letter in alphabet_upper:
            letter_value = alphabet_upper.index(letter)
            decryption = (letter_value - key)%26
            outcome = alphabet_upper[decryption]
            decrypted_msg.append(outcome)
        elif letter in alphabet_lower:
            letter_value = alphabet_lower.index(letter)
            decryption = (letter_value - key)%26
            outcome = alphabet_lower[decryption]
            decrypted_msg.append(outcome)
        elif letter in numbers:
            letter_value = numbers.index(letter)
            decryption = (letter_value - key)%10
            outcome = numbers[decryption]
            decrypted_msg.append(outcome)
        else:
            decrypted_msg.append(letter)
    return "".join(decrypted_msg)


# Decrypt a given message with brute force
# @param message
def brute_force(message):
    for key in range(len(alphabet_upper)):
        possible_outcome = decryption(message, key)
        print(f"Key #{key}: {possible_outcome}")
        
# Program Execution #
main()
