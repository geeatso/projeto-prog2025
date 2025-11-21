import math

### FUNÇÃO TRIÂNGULOS

def triangulo(lados):
    num1, num2, num3 = lados
    
# Classificação do triângulo (equilátero, escaleno ou isósceles)

    if num1 == num2 == num3:
        classificacao = "Triângulo equilátero"
    elif num1 == num2 or num1 == num3 or num2 == num3:
        classificacao = "Triângulo isósceles"
    else:
        classificacao = "Triângulo escaleno"
    
# Cálculo de perímetro e área
    perimetro = num1 + num2 + num3
    valor = perimetro/2
    area = math.sqrt(valor * (valor - num1) * (valor - num2) * (valor - num3))
    
    return classificacao, area, perimetro

### FUNÇÃO QUADRILÁTEROS

# Cálculo de perímetro e área

def quadrilatero(lados):
    num1, num2, num3, num4 = lados
    perimetro = num1 + num2 + num3 + num4
    area = num1 * num2
    return "Quadrilátero", area, perimetro
    
### FUNÇÃO PENTÁGONO

def pentagono(lados):
    lado = lados[0]
    
# Cálculo de perímetro e área
    
    perimetro = sum(lados)
    area = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * lado * lado
    
    return "Pentágono", area, perimetro
    
### FUNÇÃO HEXÁGONO

def hexagono(lados):
    lado = lados[0]
    
# Cálculo de perímetro e área
    
    perimetro = sum(lados)
    area = (3*math.sqrt(3)*(lado**2))/2
    
    return "Hexágono", area, perimetro

### FUNÇÃO HEPTÁGONO

def heptagono(lados):
    lado = lados[0]
    
# Cálculo de perímetro e área
    
    perimetro = sum(lados)
    area = 3.634*(lado**2)
    
    return "Heptágono", area, perimetro
    
### FUNÇÃO OCTÓGONO

def octogono(lados):
    lado = lados[0]
    
# Cálculo de perímetro e área
    
    perimetro = sum(lados)
    area = 2*lado**2*(1+math.sqrt(2))
    
    return "Octógono", area, perimetro

### FUNÇÃO ENEÁGONO

def eneagono(lados):
    lado = lados[0]
    
# Cálculo de perímetro e área
    
    perimetro = sum(lados)
    area = (9/4) * (lado**2) * (1/math.tan(math.pi/9))
    
    return "Eneágono", area, perimetro

### FUNÇÃO DECÁGONO

def decagono(lados):
    lado = lados[0]
    
# Cálculo de perímetro e área
    
    perimetro = sum(lados)
    area = (5*lado**2)/math.sqrt(5+2*math.sqrt(5))

    return "Decágono", area, perimetro
    
### FUNÇÃO UNDECÁGONO

def undecagono(lados):
    lado = lados[0]
    
# Cálculo de perímetro e área

    perimetro = sum(lados)
    area = ((11*lado**2)/4)*1/math.tan(math.pi/11)
    
    return "Undecágono", area, perimetro
    
### FUNÇÃO DODECÁGONO

def dodecagono(lados):
    lado = lados[0]
    
# Cálculo de perímetro e área

    perimetro = sum(lados)
    area = 3*(2+math.sqrt(3))*lado**2
    
    return "Dodecágono", area, perimetro
    
### Input único (obrigatório)

entrada = input("Digite os números desejados separados por vírgula: ")
lista = [float(digito) for digito in entrada.split(',')]

### Classificação e resultado final

if len(lista) == 3:
    classificacao, area, perimetro = triangulo(lista)
elif len(lista) == 4:
    classificacao, area, perimetro = quadrilatero(lista)
elif len(lista) == 5:
    classificacao, area, perimetro = pentagono(lista)
elif len(lista) == 6:
    classificacao, area, perimetro = hexagono(lista)
elif len(lista) == 7:
    classificacao, area, perimetro = heptagono(lista)
elif len(lista) == 8:
    classificacao, area, perimetro = octogono(lista)
elif len(lista) == 9:
    classificacao, area, perimetro = eneagono(lista)
elif len(lista) == 10:
    classificacao, area, perimetro = decagono(lista)
elif len(lista) == 11:
    classificacao, area, perimetro = undecagono(lista)
elif len(lista) == 12:
    classificacao, area, perimetro = dodecagono(lista)
                                        
print("Forma geométrica:", classificacao)                      
print("Perímetro:", round(perimetro))
print("Área:", round(area))