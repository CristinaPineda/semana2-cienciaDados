"""
COURSERA 

Introdução à ciência da computação com Python - USP 

Semana 02 - Exercicíos opcionais

Exercício 1
Uma empresa de cartão de crédito envia suas faturas por email com a seguinte mensagem:

1 Olá, Fulano de Tal
2 A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.

Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento, o mês de vencimento e o valor da fatura e imprima (saída de dados) a mensagem com os dados recebidos, no mesmo formato da mensagem acima. Note que o programa imprime a saída em duas linhas diferentes. Note também que, como não é preciso realizar cálculos, o valor não precisa ser convertido para número, pode ser tratado como texto.

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:
1 Digite o nome do cliente: Fulano de Tal
2 Digite o dia de vencimento: 9
3 Digite o mês de vencimento: Janeiro
4 Digite o valor da fatura: 350,00

Saída de Dados:
Olá, Fulano de Tal
A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.
"""

#fatura

cliente = input('Digite o nome do cliente:')
diaVencimentoFatura = input('Digite o dia de vencimento:')
mesVencimentoFatura = input('Digite o mês de vencimento:')
valorFatura = input('Digite o valor da fatura:')

print('Olá,', cliente)
print('A sua fatura com vencimento em', diaVencimentoFatura, 'de', mesVencimentoFatura, 'no valor de R$', valorFatura, 'está fechada.')