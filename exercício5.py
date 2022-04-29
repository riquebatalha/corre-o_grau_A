def menu():
    print('=' * 30)
    print('    MENU PRINCIPAL   ')
    print('=' * 30)
    print('OPÇÕES - A')
    print('OPÇÕES - B')
    print('OPÇÕES - C')
    print('OPÇÕES - D')

def menu2():
    print('-' * 50)
    print('INFORME QUAL TIPO DE CAFÉ VOCÊ DESEJA: ')
    print('[C] para CAFÉ')
    print('[CP] para CAFÉ PRETO')
    print('[CL] para CAFÉ COM LEITE E CAPPUCCINO ')
    print('-' * 50)

cafe = 1000
agua = 1000
leite = 1000
mistura = 1000


menu()
num = int(input('Informe um número: '))
if num == 0:
    menu2()