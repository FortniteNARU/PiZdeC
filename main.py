import random

число = random.randint(1, 100)

while True:
    CHISLO = input('Угадай число от 1 до 100 (или напиши "выключить"): ')

    if CHISLO == 'выключить':
        print('Пока!')
        break

    CHISLO = int(CHISLO)

    if CHISLO == число:
        print('Ты угадал!')
        break
    elif CHISLO < число:
        print('Число больше')
    else:
        print('Число меньше')
