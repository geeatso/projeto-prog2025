import math

### FUNÇÃO TRIÂNGULOS

def triangulo(lados):
    a, b, c = lados
    
# Classificação do triângulo (equilátero, escaleno ou isósceles)

    if a == b:
        if b == c:
            classificacao = "Triângulo Equilátero"
        else:
            classificacao = "Triângulo Isósceles"
    else:
        if a == c:
            classificacao = "Triângulo Isósceles"
        else:
            if b == c:
                classificacao = "Triângulo Isósceles"
            else:
                classificacao = "Triângulo Escaleno"
    
# Cálculo de perímetro e área
    perimetro = a + b + c
    s = perimetro/2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return classificacao, area, perimetro

### FUNÇÃO QUADRILÁTEROS

# Cálculo de perímetro e área

def quadrilatero(lados):
    a, b, c, d = lados
    perimetro = a + b + c + d
    area = a * b
    return "Quadrilátero", area, perimetro

### Input único (obrigatório)

entrada = input("Digite os números desejados separados por vírgula: ")
lista = [float(digito) for digito in entrada.split(',')]

### Classificação e resultado final

if len(lista) == 3:
    classificacao, area, perimetro = triangulo(lista)
    print("Forma geométrica:", classificacao)
    print("Perímetro:", round(perimetro, 2))
    print("Área:", round(area, 2))
else:
    if len(lista) == 4:
        classificacao, area, perimetro = quadrilatero(lista)
        print("Forma geométrica:", classificacao)
        print("Perímetro:", round(perimetro, 2))