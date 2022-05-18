#Matheus Gomes Rocha
#DRE 120063760

def div(x1, x2):
    
    counter = 0
    
    a = 1.0
    
    b = 1.5
    
    if x2 == 0:
        
        print("Não pode dividir por zero!")
        
        exit()
        
    elif x1 == 0:
        
        return [0,0]
    
    else: 
        while counter <=50 and (b-a) >=10**(-8):
            
            n1 = x2*a - x1
            
            n2 = x2*b - x1
            
            if n1 == 0:
                
                return [a,0]
            
            elif n2 == 0:
                return [b,0]    
            
            elif n1*n2<0: 
                c = (a+b)/2
                n3 = x2*c - x1
                if n3*n2 < 0:
                    a = c
                else:
                    
                    b = c
                    
                counter += 1
                
            else:
                
                if n1<0 and n2<0 and a < b:
                    
                    b += 10
                    
                elif n1<0 and n2<0 and b < a:
                    
                    a += 10
                    
                elif n1>0 and n2>0 and a < b:
                    
                    a -= 10
                    
                elif n1>0 and n2>0 and b < a:
                    
                    a -= 10
                    
    average = (a+b)/2
    average = round(average, 8)
    list = [average, counter]
    return list

print(div(3, 2))