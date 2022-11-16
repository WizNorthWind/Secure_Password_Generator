from random import choice


def generate_password(lenght, chars):
    parol = ''
    for i in range(int(lenght)):
            parol += choice(chars)
    return parol

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''


amount = input('Сколько паролей ты хочешь сгенерировать?   ')
lenght = input('Сколько символов должно быть в пароле?   ')
digits_parol = input('Включать ли цифры 0123456789? (да) или (нет)   ')
if digits_parol.lower() == 'да':
    chars += digits
lower_parol = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да) или (нет)   ')
if lower_parol.lower() == 'да':
    chars += lowercase_letters
upper_parol = input('Включать ли строчные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да) или (нет)   ')
if upper_parol.lower() == 'да':
    chars += uppercase_letters
punctuation_parol = input('Включать ли символы !#$%&*+-=?@^_? (да) или (нет)   ')
if punctuation_parol.lower() == 'да':
    chars += punctuation
exception_parol = input('Исключать ли неоднозначные символы il1Lo0O? (да) или (нет)   ')
if exception_parol == 'да':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')


for _ in range(int(amount)):
    print(generate_password(lenght, chars))