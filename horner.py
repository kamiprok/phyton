import os
import sys

def horner_menu():
    print('\nMenu: ')
    print("1. Powtórz ")
    print('e. Exit ')
    choice = input("\nWybierz opcję: ")
    loop = True
    while loop:
        if choice == '1':
            loop = False
            os.system('cls')
            horner()
        if choice == 'e':
            loop = False
            os.system('cls')
            menu()
        else:
            choice = input('Zły wybór. Wybierz ponownie: ')

def horner():
    powtorz = 0
    while powtorz == 0:
        try:
            n = int(input('Podaj stopień wielomianu: \n'))
        except ValueError:
            print('To nie jest liczba!')
        else:
            if n < 2 or n > 12:
                print('Podaj liczbę z przedziału (2 - 12)')
            else:
                print('Wybrano :', n)
                y = n

                tablica = []
                powtorz2 = n+1

                for x in range(n+1):
                    while powtorz2 != 0:
                        try:
                            print('Podaj liczbę przy potędze x ^', y)
                            z = int(input())
                        except ValueError:
                            print('To nie jest liczba!!')
                        else:
                            if z > -1000000 and z < 1000000:
                                tablica.append(z)
                                y = y - 1
                                powtorz2 = powtorz2 - 1
                            else:
                                print('Podaj inną liczbę...')
                print(tablica)
                powtorz3 = 0
                while powtorz3 == 0:
                    try:
                        print('Podaj c: (x - c) ')
                        c = int(input())
                    except ValueError:
                        print('To nie jest liczba!!!')
                    else:
                        if c > -1000000 and c < 1000000:
                            if c != 0:
                                powtorz3 = 1
                                print('Wybrano c =', c)

                                i = len(tablica)
                                print('Długość tablicy:', i)

                                tablica2 = []
                                tablica2.append(tablica[0])

                                for i in range(1, n+1):
                                    tablica2.append(tablica2[i-1]*c+tablica[i])
                                print(tablica2)

                                m = n-1

                                print(' Wynik: ')
                                print('( x -', c, ')( ', end="")
                                for i in range(1, n):
                                    print(tablica2[i-1], 'x ^', m, ' + ', end="")
                                    m = m-1
                                print(tablica2[i], ") i ", tablica2[i+1], ' reszty.')
                                print('\n ### KONIEC ### ')
                                horner_menu()
                            else:
                                print('c nie może być 0 bo to nie będzie dwumian')
                        else:
                            print('Wybierz inną liczbę...')

horner()