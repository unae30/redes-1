#função de contar consoantes e vogais criad
def contarVogaisConsoantes(string):
    vogais = "aeiou"
    consoantes = "bcdfghjklmnpqrstvwxyz"
    num_vogais = 0
    num_consoantes = 0
    for char in string.lower():
        if char in vogais:
            num_vogais += 1
        elif char in consoantes:
            num_consoantes += 1
    return (num_vogais, num_consoantes)

print(contarVogaisConsoantes('UNAEANTUNES'))