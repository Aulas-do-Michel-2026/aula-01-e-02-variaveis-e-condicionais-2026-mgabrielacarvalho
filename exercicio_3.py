"""
#### Exercício 3

Receba um número inteiro de um usuário. Se ele for par, imprima "Par". Se não, imprima "Ímpar".

Exemplo:

Digite um número:
10

Par
--------
Digite um número:
1

Ímpar

Dica: Lembre do comando de resto da divisão inteira!
"""

def par_ou_impar():
    numero = int(input("Digite um número qualquer: "))
    if numero % 2 ==0:
        return(f"O número {numero} é PAR")
    else:
        return(f"O número {numero} é ÍMPAR")


resultado = par_ou_impar()
print(resultado)
