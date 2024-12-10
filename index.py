tasks = []
status = []

def add_task(task):
    tasks.append(task)
    status.append("pendente")

def mark_task_completed(task):
    if task in tasks:
        index = tasks.index(task)
        status[index] = "concluída"

def remove_task(task):
    if task in tasks:
        index = tasks.index(task)
        tasks.pop(index)
        status.pop(index)

def list_tasks():
    for task, state in zip(tasks, status):
        print(f"{task} - {state}")

def search_task(task):
    if task in tasks:
        index = tasks.index(task)
        print(f"{task} está {status[index]}.")
    else:
        print(f"{task} não encontrado.")

while True:
    print("\n1. Adicionar tarefa")
    print("2. Marcar tarefa como concluída")
    print("3. Remover tarefa")
    print("4. Listar tarefas")
    print("5. Pesquisar tarefa")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite o nome da tarefa: ")
        add_task(tarefa)
    elif opcao == "2":
        tarefa = input("Digite o nome da tarefa: ")
        mark_task_completed(tarefa)
    elif opcao == "3":
        tarefa = input("Digite o nome da tarefa: ")
        remove_task(tarefa)
    elif opcao == "4":
        list_tasks()
    elif opcao == "5":
        tarefa = input("Digite o nome da tarefa: ")
        search_task(tarefa)
    elif opcao == "6":
        break
    else:
        print("Opção inválida.")