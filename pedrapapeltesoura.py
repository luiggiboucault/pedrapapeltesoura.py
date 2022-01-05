import random

perguntar = int(input('''Escolha uma das opções: 

[0] Pedra
[1] Papel
[2] Tesoura
 
Digite sua escolha: '''))
computador = random.randint(0,2)

if computador == 0:
    print('O computador escolheu: Pedra')
    if perguntar == 0:
        print("Empate !")
    elif perguntar == 1:
        print(" Você perdeu")
    elif perguntar == 2:
        print("Computador venceu")
    else:
        print("Operacao invalida")

elif computador == 1:
    print('O computador escolheu: Papel')
    if perguntar == 0:
        print("Computador perdeu")
    elif perguntar == 1:
        print("Empate !")
    elif perguntar == 2:
        print("Você venceu")
    else:
        print("Operacao invalida")
elif computador == 2:
    print('O computador escolheu: Tesoura')
    if perguntar == 0:
        print("Você venceu")
    elif perguntar == 1:
        print("Computador venceu")
    elif perguntar == 2:
        print("Empate !")
    else:
        print("Operacao invalida")