import sys 
from colorama import Fore, init

init()

# Firewall Group

def caesar_cipher(mssg, key, decrypt=False):
   result = ""

   for character in mssg:
       if character.isalpha():
           
           # the amount of times to be shifted e.g 2,3,4.
           shift = key if not decrypt else -key
           if character.islower():
               # caesar cipher for lowercase letters.
               result += chr(((ord(character) - ord('a') + shift) % 26) + ord('a'))
           else:
               # caesar cipher for uppercase letters.
               result += chr(((ord(character) - ord('A') + shift) % 26) + ord('A'))
       else:
           # non-alphabet characters
           result += character
   return result

# enter the text to be encrypted
user_input = input(f"{Fore.GREEN}-> Please Enter your text/message: ")
# enter how many times to shift
key = int(input(f"{Fore.GREEN}-> Please specify the shift length: "))

if key > 25 or key < 0:
   print(f"{Fore.RED}[!] Your shift length should be between 0 and 25 ")
   sys.exit()

   # encrypt the user input with the given shift number
encrypted_text = caesar_cipher(user_input, key)

# encrypted text
print(f"{Fore.GREEN}The text: ({user_input}) has been encrypted as {Fore.RED}{encrypted_text}")