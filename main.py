import os
import sys
import time

def menu():
    os.system('cls')
    print("Current Python version: ", sys.version)
    print('\nWitaj\n')
    print('Wybierz z listy który program chcesz uruchomić (1 - 5) :\n')
    print('1. Hello World!')
    print('2. Harmoniczny')
    print('3. Horner')
    print('4. Hanoi')
    print('5. 8 Queens')
    print('\n\ne. Wyjście')
    print('\nWybierz program: ', end='')
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

        def menu_harmoniczny():
            print('\nMenu: ')
            print('1. Powtórz ')
            print('e. Exit \n')
            choice = input('Co chcesz zrobić: ')
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
                            for x in range(1, n + 1):
                                sum += 1 / x
                            print('Wynik:', sum)
                            menu_harmoniczny()
                            loop = False
                        else:
                            print('Podaj liczbę z przedziału (1 - 1 000 000)')
                        break
                except ValueError:
                    print('To nie jest liczba!')

        harmoniczny()
        input('\n\nPress ENTER to continue.')
        menu()
    if x == '3':
        os.system('cls')

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
                n = input('Podaj stopień wielomianu: \n')
                try:
                    n = int(n)
                except ValueError:
                    if n == 'e':
                        m = input("Zakończyć? ")

                    else:
                        print('To nie jest liczba!')
                else:
                    if n < 2 or n > 12:
                        print('Podaj liczbę z przedziału (2 - 12)')
                    else:
                        print('Wybrano :', n)
                        y = n

                        tablica = []
                        powtorz2 = n + 1

                        for x in range(n + 1):
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

                                        for i in range(1, n + 1):
                                            tablica2.append(tablica2[i - 1] * c + tablica[i])
                                        print(tablica2)

                                        m = n - 1

                                        print('Wynik: ')
                                        print('(x - ', c,')(', end="", sep='')
                                        for i in range(0, n - 1):
                                            print(tablica2[i], 'x^', m, ' + ', end='', sep='')
                                            m = m - 1
                                        print(tablica2[-3], 'x + ', tablica2[-2],') i ', tablica2[-1], ' reszty.',sep='')
                                        print('\n ### KONIEC ### ')
                                        horner_menu()
                                    else:
                                        print('c nie może być 0 bo to nie będzie dwumian')
                                else:
                                    print('Wybierz inną liczbę...')

        horner()
    if x == '4':
        os.system('cls')

        def hanoi_menu():
            print('\nMenu: ')
            print("1. Powtórz ")
            print('e. Exit ')
            choice = input("\nWybierz opcję: ")
            loop = True
            while loop:
                if choice == '1':
                    loop = False
                    os.system('cls')
                    hanoiMain()
                if choice == 'e':
                    loop = False
                    os.system('cls')
                    menu()
                else:
                    choice = input('Zły wybór. Wybierz ponownie: ')

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
                    n = int(input('Podaj liczbę dysków [n]: '))
                except ValueError:
                    print('To nie jest liczba')
                else:
                    if n > 0 and n < 21:
                        A = list(range(n, 0, -1))
                        B, C = [], []
                        print(A, B, C)
                        count = 0
                        start = time.time()
                        hanoi(n, A, B, C)
                        end = time.time()
                        print('\nLiczba ruchów: ', count)
                        print('Czas: ', round(end - start, 4))
                        hanoi_menu()
                    else:
                        print('Podaj liczbę od 1 do 20')

        hanoiMain()
    if x == '5':
        os.system('cls')
        print('8 Hetmanów (early access)')

        def czy_moze(dane, x, y):
            for i in range(0, len(dane)):
                przesx = abs(i - x)
                przesy = abs(dane[i] - y)
                if (dane[i] == y or przesx == przesy):
                    return False
            return True

        def ustaw_hetmana(dane, n):
            ile = 0
            if (len(dane) == n):
                return 1
            else:
                for k in range(0, n):
                    if (czy_moze(dane, len(dane), k)):
                        dane.append(k)
                        ile += ustaw_hetmana(dane, n)
                        dane.pop()
            return ile

        def szukaj_rozwiazan(n):
            dane = []
            return ustaw_hetmana(dane, n)

        n = int(input("Podaj wielkość planszy [n] : "))
        w = szukaj_rozwiazan(n)
        print("Rozwiązań: " + str(w))


        input('\n\nPress ENTER to continue.')
        menu()
    elif x == 'e':
        print('\nŻegnaj')
        time.sleep(0.5)
        os.system('cls')
        sys.exit()
    else:
        os.system('cls')
        menu()

menu()