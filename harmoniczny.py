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
                for x in range(1,n+1):
                    sum+=1/x
                print(sum)
                if input('Jeszcze raz?  [y/n]: ') == 'n':
                    powtorz = 1
            else:
                print('podaj liczbę z przedziału ( 1 - 1.000.000 )')

harmoniczny()
