# Correção do exercício 2
def ePrimo(n): 
    resultado = True
    for i in range(2,n): 
        if (n % i == 0):
            resultado = False
        
    
    return resultado 

n = -1
contpos = 0
contneg = 0
contdivpor2 = 0
contdivpor5 = 0
contprimos = -1 
conttotal = 0 
while n != 0:
    n = int(input('Digite um número inteiro: '))
    conttotal = conttotal + 1
    if n > 0: 
        contpos = contpos + 1
    if n < 0: 
        contneg = contneg + 1
    if n % 2 == 0: 
        contdivpor2 = contdivpor2 + 1
    if n % 5 == 0:
        contdivpor5 = contdivpor5 + 1
    if ePrimo(n) == True: 
        contprimos = contprimos + 1

print('Total de números:', conttotal)
print('Porcentagem de números positivos: ', (contpos / conttotal) * 100, '%')
print('Porcentagem de números negativos: ', (contneg / conttotal) * 100, '%') 
print('Porcentagem de números div por 5: ', (contdivpor2 / conttotal) * 100, '%') 
print('Porcentagem de números div por 2: ', (contdivpor5 / conttotal) * 100, '%') 
print('Porcentagem de números primos : ', (contprimos / conttotal) * 100, '%') 