"""
#### Exercício 1

Receba três notas (números decimais) de um aluno e imprima a média.

Exemplo:

Digite a primeira nota:
8.5
Digite a segunda nota:
7.0
Digite a terceira nota:
9.0

Resposta:
Média: 8.17

Dica: Use inputs para receber os dados! 
Lembre de converter ele para o tipo necessário!
Print na tela com "print"
"""

def calcular_media():
    Nota1 = float(input("Digite a primeira nota: "))
    Nota2 = float(input("Digite a segunda nota: "))
    Nota3 = float(input("Digite a terceira nota: "))

    return (Nota1 + Nota2 + Nota3) / 3

media_notas = calcular_media()
print(f"A media das notas é: {media_notas:.2f}")
