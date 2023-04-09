import numpy as np
import random


#Crie um array em NumPy com 5 números aleatórios entre 0 e 100.
array = np.random.randint(low=0, high=101, size=(5))

'''
low: o menor valor que pode ser gerado (inclusive).
high: o maior valor que pode ser gerado (exclusive).
size: a forma (ou tamanho) do array a ser gerado.
'''

#Imprima o array na tela.
print(type(array))
print(array)

#Acesse o terceiro elemento do array e imprima-o na tela.
print(array[2])

#Altere o segundo elemento do array para o valor 10.
array[2]=10
print(array)

#Crie uma nova lista em Python contendo os valores do array em ordem inversa.

def reverse(array):
    '''O slice é representado por seq[início:fim:passo]'''
    array_inversa = array[::-1]
    return array_inversa

array_inversa = list(reverse(array))
print(array_inversa)


#Crie uma função em Python que receba um array como argumento e retorne a média dos valores do array.
desvio_array = np.std(array)
med_array = np.mean(array)
print(f'Desvio Padrão: {desvio_array} , Média: {med_array}')
