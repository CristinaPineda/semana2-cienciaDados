"""
COURSERA 

Introdução à ciência da computação com Python - USP 

Semana 02 - Exercicíos opcionais

Exercício 2
Este é o desafio do vídeo "Entrada de Dados".

Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos. A saída deve estar no formato: a dias, b horas, c minutos e d segundos. Seja cuidadoso com o formato! Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:
Por favor, entre com o número de segundos que deseja converter: 178615

Saída de Dados:
2 dias, 1 horas, 36 minutos e 55 segundos.
"""

#contaSegundos

seg_str = int(input('Por favor, entre com o número de segundos que deseja converter:'))

dias = seg_str // 86400
seg_restantes = seg_str % 86400
horas = seg_restantes // 3600
seg_restantes = seg_restantes % 3600
minutos = seg_restantes // 60 
seg_rest_final = seg_restantes % 60

print(dias,'dias,',horas,'horas,',minutos,'minutos e',seg_rest_final,'segundos.')