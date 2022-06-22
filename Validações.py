# Avaliação 02 individual
# Autor: Filipe Tenedini Domingos

import random

def validar_acesso():
    while True:
        acctest = input('login: ')
        if acctest in logins:
            pastest = int(input('senha: '))
            if pastest in senhas:            
                if logins.index(acctest) == senhas.index(pastest):
                    print('Autorizado')
                    break
                else:
                    print('Senha ou usuário incorreto.')
            else:
                print('Senha incorreta')
        else:
            print('Usuário inválido')            

def gerar_senha():
    senha = random.randint(1000,9999)
    senhas.append(senha)
    return senha

def gerar_login():
    while True:

        print(*funcionarios, sep=", ", end="?\n")
        login = input('Quem está aí?\n:> ')
        if login in funcionarios:
            if login not in logins:
                logins.append(login)
                funcionarios.remove(login)
            else:
                print('Usuário já foi cadastrado antes')
                funcionarios.remove(login)
                continue
        else:
            print('Seu nome não está na lista de funcionários')
            continue
        return login

funcionarios = ['Pedro' , 'Ana'   , 'Carlos', 'Maria Clara', 'João Antonio']
salarios     = [ 3470.00, 2200.00, 3970.34, 7450.23 , 5677.33 ]
logins = []
senhas = []
media = sum(salarios) / len(salarios)
senhab = ''

login = gerar_login()
print('Bem vindo ao meu sistema de cadastro e controle de funcionários. Espero que goste!')
print('{}~~ digitar "sair" finaliza o programa ~~'.format(' '*25))
input('{}~~ aperte enter ~~\n\n'.format(' '*35))
print('|{0}|\n|{1:^40}|'.format('-'*40, 'Controle De Funcionários'))
print('|{0}|\n|{1:^40}|\n|{0}|'.format('-'*40, 'MENU'))
print('|{:^40}|\n|{:^32}        |\n| {:^25}              |\n|{:^39} |\n|{}|'.format('1- Cadastrar Login e Senha','2- Aumento de 10%',
                                                                                    '3- Relatório','4- Cadastrar Funcionário','-'*40))

while True:
    menu = input('Escolha uma opção do menu: ')
    if menu == 'sair':
        break

    if menu == '1':
        if senhab in senhas:
            print('Você já foi cadastrado')
            continue
        else:
            print(f'Bem vindo {login}.')
            senha = gerar_senha()
            print(f'Cadastro completo!\nSeu login: {login}\nSua senha: {senha}')
            senhab = senha
        
    if menu == '2':
        if len(logins) == 0:
            print('primeiro você precisa criar um login')
        else:
            print('~~ Área de aumento de salários ~~')
            validar_acesso()
            while True:
                aumento = input('Deseja aumentar o salário de seus funcionários que estão abaixo da média?\n[S / N]\n')
                if aumento in 'sS':
                    for indice, grana in enumerate(salarios):
                        aumento = grana * 0.10 + grana
                        if grana < media:
                            print('{} recebe abaixo da média. Aumentando salário de: R${:,.2f} para: R${:,.2f}\n'.format(funcionarios[indice], grana, aumento))
                            salarios[indice] = aumento
                            media = sum(salarios) / len(salarios)
                    break
                elif aumento in 'nN':
                    for indice, grana in enumerate(salarios):
                        if grana < media:
                            print('{} ficará com salário abaixo da média'.format(funcionarios[indice]))
                    break
                else:
                    print('Digite S ou N')
                    continue
                
    if menu == '3':
        if len(logins) == 0:
            print('primeiro você precisa criar um login')
        else:
            validar_acesso()
            print('|{0}|\n|{1:^45}|\n|{0}|'.format('-'*45,'FOLHA DE PAGAMENTOS'))
            for i, pessoa in enumerate(funcionarios):    
                print('|{:^22}|      R${:<14,.2f}|'.format(pessoa, salarios[i]))
            print('|{0}|\n|{1:>25} R${2:.2f}          |\n|{0}|'.format('-'*45,'MÉDIA SALARIAL:',media))
    
    if menu == '4':
        if len(logins) == 0:
            print('primeiro você precisa criar um login')
        else:
            validar_acesso()
            print('~~ Área de cadastro de funcionários/as ~~')
            print('Vamos cadastrar um funcionário novo!')
            while True:
                func = input('Digite o nome dele:\n')
                if len(func) == 0:
                    print('Nome inválido')
                    continue
                else:
                    while True:
                        salario = input('Qual salario mensal dele?')
                        if len(salario) == 0:
                            print('Digite um salário válido')
                            continue
                        else:
                            try:
                                salario = float(salario)
                                break
                            except:
                                print('Digite um salário válido')
                                continue
                            break
                    funcionarios.append(func)
                    salarios.append(salario)
                    media = sum(salarios) / len(salarios) #a média é atualizada a cada funcionário que você adiciona
                    print('Funcionário cadastrado.')
                    break
print('Foi um prazer desenvolver esse código')
