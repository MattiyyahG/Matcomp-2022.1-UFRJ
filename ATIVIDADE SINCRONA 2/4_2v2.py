#Matheus Gomes Rocha
#DRE 120063760

import math
#Questão realizada de uma forma diferente de apenas elevar a 0.5
def quadrado(r, i, j):

    imaj = (i + j) / 2
    mul = imaj * imaj

    if ((mul == r) or (abs(mul - r) < 0.00001)):
        return imaj

    elif (mul < r):
        return quadrado(r, imaj, j)

    else:
        return quadrado(r, i, imaj)

def raiz(r):
    i = 1

    found = False
    while (found == False):

        if (i * i == r):
            print(i)
            found = True

        elif (i * i > r):

            res = quadrado(n, i - 1, i)
            print ("{0:.5f}".format(res))
            found = True
        i += 1

if __name__ == '__main__':
    #para saber diferentes valores de raiz, apenas mude o n!
    n = 4

    raiz(n)