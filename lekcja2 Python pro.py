import random


password = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

x = int(input('podaj długość hasła: '))

haslo = ''

for i in range(x):
    haslo += random.choice(password)

print('twoje wygenerowane hasło', haslo)