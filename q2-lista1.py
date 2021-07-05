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
    aux = num
    while abs(num)>=1:
        num = num/10
        n += 1
    a = str(num).split('.')
    inteiro = a[0]
    decimal = a[1]
    #if len(decimal) <= n:
    #    return aux
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
    else:
        print('  Não é possível calcular o erro absoluto (p = 0)')

# a) 133 + 0,921
p = 133+0.921
a = truncamento(133, 3)
b = truncamento(0.921, 3)
ap = truncamento(a+b, 3)    # trunca 133 + 0,921
print('> Para (133 + 0,921), com truncamento com 3 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

a = truncamento(133, 4)
b = truncamento(0.921, 4)
ap = truncamento(a+b, 4)
print('> Para (133 + 0,921), com truncamento com 4 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

a = arredondamento(133, 3)
b = arredondamento(0.921, 3)
ap = arredondamento(a+b, 3)
print('> Para (133 + 0,921), com arredondamento com 3 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

a = arredondamento(133, 4)
b = arredondamento(0.921, 4)
ap = arredondamento(a+b, 4)
print('> Para (133 + 0,921), com arredondamento com 4 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)
print('')

# b) −10pi + 6e − 0,327
p = (-10)*(math.pi)+(6*math.e)-0.327
a = truncamento(math.pi, 3)     # trunca pi
b = truncamento(-10*a, 3)       # trunca -10pi
c = truncamento(math.e, 3)      # trunca e
d = truncamento(6*c, 3)         # trunca 6e
e = truncamento(b+d, 3)         # trunca -10pi + 6e
ap = truncamento(e-0.327, 3)    # trunca −10pi + 6e − 0,327
print('> Para (−10pi + 6e − 0,327), com truncamento com 3 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

a = truncamento(math.pi, 4)     
b = truncamento(-10*a, 4)       
c = truncamento(math.e, 4)      
d = truncamento(6*c, 4)         
e = truncamento(b+d, 4)        
ap = truncamento(e-0.327, 4)    
print('> Para (−10pi + 6e − 0,327), com truncamento com 4 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

a = arredondamento(math.pi, 3)     
b = arredondamento(-10*a, 3)      
c = arredondamento(math.e, 3)     
d = arredondamento(6*c, 3)         
e = arredondamento(b+d, 3)         
ap = arredondamento(e-0.327, 3)    
print('> Para (−10pi + 6e − 0,327), com arredondamento com 3 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

a = arredondamento(math.pi, 4)     
b = arredondamento(-10*a, 4)      
c = arredondamento(math.e, 4)     
d = arredondamento(6*c, 4)         
e = arredondamento(b+d, 4)         
ap = arredondamento(e-0.327, 4) 
print('> Para (−10pi + 6e − 0,327), com arredondamento com 4 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)
print('')

# c) (2/9)*(9/7)
p = (2/9)*(9/7)
a = truncamento(2/9, 3)     # trunca 2/9
b = truncamento(9/7, 3)     # trunca 9/7
ap = truncamento(a*b, 3)    # trunca (2/9)*(9/7)
print('> Para (2/9)*(9/7), com truncamento com 3 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

a = truncamento(2/9, 4) 
b = truncamento(9/7, 4)
ap = truncamento(a*b, 4)
print('> Para (2/9)*(9/7), com truncamento com 4 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

a = arredondamento(2/9, 3) 
b = arredondamento(9/7, 3)
ap = arredondamento(a*b, 3)
print('> Para (2/9)*(9/7), com arredondamento com 3 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

a = arredondamento(2/9, 4) 
b = arredondamento(9/7, 4)
ap = arredondamento(a*b, 4)
print('> Para (2/9)*(9/7), com arredondamento com 4 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)
print('')

# d) (pi-(22/7))/(1/17)
p = (math.pi-(22/7))/(1/17)
a = truncamento(math.pi, 3) # trunca pi
b = truncamento(22/7, 3)    # trunca 22/7
c = truncamento(a-b, 3)     # trunca pi - 22/7
d = truncamento(1/17, 3)    # trunca 1/17
ap = truncamento(c/d, 3)    # trunca (pi-(22/7))/(1/17)
print('> Para (pi-(22/7))/(1/17), com truncamento com 3 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

a = truncamento(math.pi, 4)
b = truncamento(22/7, 4)
c = truncamento(a-b, 4)
d = truncamento(1/17, 4)
ap = truncamento(c/d, 4)
print('> Para (pi-(22/7))/(1/17), com truncamento com 4 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

a = arredondamento(math.pi, 3)
b = arredondamento(22/7, 3)
c = arredondamento(a-b, 3)
d = arredondamento(1/17, 3)
ap = arredondamento(c/d, 3)
print('> Para (pi-(22/7))/(1/17), com arredondamento com 3 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)

a = arredondamento(math.pi, 4)
b = arredondamento(22/7, 4)
c = arredondamento(a-b, 4)
d = arredondamento(1/17, 4)
ap = arredondamento(c/d, 4)
print('> Para (pi-(22/7))/(1/17), com arredondamento com 4 dígitos:')
print('  p = ', p)
print('  p* = ', ap)
calcularErros(p, ap)