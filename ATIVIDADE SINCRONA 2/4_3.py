#Matheus Gomes Rocha
#DRE 120063760

import math
""""
Escreva o codigo que implemente LN(x), usando todas as operações aritmeticas e EXpE(x), 4.3)
"""         
                                            
def fat(x):
    if x == 0:
        
        return 1
    
    if x == 1:
        
        return 1
    
    if x > 1:
        
        return fat(x - 1) * x


def EXPE(x):
    
    result = 0
    
    for n in range(9): 
        
        result += x**n/fat(n)
        
    return result, abs(math.exp(x)-result)


#Para realizar esse exercicio o metodo utilizado foi o de Newton Raphson, onde xn+1 = xn-(f(xn)/f'(xn));
# n E Naturais onde "x0" é uma aproximação inicial dada, "n" indica a n-ésima iteração do algoritmo e "f'(xn) é a derivada da função "f" no ponto "xn".

def LN(x):
    
    it_maxima = 50 
    
    x1 = 0.7
    
    erro = 100
    
    i = 0
    
    while i < it_maxima and  abs(erro) > 1.0e-8:
        
        i += 1
        
        exp = EXPE(x1)[0] 
        
        x2 = x1 - (exp - x - 0)/exp
        
        erro = abs((x2 - x1)/x2*100) 
        
        x1 = x2       

    return round(x1, 8)


x = eval(input('x: '))

Vx = LN(x)

print('\nValor final:\n LN(x) = ', Vx)