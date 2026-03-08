class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    


s = Stack()

while True: 
    Opcao = input("Você quer inserir uma tarefa? S - Sim  N - Não Q - Sair \n")
    match Opcao:
        case "S":
            if (Opcao == "S"):
                tarefa = input("Qual tarefa?\n")
                s.push(tarefa)

                print("\nTarefa Adicionada")
                print(s.items)
        case "N":
            print("Última Tarefa adicionada: ", s.peek())
        
        case "Q":
            print("Sair.")
            break

    
