from time import sleep
import func

lista_tarefas = func.loadfile('lista_tarefas.json')
memoria = func.loadfile('historico.json')
while True:
    print(f'{'Nº':2} {'TAREFAS':^20} {'STATUS':10}')
    print('-'*30)
    for n, l in enumerate(lista_tarefas):
        print(f'{n:<2} {l['tarefa']:^20} {l['status']:10}')
    print('-'*30)
    sleep(2)
    
    print(
'''[ 1 ] - Adicionar Tarefa
[ 2 ] - Apagar Tarefa
[ 3 ] - Avançar Tarefa
[ 4 ] - Editar tarefa
[ 5 ] - Desfazer
[ 6 ] - Encerrar'''
    )
    opc = func.inputInt('Opção: ')
    if opc == 6: # Encerrar
        break
    elif opc == 1: # Adicionar tarefa
        mem = str(input('Nome da Tarefa: ')).strip()
        memoria.append(func.novaTarefa(mem, lista_tarefas))

    elif opc == 2: # Deletar tarefa
        if not lista_tarefas:
            print('A Lista está vazia')
            sleep(2.5)
            continue
        print('DELETAR TAREFA')
        while True:
            mem = func.inputInt('Nº')
            if 0 <= mem <= len(lista_tarefas)-1:
                memoria.append(func.apagarTarefa(mem, lista_tarefas))
                break
            else:
                print('A Tarefa não existe')  
        
    elif opc == 3:
        if not lista_tarefas:
            print('A Lista está vazia')
            sleep(2.5)
            continue
        print('AVANÇAR TAREFA')
        while True:
            mem = func.inputInt('Nº ')
            if 0 <= mem <= len(lista_tarefas)-1:
                memoria.append(func.avancarTarefa(mem, lista_tarefas))
                break
            else:
                print('A Tarefa não existe')
        
    elif opc == 4:
        if not lista_tarefas:
            print('A Lista está vazia')
            sleep(2.5)
            continue

        print('EDITAR TAREFA')
        while True:
            mem = func.inputInt('Nº ')
            if 0 <= mem <= len(lista_tarefas)-1:
                print(f'Editar a tarefa {lista_tarefas[mem]['tarefa']}')
                opc = str(input('Novo Nome: '))
                memoria.append(func.editarTarefa(mem, opc, lista_tarefas))
                break
            else:
                print('A Tarefa não existe')
        
    elif opc == 5:
        print('DESFAZER')

    else:
        print('Opção Inválida')
    sleep(2.5)

    func.savefile('lista_tarefas.json', lista_tarefas)
    func.savefile('historico.json', memoria)