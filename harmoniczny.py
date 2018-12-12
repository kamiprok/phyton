import os
import sys

def menu_harmoniczny():
    print('\nMenu: ')
    print('1. Powtórz ')
    print('e. Exit \n')
    choice = input('Wybierz opcję: ')
    loop = True
    while True:
        if choice == '1':
            loop = False
            os.system('cls')
            harmoniczny()
        if choice == 'e':
            loop = False
            menu()
        else:
            choice = input('Zły wybór. Wybierz ponownie: ')

def harmoniczny():
    os.system('cls')
    while True:
        try:
            loop = True
            while loop:
                n = int(input('Podaj liczbę elementów [n]: '))
                if n > 0 and n < 1000001:
                    sum = int(0)
                    for x in range(1,n+1):
                        sum+=1/x
                    print('Wynik:', round(sum, 4))
                    menu_harmoniczny()
                    loop = False
                else:
                    print('Podaj liczbę z przedziału ( 1 - 1 000 000 )')
                break
        except ValueError:
            print('To nie jest liczba!')


harmoniczny()
