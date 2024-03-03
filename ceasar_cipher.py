import random

def alphabet():
    sv_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    indexed_alphabet = {char: index for index, char in enumerate(sv_alphabet)}
    # "indexed_alphabet" is a dictionary, where each "char" is a key, and its corresponding index "index" is the value
    # "index, char in enumerate(sv_alphabet)" is the loop that iterates over "sv_alphabet". In each iteration "index" represents the index of the character, and "char" represents the character itself
    return indexed_alphabet

def keyscanorgeninator(encrypt_input):

  alpha = alphabet()

  if "//" in encrypt_input:
# Checks if the message has // to see if there is a signature.
    name_key_list = encrypt_input.split("//")
    name_key = name_key_list[-1].lstrip()
# Puts message in list to split at //, then remove the last element which is the signature.
    key_amount = len(name_key)
# Checks how long the signature is
# These if and elif statements check if the signature has the corresponding length to the names. If not then it will be an invalid signature.
    if key_amount == 3:
      letter_shift = alpha[name_key[0].upper()]
# Checks the first letter of the signature to see which index it has on the "alphabet()".
      key = letter_shift - 1
# The encrypted index subtracted by the original name's first letter's index. This case we have Bob where B has the index of 1 in "alphabet()".
      if key == 0:
# If the message is not encrypted, so it has 0 shift. It will generate a random key shift for the message.
        key = random.randint(1, 28)
        return key
      return key
# Returns the key for the other function.      

    elif key_amount == 5:
      letter_shift = alpha[name_key[0].upper()]
      key = letter_shift - 0
      if key == 0:
        key = random.randint(1, 28)
        return key      
      return key
    
    elif key_amount == 6:
      letter_shift = alpha[name_key[0].upper()]
      key = letter_shift - 25
      if key == 0:
        key = random.randint(1, 28)
        return key      
      return key
    
    else:
       print("Invalid Signature, please try again")
       encrypt_inator()

# If the message does not have a signature(//) then it will check for a number at the end of the message.
  elif "//" not in encrypt_input:
    new_input = encrypt_input.split()
# Splits all characters from the message into a list.
    for word in new_input:
# Iterates each character to see if it is a digit. If it finds the digit that will be the key.
      if word.isdigit():
        key = int(word)
        return key
      
# If the message does not have a key or signature then it will make random.
    key = random.randint(1, 28)
    return key

def encrypt(msg, shift):
    alpha = alphabet()
    # A variable for the dictionary with the assigned index and char
    encrypted_msg = ""
    # Empty string for the message
    
    for char in msg:
        if char.isalpha():
            # Checks if the character is uppercase or lowercase
            uppercase = char.isupper()
            # Get the index of the character in the "alphabet()" dictionary
            char_index = alpha[char.upper()]
            
            # Performs the shift of the letters by determining the index (position).
            # Takes the current characters index from "alpha" and adds the shift. If it has shifted where the index is above 28 then the "%" module will make sure it stays within the range by checkin how much remainder.
            shifted_index = (char_index + shift) % len(alpha)
            # For example if "char_index = 28" and "shift = 2", that would mean "shifted_index = 30" which is outside the range of 28. So it will take 30 % 28 which will result in 2, and that is the final position "alpha".
            
            # Converts "alpha" into a list of index
            index_list = list(alpha.values())

            # Converts alpha into a list of characters
            char_list = list(alpha.keys())

            # Finds position of "shifted_index" in "index_list"
            index_position = index_list.index(shifted_index)

            # Get the new shifted character based on the new position
            shifted_char = char_list[index_position]
            
            # Checks if the original character was uppercase
            # If "uppercase" is true then it will add the uppercase, else it will make it lowercase
            encrypted_msg += shifted_char if uppercase else shifted_char.lower()
        else:
            # For all the characters not in "alpha", for example "," "." " ".
            encrypted_msg += char
    
    return encrypted_msg

def encrypt_inator():
  
  option = input("Encrypt or Decrypt?:")

  lowercase_option = option.lower()

  if lowercase_option == "encrypt":
    encrypt_input = input("Message:")
    key_shift = keyscanorgeninator(encrypt_input)
    encrypted_input = encrypt(encrypt_input, key_shift)
    print(f"Encrypted message: {encrypted_input}")
    print(f"Your key is: {key_shift}")
  
  elif lowercase_option == "decrypt":
    encrypted_input = input("Message:")
    key_shift = keyscanorgeninator(encrypted_input)
    decrypted_msg = encrypt(encrypted_input, -key_shift)
    print("Decrypted message:", decrypted_msg)
  
  else:
     print("Write encrypt or decrypt. Thank you!")
     encrypt_inator()

encrypt_inator()