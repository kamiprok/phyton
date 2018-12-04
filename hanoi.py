import os
import sys
import time

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
            hanoi(n-1, P1, P3, P2)
            if P1:
                P3.append(P1.pop())
                print(A, B, C)
            hanoi(n-1, P2, P1, P3)

        try:
            n = int(input('Podaj liczbę dysków [n]: '))
        except ValueError:
            print('To nie jest liczba')
        else:
            if n > 0 and n < 20:
                A = list(range(n,0,-1))
                B, C = [], []
                print(A, B, C)
                count = 0
                start = time.time()
                hanoi(n, A, B, C)
                end = time.time()
                print('\nLiczba ruchów: ', count)
                print('Czas: ', round(end - start, 2))
                hanoi_menu()
            else:
                print('Podaj liczbę od 1 do 14')
hanoiMain()