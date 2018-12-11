def podaj_liczbe():

    while True:
        try:
            n = int(input('Podaj liczbę od 1 do 9: '))
            if n > 0 and n < 10:
                return n
            else:
                print('Wybierz inną liczbę [', n, ']')
        except ValueError:
            print('Podana wartość nie jest liczbą.')


def powtorz():
    print('1. Powtórz\n2. Zakończ')
    m = input('Wybierz: ')
    loop = True
    while loop:
        if m == '1':
            podaj_liczbe()
        if m == '2':
            exit(0)
        else:
            print('Wybierz 1 lub 2')
            m = input('Wbyierz ponownie: ')


n = podaj_liczbe()
print('Wybrałeś', n)
powtorz()
