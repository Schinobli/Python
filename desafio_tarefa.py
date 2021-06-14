print('Aplicativo de tarefas: ')
print('1- adicionar nova tarefa.')
print('2- mostrar tarefas.')
print('3- remover tarefa.')
print('4- desfazer última ação.')

list_to_do = []
last_time = {}


def add_last_time(tarefa, index):
    global last_time
    last_time = {'add': {
        tarefa: index
    }}


def rem_last_time(tarefa, index):
    global last_time
    last_time = {'rem': {
        tarefa: index
    }}


while True:
    try:
        comando = int(input('Qual seu comando: '))
        if comando == 1:
            tarefa = input('Digite o nome da tarefa:\n')
            list_to_do.append(tarefa)

            add_last_time(tarefa, len(list_to_do) - 1)
        elif comando == 2:
            for i, v in enumerate(list_to_do):
                print(f'{i + 1}- {v}')

        elif comando == 3:
            remove = int(input('Qual tarefa desejá remover? '))

            rem_last_time(list_to_do[remove - 1], remove - 1)

            list_to_do.pop(remove - 1)
        elif comando == 4:
            if last_time == {}:
                continue
            elif last_time.get('add') is not None:
                tarefa = [x for x in last_time.get('add')]
                index = last_time.get('add').get(tarefa[-1])
                list_to_do.pop(last_time.get('add').get(tuple(last_time.get('add'))[0]))

                rem_last_time(tarefa[0], index)

            elif last_time.get('rem') is not None:
                tarefa = [x for x in last_time.get('rem')]
                index = last_time.get('rem').get(tarefa[-1])
                list_to_do.insert(index, tarefa[-1])


                add_last_time(tarefa[0], index)
        else:
            print('Opção inválida.')
            continue

    except ValueError:
        print('Opção inválida.')
        continue
