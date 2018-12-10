import sys
import os


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


def queens_menu():
	print('\nMenu: ')
	print("1. Powtórz ")
	print('e. Exit ')
	choice = input("\nWybierz opcję: ")
	loop = True
	while loop:
		if choice == '1':
			loop = False
			os.system('cls')
			glowny()
		if choice == 'e':
			loop = False
			os.system('cls')
			menu()
		else:
			choice = input('Zły wybór. Wybierz ponownie: ')


def glowny():
	os.system('cls')
	n = int(input("Podaj wielkość planszy [n] : "))
	w = szukaj_rozwiazan(n)
	print("Rozwiązań: " + str(w))
	queens_menu()

glowny()