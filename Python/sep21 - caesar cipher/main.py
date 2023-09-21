alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Main Function #
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    # reverse shift direction if decode
    shift_amount *= -1
  for char in start_text:
    if char.isalpha():
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    # use * instead of non-letter characters
    else:
      end_text += "*"
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

# logo art
import art
print(art.logo)

# loop to keep ciphering
keep_playing = True
while keep_playing:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  # if shift is greater than 26
  if shift > 26:
    shift = shift%26
    print(shift)
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  play_again = input("Cipher Another? (y/n)").lower()
  if play_again == "n":
    print("Thank you for ciphering.")
    keep_playing = False