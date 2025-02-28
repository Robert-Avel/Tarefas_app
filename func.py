from time import sleep


def pergunta(txt):
    while True:
        p = str(input(txt)).strip()[0]
        if p in 'Ss':
            return True
        elif p in 'Nn':
            return False
        

def inputInt(txt):
    while True:
        try:
            n = int(input(txt))
        except:
            print('Digite um número !')
        else:
            return n


def loadfile(arquivo):
    from json import loads
    try:
        acervo = open(arquivo, 'r')
        print(f'Recuperando dados de {arquivo}')
        sleep(1)
        conteudo = loads(acervo.read())
        print('DADOS RECUPERADOS')
        acervo.close()
        return conteudo
    except:
        print(f'Arquivo {arquivo} não encontrado!')
        sleep(1)
        acervo = open(arquivo, 'x')
        print(f'arquivo {arquivo} gerado')
        return []

def savefile(arquivo, lista_principal):
    from json import dumps
    try:
        acervo = open(arquivo, 'w')
        acervo.write(dumps(lista_principal, indent= 1))
        acervo.close()
    except:
        print(f'Arquivo {arquivo} não encontrado')
    

def novaTarefa(nome, lista_principal):
    nova_tarefa = {}
    nova_tarefa['tarefa'] = nome
    nova_tarefa['status'] = 'Pendente'
    lista_principal.append(nova_tarefa.copy())
    print(f'{nome} adicionado !')
    nova_tarefa.clear()
    return addHistorico('Adicionar', nome)


def apagarTarefa(index, lista_principal):
    while True:
        if 0 <= index <= len(lista_principal)-1:
            break
        else:
            print('A Tarefa não existe')
    log = addHistorico('Apagar', lista_principal[index]['tarefa'])
    lista_principal.pop(index)
    return log


def editarTarefa(index, novo_nome, lista_principal):
    while True:
        if 0 <= index <= len(lista_principal)-1:
            log = addHistorico('Editar', novo_nome, lista_principal[index]['tarefa'])
            lista_principal[index]['tarefa'] = novo_nome
            return log
        else:
            print('A Tarefa não existe')


def addHistorico(ação, nome, antes='---', depois='---'):
    item = {
        'ação': ação,
        'nome': nome,
        'antes': antes,
        'depois': depois
    }
    return item


def avancarTarefa(index, lista_principal):
    if not lista_principal:
            print('A Lista está vazia')
            sleep(2.5)
    else:
        if lista_principal[index]['status'] == 'Pendente':
            p = pergunta('Iniciar Tarefa? ')
            if p:
                h = addHistorico('Avançar', lista_principal[index]['tarefa'], 'Pendente', 'Em Andamento')
                lista_principal[index]['status'] = 'Em Andamento'
        elif lista_principal[index]['status'] == 'Em Andamento':
            p = pergunta('Finalizar tarefa? ')
            if p:
                h = addHistorico('Avançar', lista_principal[index]['tarefa'], 'Em Andamento', 'Concluído')
                lista_principal[index]['status'] = 'Concluído'
        elif lista_principal[index]['status'] == 'Concluído':
            print('Essa tarefa foi concluida')
    return h

