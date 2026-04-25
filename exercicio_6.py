"""
#### Exercício 6 - Conversor de moeda

Você é uma casa de câmbio, recebe dinheiro em reais e transforma na moeda da viagem do usuário.

Você tem em caixa dólares, pesos argentinos e ienes.

Pergunte para o usuário para onde ele vai viajar:

Se ele falar "Estados Unidos", "Argentina" ou "Japão", faça o seguinte processo:
    Pergunte quantos reais ele vai converter. Receba o valor em float.
    Converta o valor para a moeda do país.
    Responda com o valor da moeda e em seguida o tipo da moeda (USD, ARS, ou JPY).

Se ele falar qualquer outra coisa, responda "Não temos essa moeda em caixa.".

Utilize as seguintes conversões:
5 reais = 1 USD
1 real = 180 ARS
1 real = 30 JPY

Obs:
Nos testes, vou tentar ignorar caso haja apenas uma diferença no número de casas decimais nas respostas.
Porém, se você quiser garantir que você imprima com exatamente 2 casas decimais você pode usar a seguinte sintaxe: f"{sua_variavel:.2f}".

Exemplo:
valor_em_dolares = 23.333333
print(f"{valor_em_dolares:.2f} USD")
>>> 23.33 USD

Mais informações sobre formatação de strings: https://realpython.com/python-f-strings/#interpolating-values-and-objects-in-f-strings

-------------------------------------------
Exemplos:

Qual país você vai viajar? Estados Unidos
Quantos reais você quer converter? 100

Resposta:
20.00 USD

-------------------------------------------
Qual país você vai viajar? Argentina
Quantos reais você quer converter? 100

Resposta:
18000.00 ARS

-------------------------------------------
Qual país você vai viajar? China

Resposta:
Não temos essa moeda em caixa.
"""

def cambio ():
    pais = input("Informe o país de destino: ")

    if pais == "Estados Unidos":
        reais = float(input("Digite a quantidade de Reais que deseja converter: "))
        dolares = reais / 5
        print (f"Você receberá {dolares:.2f} USD")

    elif pais == "Argentina":
            reais = float(input("Digite a quantidade de Reais que deseja converter: "))
            pesos = reais * 180
            print (f"Você receberá {pesos:.2f} ARS")

    elif pais == "Japão":
            reais = float(input("Digite a quantidade de Reais que deseja converter: "))
            yenes = reais * 180
            print (f"Você receberá {yenes:.2f} JPY")

    else:
        print (f"Não temos a moeda circulante em {pais} ")

cambio()
