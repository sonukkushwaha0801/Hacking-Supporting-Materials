import string
letters = string.ascii_lowercase
print(letters)
num_letter = len(letters)


def encrypt_decrypt(text,mode,key):
    result = ''
    if mode == 'd':
        key = -key
    
    for letter in text:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                result +=letter
            else:
                new_index = index + key
                if new_index >= num_letter:
                    new_index -= num_letter
                elif new_index <0 :
                    new_index += num_letter
                result += letters[new_index]
    return result
print('*** CAESAR CIPHER PROGRAM')

print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()

if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    key = int(input('Enter the key (1 through 26):'))
    text = input('Enter the text to encrypt: ')
    encrypted_text = encrypt_decrypt(text,user_input,key)
    print(f"Ciphertext : {encrypted_text}")
     

if user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    key = int(input('Enter the key (1 through 26):'))
    text = input('Enter the text to decrypt: ')
    decrypted_text = encrypt_decrypt(text,user_input,key)
    print(f'Plaintext : {decrypted_text}')