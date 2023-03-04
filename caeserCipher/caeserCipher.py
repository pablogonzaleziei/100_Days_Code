alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
password = '1234'
def encrypt(text,shift):
    encoded_text=''
    for letter in text:
        if letter in alphabet:
            pos = alphabet.index(letter)
            new_pos = pos + shift
            while new_pos>=26:
                new_pos-=26
            encoded_letter = alphabet[new_pos]
            encoded_text +=encoded_letter
        else:
            encoded_text+=letter
    print('Encoded text is: ',encoded_text)
while(input("Start caeserCipher? ")=='yes'):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print('Text is: ',text)
    if direction == 'encode':
        encrypt(text,shift)
    elif direction == 'decode':
        input_password = input('This message is encoded, introduce the password: ')
        if password == input_password:
            encrypt(text, -shift)


# def decode_caesar(message):
#     for shift in range(26):
#         decoded_message = ""
#         for char in message:
#             if char.isalpha():
#                 decoded_char = chr((ord(char) - 97 - shift) % 26 + 97)
#                 decoded_message += decoded_char
#             else:
#                 decoded_message += char
#         print(f"Shift: {shift}, Decoded message: {decoded_message}")
# encoded_message = "mn n fr ufgqt"
# decoded_message = decode_caesar(encoded_message)
# print(decoded_message)

