alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

def encrypt(original_text, shift_amount):
    ans = ''
    for letter in original_text:
        if letter == ' ':
            continue
        ans += alphabet[alphabet.index(letter) + shift]

    return ans

def decrypt(original_text, shift_amount):
    ans = ''
    for letter in original_text:
        if letter == ' ':
            continue
        ans += alphabet[alphabet.index(letter) - shift]

    return ans

if direction == 'encrypt':
    print("This is the encrypted text: ")
    print(encrypt(text, shift))
elif direction == 'decrypt':
    print("This is the decrypted text: ")
    print(decrypt(text, shift))

else:
    print("Invalid Answer")