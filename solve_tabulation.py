# Recurrencia del problema del ladrón
# -----------------------------------
#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0


def solve_tabulation(items):
    table=[0]
    def fill_table():
        # Rellena la tabla 'table' con las soluciones de todos los 
        # subproblemas (o sea, los beneficios máximos que puede
        # conseguir el ladrón)
        # ...

        if len(items) > 0:
            table = [items[0]]

            if len(items) > 1:
                table.append(max(items[0], items[1]))
                
                for i in range(2,len(items)):
                    table.append(max(items[i]+table[i-2], table[i-1]))
        
        return table.copy()

    table = fill_table()

    max_benefit = table[-1]     # El máximo beneficio está en el
                                # último elemento de la tabla
    return max_benefit