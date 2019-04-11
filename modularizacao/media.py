#media, moda, mediana
from statistics import *
#median(lista)
#mode(lista)

def media(lista):
	#mean(lista)
	media = sum(lista)/float(len(lista))
	return media

def mediana(lista):
	#median(lista)
	lista_ordenada = sorted(lista)
	t = len(lista_ordenada)
	if t%2 == 0:
		mediana = lista_ordenada[int(t/2)]+lista_ordenada[int((t/2)+1)]/2
	elif t%2 == 1:
		mediana = lista_ordenada[int((t/2))]

	return mediana

def moda(lista):
	#mode(list)
	lista_dicionario = {}
	for l in lista:
		if l not in lista_dicionario:
			lista_dicionario[l] = 1
		else:
			lista_dicionario[l] += 1
	maior_repeticao = max(lista_dicionario.values())
	for i in  lista_dicionario:
		if lista_dicionario[i] == maior_repeticao:
			moda = i
	return moda
