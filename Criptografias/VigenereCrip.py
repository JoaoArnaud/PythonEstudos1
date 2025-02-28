text = input('digite seu texto aqui: ')
custom_key = input('digite a customKey: ')

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # mantem todos os caracteres que não são letras
        if not char.isalpha():
            final_message += char
        else:        
            # encontrando o caractere chave certo para encodificar
            key_char = key[key_index % len(key)]
            key_index += 1

            # definindo o offset e a letra encriptada 
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)
encryption = encrypt(text, custom_key)
print(encryption)
decryption = decrypt(encryption, custom_key)
print(decryption)