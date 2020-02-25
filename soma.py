import random
def soma(lista):
    lista2 = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    for i in range(0,3):
        for c in range(0,3):
            lista2[i][c] = random.randint(0, 3)
    for i in range(0,3):
        for c in range(0,3):
            print(f'[{lista2[i][c]:^5}]' ,end=" ")
        print()
    print("\n")
    for i in range(0,3):
        for c in range(0,3):
            lista[i][c] = lista[i][c] + lista2[i][c]
    print()
    for i in range(0,3):
        for c in range(0,3):
            print(f'[{lista[i][c]:^5}]' ,end=" ")
        print()   
       