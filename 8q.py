def czy_moze(dane, x, y):
	for i in range(0, len(dane)):
		przesx = abs(i - x)
		przesy = abs(dane[i] - y)
		if (dane[i] == y or przesx == przesy):
			return False
	return True


def ustaw_hetmana(dane, n):
	ile = 0
	if (len(dane) == n):
		return 1
	else:
		for k in range(0, n):
			if (czy_moze(dane, len(dane), k)):
				dane.append(k)
				ile += ustaw_hetmana(dane, n)
				dane.pop()
	return ile


def szukaj_rozwiazan(n):
	dane = []
	return ustaw_hetmana(dane, n)

n = int(input("Podaj wielkość planszy [n] : "))
w = szukaj_rozwiazan(n)
print("Rozwiązań: " + str(w))