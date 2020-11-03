"""
COURSERA 

Introdução à ciência da computação com Python - USP 

Semana 02 

Tarefa de programação: Lista de Exercícios -1 

Exercício 1
	Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, 
calcule e imprima (saída de dados) seu perímetro e sua área.

Observação: a saída deve estar no formato: "perímetro: x - área: y"

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:
Digite o valor correspondente ao lado de um quadrado: 3

Saída de Dados:
perímetro: 12 - área: 9

Dica: lembre-se que um quadrado tem quatro lados iguais, logo só é necessário pedir o lado uma vez.
"""

# Cálculo de perimetro e area

ladoQuadrado = int(input('Digite o valor do lado do quadrado: '))
perimetro = ladoQuadrado*4
area = ladoQuadrado**2

print('perímetro:',perimetro,'-','área:',area)