# Exercício 1  / 2 formas de resolução 

# 1 resolução, código simples 

def ePrimo(n): 
    resultado = True
    for i in range(2,n): 
        if (n % i == 0):
            resultado = False
        
    
    return resultado 

# continuação do exercício 1 com o 3

contaPrimos = 0 
n = 2
while (contaPrimos < 10): 
    if (ePrimo(n) == True):
        # print(n) # Uma forma de escrever
        contaPrimos = contaPrimos + 1
        print(contaPrimos, '=', n)
    n = n + 1
