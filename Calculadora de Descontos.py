#here go again

def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return 'The price should be a number'
    elif not isinstance(discount, (int, float)):
        return 'The discount should be a number'
    elif price <= 0:
        return 'The price should be greater than 0'
    elif discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'
    else:
        return price * (1 -(discount / 100)) 

teste = apply_discount(200, 35)
print(teste)

print('-' * 30)

# Segundo desafio - Cifra de César (criptrografia) 
def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
def decrypt(text, shift):
    return caesar(text, shift, False)

encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf'
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)