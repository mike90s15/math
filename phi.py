from time import sleep
ultimo=1
penultimo=1
count=0
try:
    while True:
        count = count + 1
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        print(f'\033[34m  {count}ⁿ termo: ', termo)
        print('\033[33m  φ ≈ \033[31m', ultimo / penultimo, 'cada vez mais perto do número perfeito')
        sleep(0.01)    
        if count == 47:
                sleep(2)
                exit()
except:
    print()
