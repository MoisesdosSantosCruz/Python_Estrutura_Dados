class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpity(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

q = Queue()


while True:
    Opcao = input("Você quer inserir um contato: S - Sim ou N - Não Q - Sair\n")
    match Opcao:
        case "S":
            nome = input("Nome do contato\n")
            telefone = input("Telefone do contato\n")
            contato = f"{nome} - {telefone}" #Junta os dados numa variável
            q.enqueue(contato)
        case "N":    
            print(q.dequeue())
        case "Q":
            print("Sair...")
            break
