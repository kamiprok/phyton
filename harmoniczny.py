print('podaj liczbe elementow: ')
n = int(input())
sum = int(0)

for x in range(1,n+1):
    sum+=1/x

print(sum)