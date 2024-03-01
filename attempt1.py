import random

alpha = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "å": 27,
    "ä": 28,
    "ö": 29,    
  }  

nums = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "z",
    27: "å",
    28: "ä",
    29: "ö"    
  }    

def keyscanorgeninator(user_input):

  if "//" in user_input:
    name_key_list = user_input.split("//")
    name_key = name_key_list[-1]
    key_amount = len(name_key.lstrip())

    return key_amount

  elif "//" not in user_input:
    new_input = user_input.split()
    for word in new_input:
      
      if word.isdigit():
        key = int(word)
        return key
      
    key = random.randint(1, 29)
    return key

user_input = input(":")

result_key = 5

def encrypt(result_key, user_input):

  print(f"{user_input} input")
  print(f"{result_key} key")
  
  key = int(result_key)

  alpha = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "å": 27,
    "ä": 28,
    "ö": 29,    
  }  

  nums = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "z",
    27: "å",
    28: "ä",
    29: "ö"    
  }    

  sentence = []

  for letter in user_input:

    print(letter)

    if letter.isupper():
      
      
    elif letter.islower():
      bokstav = alpha[letter]
      sentence.append(bokstav)      

    elif letter.isspace():
      sentence.append(letter)      

    else:



    print(sentence)
    
#  x = alpha[user_input]
#  y = alpha[user_input] + result_key

#  if y <= 29:
#    print(x)
#    print(nums[y])

#  elif y > 29:
#    letter2 = y - 29
#    letter3 = nums[letter2]
#    print(f" letter2 {letter3}")
#    print(x)
#    print(y)

encrypt(result_key, user_input)
  
def decrypt():
  print("b")

def decrypttoencryptnator():

  option = input("Vill du kryptera eller dekryptera?:")
  if option == "kryptera":
    user_input = input("Skriv:")
    keyscanorgeninator(user_input)
    result_key = keyscanorgeninator(user_input)
    print(result_key)

  else:
    print("Skriv kryptera eller dekryptera!")
    decrypttoencryptnator()

def test():

  user_input = input("test:")

  gap = 1

  alpha = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "å": 27,
    "ä": 28,
    "ö": 29,    
  }  

  nums = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "z",
    27: "å",
    28: "ä",
    29: "ö"    
  }    

  x = alpha[user_input]
  y = alpha[user_input] + gap

  if y <= 29:
    print(x)
    print(nums[y])

  elif y > 29:
    letter2 = y - 29
    letter3 = nums[letter2]
    print(f" letter2 {letter3}")
    print(x)
    print(y)