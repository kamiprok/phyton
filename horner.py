print('podaj stopien wielomianu: ')
n = int(input())
print(n)
y = n

tablica = []
for x in range(n+1):
    print('podaj liczbe przy potedze x ^', y)
    z = int(input())
    tablica.append(z)
    y = y - 1
print(tablica)

print('podaj c: (x + c) ')
c = int(input())
print('wybrano c =', c)

i = len(tablica)
print('dlugosc tablicy: ', i)

tablica2 = []
tablica2.append(tablica[0])

for i in range(1, n+1):
    tablica2.append(tablica2[i-1]*c+tablica[i])
print(tablica2)

m = n-1

print('Wynik: ')
print('( x -', c, ' )( ', end="")
for i in range(1, n):
    print(tablica2[i-1], 'x ^', m, ' + ', end="")
    m = m-1
print(tablica2[i], "} i ", tablica2[i+1], ' reszty.')