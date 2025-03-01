from datetime import datetime
class Tarefa:
    STATUS = ['PENDENTE', 'EM ANDAMENTO', 'CONCLUIDO']
    DIAS_SEMANA = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo']    
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self._status: int = 0
        self.data_unix = datetime.timestamp(datetime.now())
        self.data_criacao = datetime.fromtimestamp(self.data_unix).strftime('%d/%m/%Y %H:%M')
        self._dia_semana = datetime.now().weekday()
        self.meta: str | None = None


    @property
    def meta_contagem(self):
        if self.meta == None:
            return None
        contagem = datetime.fromtimestamp(datetime.strptime(self.meta, '%d/%m/%Y %H:%M').timestamp() - datetime.now().timestamp())
        return f'{contagem.hour}:{contagem.minute} horas, {contagem.day-1} Dia(s), {contagem.month-1} Mês(es) e {contagem.year-1970} Ano(s) restantes'


    def __repr__(self) -> str:
        return f'{__class__.__name__}({self.nome!r})'


    def __str__(self) -> str:
        return f'{self.nome:^20} | {self.STATUS[self._status]:^12} | {self.data_criacao} ({self.DIAS_SEMANA[self._dia_semana]})'


class ListaTarefas:
    def __init__(self) -> None:
        self.lista_tarefa: list[Tarefa] = [].copy()
    

    def nova_tarefa(self, nome: str):
        self.lista_tarefa.append(Tarefa(nome))
    

    def ver_tarefa(self, indice: int):
        print(self.lista_tarefa[indice])
    

    def avancar_tarefa(self, indice):
        if self.lista_tarefa[indice]._status >= 2:
            print(f'A Tarefa "{self.lista_tarefa[indice].nome}" foi concluida')
        else:
            self.lista_tarefa[indice]._status += 1
    

    def resetar_tarefa(self, indice):
        self.lista_tarefa[indice]._status = 0
    

    def definir_meta(self, indice, dia=0, mês=0, ano=0):
        ano_formatado = ano+1970
        base = datetime(ano_formatado, mês+1, dia+1).timestamp()
        meta = base + self.lista_tarefa[indice].data_unix
        self.lista_tarefa[indice].meta = datetime.fromtimestamp(meta).strftime('%d/%m/%Y %H:%M')


    def __str__(self) -> str:
        for number, lista in enumerate(self.lista_tarefa):
            print(f'{number} | {str(lista)}')
        return ''


import modulo_Lc
from time import sleep
memory: ListaTarefas = modulo_Lc.loadfile('data.py')

while True:
    modulo_Lc.savefile('data.py', memory)
    modulo_Lc.optiontable(
        'ANOTADOR DE TAREFAS',
        'Ver Tarefas',
        'Criar Tarefa',
        'Apagar Tarefa',
        'Avançar Tarefa',
        'Resetar Tarefa',
        'Definir Meta',
        'Ver Metas',
        'Sair',
        center=True
    )
    opc = modulo_Lc.inputInt('Opção: ')
    if opc == 1:
        print(str(memory))
        sleep(2)
    elif opc == 2:
        name = str(input('Nome da nova tarefa: '))
        memory.nova_tarefa(name)
    elif opc == 3:
        for number, options in enumerate(memory.lista_tarefa):
            print(f'[ {number} ] - {options.nome}')
        opc = modulo_Lc.inputRange('Qual Você deseja apagar? ', memory.lista_tarefa)
        confirma = modulo_Lc.pergunta(f'Quer mesmo apagar a tarefa "{memory.lista_tarefa[opc].nome}"?')
        if confirma:
            del memory.lista_tarefa[opc]
    elif opc == 4:
        for number, options in enumerate(memory.lista_tarefa):
            print(f'[ {number} ] - {options.nome}')
        opc = modulo_Lc.inputRange('Qual Você deseja Avançar? ', memory.lista_tarefa)
        confirma = modulo_Lc.pergunta(f'Quer mesmo avançar a tarefa "{memory.lista_tarefa[opc].nome}"?')
        if confirma:
            memory.avancar_tarefa(opc)
    elif opc == 5:
        for number, options in enumerate(memory.lista_tarefa):
            print(f'[ {number} ] - {options.nome}')
        opc = modulo_Lc.inputRange('Qual Você deseja resetar? ', memory.lista_tarefa)
        confirma = modulo_Lc.pergunta(f'Quer mesmo resetar a tarefa "{memory.lista_tarefa[opc].nome}"?')
        if confirma:
            memory.resetar_tarefa(opc)
    elif opc == 6:
        for number, options in enumerate(memory.lista_tarefa):
            print(f'[ {number} ] - {options.nome}')
        opc = modulo_Lc.inputRange('Qual Você deseja definir a meta? ', memory.lista_tarefa)
        while True:
            dias = modulo_Lc.inputInt('Dias: ')
            if dias <= -1:
                print('Esse parametro deve ser 0 ou mais')
                continue
            break
        while True:
            meses = modulo_Lc.inputInt('Meses: ')
            if meses <= -1:
                print('Esse parametro deve ser 0 ou mais')
                continue
            break
        anos = modulo_Lc.inputInt('Anos: ')
        memory.definir_meta(opc, dias, meses, anos)
        print(f'Meta definido para {memory.lista_tarefa[opc].meta_contagem}')
    elif opc == 7:
        for metas in memory.lista_tarefa:
            print(f'{metas.nome:20} | {metas.meta_contagem}')
    elif opc == 8:
        break