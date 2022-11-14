# Recurrencia del problema del ladrón
# -----------------------------------
#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_memoization(items):
    mem = {}

    # Utiliza esta función para programar el código de
    # tu recurrencia utilizando memoization.
    #   Aviso: Para resolver este ejercicio no es valido
    #          utilizar el soporte de @functools
    vec = []

    def t(n):
        sum = 0
        if n >= 0:
            vec.append(items[n])
            sum+=items[n]
            t(n-2)
            vec.pop()
            t(n-1)
        else:
            sum = 0

            for i in vec:
                sum += i
            
            mem[sum]=vec
        
        aux=0
        for i in mem.keys():
            if aux < i:
                aux = i

        return aux
        

    

    return t(len(items)-1)

    #3 10 3 1 2
    #0 1  2 3 4