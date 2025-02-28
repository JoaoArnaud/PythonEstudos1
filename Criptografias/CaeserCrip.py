text = input("Digite algo: ")
#quantas letras vai pular:
shift = 3

def caesar(message, offset):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = '' #declara text = string

    for i in text.lower():
        if i == ' ':
            #se tiver espaço add o espaço e nn criptografa ele
            encrypted_text += i
        else:
            index = alphabet.find(i) #local da letra no alfabeto
            new_index = (index + offset) % len(alphabet) #local + 3 dividido pelo resto da divisao do alfabeto
            #a divisão serve para quando chegar no limite voltar para o inicio do alfabeto 
            encrypted_text += alphabet[new_index]

    print('encrypted: ', encrypted_text)
    print('original text: ', message)

caesar(text, shift)
