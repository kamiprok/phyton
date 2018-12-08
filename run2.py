def podaj_liczbe():
    n = input('Podaj liczbę: ')
    print('Wybrałeś:', n)
    powtorz()


def powtorz():
    print('1. Powtórz\n2. Zakończ')
    n = input('Wybierz: ')
    loop = True
    while loop:
        if n == '1':
            podaj_liczbe()
        if n == '2':
            exit(0)
        else:
            n = input('Wbyierz ponownie: ')


podaj_liczbe()
