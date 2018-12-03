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
            n = int(input('podaj liczbę dysków [n]: '))
        except ValueError:
            print('To nie jest liczba')
        else:
            if n > 0 and n < 15:
                A = list(range(n,0,-1))
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