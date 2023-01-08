alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def caesar(start_text, shift_alphabet_amount, shift_number_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_alphabet_amount *= -1
  
  for char in start_text:
 # Shift the letter.  
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_alphabet_amount
      end_text += alphabet[new_position]
 # Shift the number.   
    elif char in number:
      position = number.index(char)
      new_position = position + shift_number_amount
      end_text += number[new_position]
 # Don't shift the character, just insert it. in this case its " " and symbols.   
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")



should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift_letter = shift % 26 # incase user shift number is greater than 26
  shift_num = shift % 10 # incase user shift number is greater than 26

  caesar(start_text=text, shift_alphabet_amount=shift_letter, shift_number_amount =shift_num, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
    


