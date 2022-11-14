from solve_memoization import *
from solve_tabulation  import *

def test():
    first_line = input().split()
    item_count = int(first_line[0])

    items = []
    for i in range(1, item_count+1):
        parts = input().split()
        items.append(int(parts[0]))

    value1 = solve_memoization(items)
    value2 = solve_tabulation(items)

    assert value1 == value2
    print(value1)

def test2():

    items = [3,10,11]

    value1 = solve_memoization(items)
    value2 = solve_tabulation(items)

    #assert value1 == value2
    print(value1)
    print(value2)

test2()