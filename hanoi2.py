def hanoi2(n, src, dst, tmp):
    if n <=0:
        return
    hanoi2(n-1, src, tmp, dst)
    print(src, dst)
    hanoi2(n-1, tmp, dst, src)

n = int(input('Podaj [n]: '))
hanoi2(n, 1, 3, 2)