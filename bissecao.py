from math import cos, pow

def metodo_bissecao(f, a, b, precisao):

    if (f(a)*f(b)<0):
        
        while (True):
            r = (a+b)/2
            e = (b-a)/2

            if (e <= precisao):
                return r
            else:
                if(f(r) == 0):
                    return r
                elif (f(r) < 0):
                    a = r
                else:
                    b = r

    else:
        print 'nao ha raiz no intervalo'
        return False

# f(x) = x^3 - cos(x) no intervalo [0, 5] com e=10^-2
print (metodo_bissecao(lambda x: pow(x, 3) - cos(x), -1, 1, pow(10, -2)))