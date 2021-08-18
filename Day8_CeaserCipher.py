alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special = [32, 33, 64, 35, 36, 37, 94, 38, 42, 40, 41, 45, 43, 95, 61, 44, 46, 63, 47, 60, 62, 59, 58, 39, 34, 123, 125, 91, 93]

def encrypt(text, shift):
    encoded = ""
    ls = list(text)
    for i in range(len(ls)):
        if ord(ls[i]) in special:
            continue
        elif (ord(ls[i])+shift)%123 < 97:
            ls[i] = chr((ord(ls[i]) + shift) % 123 + 97)
        else:
            ls[i] = chr((ord(ls[i]) + shift) % 123)

    print(f"Your encrypted message is: \n{encoded.join(ls)}\n")


def decrypt(text, shift):
    decoded = ""
    ls = list(text)
    for i in range(len(ls)):
        if ord(ls[i]) in special:
            continue
        elif (ord(ls[i])-shift)%123 < 97:
            ls[i] = chr((ord(ls[i]) - shift) % 123 + 26)
        else:
            ls[i] = chr((ord(ls[i]) - shift) % 123)

    print(f"Your decrypted message is: \n{decoded.join(ls)}\n")

choice = 'y'
while choice == 'y':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
    choice = input("Do you again want to input (y/n): ")
