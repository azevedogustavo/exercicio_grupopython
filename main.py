import random
import soma, subtrai, determinante
lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0,3):
    for c in range(0,3):
        lista[i][c] = random.randint(0, 3) 
for i in range(0,3):
    for c in range(0,3):
        print(f'[{lista[i][c]:^5}]' ,end=" ")
    print()

while(True):
    print("digite uma das opções")
    print("1.Soma \n2.subtrai \n3.calcula determinante")
    try:  
        decision = int(input())
    except NameError:
        print("\n digite uma das opções \n") 
    except ValueError:    
        print("\n digite uma das opções \n")    
    if decision == 1:
        soma.soma(lista)
    if decision == 2:
        subtrai.subtrai(lista)
    if decision == 3:
        determinante.determinante(lista)    
    # decision = {
    #     1: soma.soma(lista),
    #     2: subtrai.subtrai(lista),
    #     3: "3",
    # }
