import sys
import msvcrt

def run():
    while True:
        i=0
        while True:
            print(i)
            i=i+1
            if msvcrt.kbhit():
                if ord(msvcrt.getch()) == 27:
                    break
        loop = True
        while loop:
            print('1. Powtórz.')
            print('2. Zakończ')
            x = input('Wybierz 1. lub 2. : ')
            if x == '1':
                loop = False
                run()
            if x == '2':
                loop = False
                menu()
            else:
                loop = True

run()