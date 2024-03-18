from random import randint as rnd

number = rnd(1, 100)
print('Угадай число от 1 до 100')

while True:
    guess = int(input('Введите число:'))
    if guess < number:
        print('Ваше число меньше того, что загаданою')
    elif guess > number:
        print('Ваше число больше того, что загадано.')
    elif guess == number:
        break
print('Отличная интуиция! Вы угадали число :)')