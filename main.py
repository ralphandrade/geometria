# Programa que calcula a area de algumas imagens geometricas
# função do menu

area_calculada = input('Qual area gostaria de calcular? "circulo" "triangulo" "trapezio": ')


        
#função area do círculo
def calcular_circulo(raio):
    area_circulo = raio * raio * 3.14
    return area_circulo

# resultado area circulo
raio = int(input('Informe o valor do raio: '))
print(f'Area do Circulo: {calcular_circulo(raio)}')

#função area do triangulo
def calcular_triangulo(base, altura):
    area_triangulo = base * altura / 2
    return area_triangulo

#resultado area triangulo
base = int(input('Informe a base do triangulo: '))
altura = int(input('Informe a altura do triangulo: '))
print(f'Area do Triangulo: {calcular_triangulo(base, altura)}')

#função area do trapézio
def calcular_trapezio(base_maior, base_menor, altura):
    area_trapezio = (base_maior + base_menor) * altura / 2
    return area_trapezio

#resultado area trapezio
base_maior = int(input('Informe a base maior do trapézio: '))
base_menor = int(input('Infomre a base menor do trapézio: '))
altura = int(input('Informe a altura do trapezio: '))
print(f'Area do Trapézio: {calcular_trapezio(base_maior, base_menor, altura)}')



match area_calculada:
    case "circulo":
        calcular_circulo
    case "triangulo":
        calcular_triangulo
    case "trapezio":
        calcular_trapezio
