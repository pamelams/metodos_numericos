### LISTA DE EXERCÍCIOS 1
## QUESTÃO 2
import math

def truncamento(num, d):    # d = número de dígitos
    n = 0
    while abs(num)>=1:
        num = num/10
        n += 1
    a = str(num).split('.')
    inteiro = a[0]
    decimal = a[1]
    decimal = decimal[:d]
    x = inteiro+'.'+decimal
    num = float(x)
    for i in range(n):
        num *= 10
    return num    

def arredondamento(num, d):
    n = 0
    while abs(num)>=1:
        num = num/10
        n += 1
    a = str(num).split('.')
    inteiro = a[0]
    decimal = a[1]
    if len(decimal) <= n:
        return num
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
    else:
        print('  Não é possível calcular o erro absoluto (p = 0)')

# a) 133 + 0,921
p = 133+0.921
ap = truncamento(p, 3)
print('> Para (133 + 0,921), com truncamento com 3 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

ap = truncamento(p, 4)
print('> Para (133 + 0,921), com truncamento com 4 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

ap = arredondamento(p, 3)
print('> Para (133 + 0,921), com arredondamento com 3 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

ap = arredondamento(p, 4)
print('> Para (133 + 0,921), com arredondamento com 4 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)
print('')

# b) −10pi + 6e − 0,327
p = (-10)*(math.pi)+(6*math.e)-0.327
ap = truncamento(p, 3)
print('> Para (−10pi + 6e − 0,327), com truncamento com 3 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

ap = truncamento(p, 4)
print('> Para (−10pi + 6e − 0,327), com truncamento com 4 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

ap = arredondamento(p, 3)
print('> Para (−10pi + 6e − 0,327), com arredondamento com 3 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

ap = arredondamento(p, 4)
print('> Para (−10pi + 6e − 0,327), com arredondamento com 4 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)
print('')

# c) (2/9)*(9/7)
p = (2/9)*(9/7)
ap = truncamento(p, 3)
print('> Para (2/9)*(9/7), com truncamento com 3 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

ap = truncamento(p, 4)
print('> Para (2/9)*(9/7), com truncamento com 4 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

ap = arredondamento(p, 3)
print('> Para (2/9)*(9/7), com arredondamento com 3 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

ap = arredondamento(p, 4)
print('> Para (2/9)*(9/7), com arredondamento com 4 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)
print('')

# d) (pi-(22/7))/(1/17)
p = (math.pi-(22/7))/(1/17)
ap = truncamento(p, 3)
print('> Para (pi-(22/7))/(1/17), com truncamento com 3 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

ap = truncamento(p, 4)
print('> Para (pi-(22/7))/(1/17), com truncamento com 4 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

ap = arredondamento(p, 3)
print('> Para (pi-(22/7))/(1/17), com arredondamento com 3 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

ap = arredondamento(p, 4)
print('> Para (pi-(22/7))/(1/17), com arredondamento com 4 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)