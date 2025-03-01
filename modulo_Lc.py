def pergunta(txt: str):
    while True:
        p = str(input(txt)).strip()[0]
        if p in 'Ss':
            return True
        elif p in 'Nn':
            return False
        

def inputInt(txt: str):
    while True:
        try:
            n = int(input(txt))
        except:
            print('Digite um número !')
        else:
            return n


def inputRange(txt: str, list: list | tuple):
    while True:
        try:
            n = int(input(txt))
            if 0 <= n <= len(list)-1:
                return n
            else:
                print(f'As opções vão até {len(list)-1}')
        except:
            print('Digite um número !')


def loadfile(arquivo):
    from pickle import loads
    from time import sleep
    from tarefa import ListaTarefas
    try:
        acervo = open(arquivo, 'rb')
        print(f'Recuperando dados de {arquivo}')
        sleep(1)
        conteudo = loads(acervo.read())
        print('DADOS RECUPERADOS')
        acervo.close()
        return conteudo
    except:
        print(f'Arquivo {arquivo} não encontrado!')
        sleep(1)
        acervo = open(arquivo, 'xb')
        print(f'arquivo {arquivo} gerado')
        return ListaTarefas()

def savefile(arquivo, lista):
    from pickle import dumps
    try:
        acervo = open(arquivo, 'wb')
        acervo.write(dumps(lista))
        acervo.close()
    except:
        print(f'Arquivo {arquivo} não encontrado')


def optiontable(title: str, *options: str, center=False):
    if center:
        title_in = f'{title:^40}'
    else:
        title_in = title
    print(f'{'-'*40} \n{title_in} \n{'-'*40}')
    for number, option in enumerate(options):
        print(f'[ {number+1} ] - {option}')


def checktruty(variable, message: str = '', reverse: bool = False):
    if not reverse:
        if variable:
            return True
        print(message)
        return False
    else:
        if not variable:
            return True
        print(message)
        return False