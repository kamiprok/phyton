s=0
while s<1:
    try:
        n = int(input('podaj liczbe elementow: \n'))
    except ValueError:
        print('To nie jest liczba')
    else:
        sum = int(0)
        for x in range(1,n+1):
            sum+=1/x
        print(sum)