import os
import sys
import time

def menu():
    print("Current Python version: ", sys.version)
    os.system('cls')
    print(' Witaj\n')
    print(' Wybierz z listy który program chcesz uruchomić (1 - 5) :\n')
    print(' 1. Hello World!')
    print(' 2. Harmoniczny')
    print(' 3. Horner')
    print(' 4. Hanoi')
    print(' 5. 8 Queens')
    print('\n\n e. Wyjście')
    print('\n Wybierz program: ', end='')
    x = input()
    if x == '1':
        os.system('cls')
        def hello2():
            os.system('cls')
            input('Hello World!\n\n\nPress ENTER to continue.')
        hello2()
        menu()
    if x == '2':
        os.system('cls')
        def harmoniczny():
            powtorz = 0
            while powtorz == 0:
                try:
                    n = int(input('podaj liczbe elementow: \n'))
                except ValueError:
                    print('To nie jest liczba')
                else:
                    if n > 0 and n < 1000001:
                        sum = int(0)
                        for x in range(1, n + 1):
                            sum += 1 / x
                        print(sum)
                        if input('Jeszcze raz?  [y/n]: ') == 'n':
                            powtorz = 1
                    else:
                        print('podaj liczbę z przedziału ( 1 - 1.000.000 )')
        harmoniczny()
        input('\n\nPress ENTER to continue.')
        menu()
    if x == '3':
        os.system('cls')

        def horner():
            powtorz = 0
            while powtorz == 0:
                try:
                    n = int(input('podaj stopien wielomianu: \n'))
                except ValueError:
                    print('To nie jest liczba!')
                    horner()
                else:
                    if n > 1 and n < 21:
                        print('wybrano :', n)
                        y = n

                        tablica = []
                        for x in range(n + 1):
                            try:
                                print('podaj liczbe przy potedze x ^', y)
                                z = int(input())
                            except ValueError:
                                print('To nie jest liczba!!')
                            else:
                                if z > -1000000 and z < 1000000:
                                    tablica.append(z)
                                    y = y - 1
                                else:
                                    print('podaj inną liczbę...')
                        print(tablica)

                        try:
                            print('podaj c: (x - c) ')
                            c = int(input())
                        except ValueError:
                            print('To nie jest liczba!!!')
                        else:
                            if c > -1000000 and c < 1000000:
                                if c != 0:
                                    print('wybrano c =', c)

                                    i = len(tablica)
                                    print('dlugosc tablicy:', i)

                                    tablica2 = []
                                    tablica2.append(tablica[0])

                                    for i in range(1, n + 1):
                                        tablica2.append(tablica2[i - 1] * c + tablica[i])
                                    print(tablica2)

                                    m = n - 1

                                    print('Wynik: ')
                                    print('( x -', c, ')( ', end="")
                                    for i in range(1, n):
                                        print(tablica2[i - 1], 'x ^', m, ' + ', end="")
                                        m = m - 1
                                    print(tablica2[i], "} i ", tablica2[i + 1], ' reszty.')
                                    print('\n### KONIEC ###\n')
                                    if input('Jeszcze raz?  [y/n]: ') == 'n':
                                        powtorz = 1
                                else:
                                    print('c nie może być 0 bo to nie będzie dwumian')
                            else:
                                print('wybierz inną liczbę...')
                    else:
                        print('podaj liczbę z przedziału (2 - 20)')
                        horner()

        horner()
        input('\n\nPress ENTER to continue.')
        menu()
    if x == '4':
        os.system('cls')
        def hanoiMain():
            powtorz = 0
            while powtorz == 0:
                global count

                def hanoi(n, P1, P2, P3):
                    if n == 0:
                        return
                    global count
                    count += 1
                    hanoi(n - 1, P1, P3, P2)
                    if P1:
                        P3.append(P1.pop())
                        print(A, B, C)
                    hanoi(n - 1, P2, P1, P3)

                try:
                    n = int(input('podaj liczbę dysków [n]: '))
                except ValueError:
                    print('To nie jest liczba')
                else:
                    if n > 0 and n < 15:
                        A = list(range(n, 0, -1))
                        B, C = [], []
                        print(A, B, C)
                        count = 0
                        hanoi(n, A, B, C)
                        print('\nLiczba ruchów: ', count)
                        if input('\nJeszcze raz?  [y/n]: ') == 'n':
                            powtorz = 1
                    else:
                        print('podaj liczbę od 1 do 14')
        hanoiMain()
        input('\n\nPress ENTER to continue.')
        menu()
    if x == '5':
        os.system('cls')
        print('nic tu nie ma jeszcze')
        input('\n\nPress ENTER to continue.')
        menu()
    elif x == 'e':
        print('\n Żegnaj')
        print(' 3...')
        time.sleep(0.5)
        print(' 2...')
        time.sleep(0.5)
        print(' 1...')
        time.sleep(1)
        os.system('cls')
        sys.exit()
    else:
        os.system('cls')
        menu()

menu()