### LISTA DE EXERCÍCIOS 1
## QUESTÃO 4

def arredondamento(num, d):
    n = 0
    while abs(num)>=1:
        num = num/10
        n += 1
    a = str(num).split('.')
    inteiro = a[0]
    decimal = a[1]
    if len(decimal) > d:
        if int(decimal[d]) >= 5:
            aux = str(int(decimal[d-1])+1)
            decimal = decimal[:d-1]+aux
        else:
            decimal = decimal[:d]
    x = inteiro+'.'+decimal
    num = float(x)
    for i in range(n):
        num *= 10
    return num

def calcularErros(p, ap):
    erroAb = abs(p-ap)
    print('  Erro absoluto: ', erroAb)
    p = abs(p)
    if p > 0.0000001:   # p deve ser diferente de 0.
        erroRel = erroAb/p
        print('  Erro relativo: ', erroRel)
        erros = [erroAb, erroRel]
        return erros
    else:
        print('  Não é possível calcular o erro absoluto (p = 0)')
        erros = [erroAb, -1000000]
        return erros

x0 = 1.31
y0 = 3.24
x1 = 1.93
y1 = 4.76

p = ((x0*y1)-(x1*y0))/(y1-y0)
a = arredondamento(x0*y1, 3)
b = arredondamento(x1*y0, 3)
c = arredondamento(y1-y0, 3)
ap = (a-b)/c
ap = arredondamento(ap, 3)
print('> Para x = ((x0*y1)-(x1*y0))/(y1-y0), com arredondamento com 3 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
erros1 = calcularErros(p, ap)
print('')

p = x0-((x1-x0)*y0)/(y1-y0)
a = arredondamento((x1-x0)*y0, 3)
b = arredondamento(a/(y1-y0), 3)
ap = x0-b
ap = arredondamento(ap, 3)
print('> Para x = x0-((x1-x0)*y0)/(y1-y0), com arredondamento com 3 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
erros2 = calcularErros(p, ap)
print('')

print('> Conclusões:')
if erros1[0] < erros2[0]:
    print('  Erro absoluto é menor com a primeira fórmula')
elif erros1[0] == erros2[0]:
    print('  Erro absoluto é igual com as duas fórmulas')
else:
    print('  Erro absoluto é menor com a segunda fórmula')

if erros1[1] < 0 or erros2[1] < 0:
    print('  Não foi possível comparar os erros relativos')
if erros1[1] < erros2[1]:
    print('  Erro relativo é menor com a primeira fórmula')
elif erros1[1] == erros2[1]:
    print('  Erro relativo é igual com as duas fórmulas')
else:
    print('  Erro relativo é menor com a segunda fórmula')
print('')

# Conclusão: A segunda fórmula funciona melhor com aritmética de arredondamento com 
# 3 dígitos, pois são realizadas menos aproximações no seu processo, então a perda 
# de precisão é menor e, consequentemento, o resultado é mais próximo do exato.