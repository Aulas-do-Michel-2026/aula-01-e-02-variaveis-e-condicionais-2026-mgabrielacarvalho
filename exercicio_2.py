"""
#### Exercício 2

Uma fórmula recomenda 2mg de medicamento por kg de peso do paciente.

Peça o peso de uma pessoa e calcule a dose recomendada.

Exemplo:

Digite o peso do paciente (em kg):
70

Resposta:
Média: 140 mg
"""

def dose_recomendada ():
    peso = float(input("Digite o seu peso em kg: "))

    return (2* peso)

dose_paciente = dose_recomendada()
print(f"A dose recomendada para este paciente é: {dose_paciente:.2f}")
