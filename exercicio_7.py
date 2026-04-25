def ident_variante_relevante ():
    freq_pop = float(input("Digite a frequencia da variante na população: "))
    gene  = input("Digite o gene da variante: ").upper()
    reads = int(input("Digite o numero de reads da variante: "))
    vaf = float(input("Digite a frequencia alelica da variante (0-100): "))
    impacto = input ("Digite o impacto da variante (ALTO ou BAIXO): ").upper()

    if reads < 10 or vaf < 20:
        return "Não é relevante"

    elif impacto =="BAIXO":
        return "Não é relevante"
    
    elif impacto =="ALTO" and freq_pop > 5 and  gene not in ["HFE", "MEFV", "GJB2"]:
       return "Não é relevante"
    
    else:
       return "É relevante"
    
relevancia = ident_variante_relevante ()
print(relevancia)
