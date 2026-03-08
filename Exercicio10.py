class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def exibir(self):
        return self.items.copy()


q = Queue()

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
    def exibir(self):
        return self.items.copy()

s = Stack()
historico = [] #Para guardar os alimentos que foram entregues

while True:
   
    Opcao = int(input("Menu: 1 - Novo Pedido, 2 - Cozinhar Próximo 3 - Entregar pedido pronto " \
    "4 - Ver Histório 5 - Ver Status Atual 6 - Sair\n"))
    match Opcao:
        case 1:
            pedido_novo = input("Qual é o pedido?\n")
            q.enqueue(pedido_novo) #Adiciona pedido à fila
        case 2:    
            if not q.isEmpty():
                pedido_pronto = q.dequeue() #Recebe o pedido da fila para cozinhar
                s.push(pedido_pronto) #manda o pedido pronto para entrega
                print(f"Cozinhando... {pedido_pronto}")
            else:
                print("Fila vazia...")
        case 3:
            if not s.isEmpty():
                pedido_entregue = s.pop() # recebe o pedido pronto 
                historico.append(pedido_entregue) # guarda 
                print(f"Entregue: {pedido_entregue}")
            else:
                print("Nenhum foi entregue ainda.")
        case 4:
            print(historico)
        case 5:
            print("Status\n")
            if (q.size() > 0): #verifica o tamanho para fazer quantos foram pedidos
                print(f" Pedidos: {q.exibir()}")
            
            if (s.size() > 0):
                print(f" Prontos: {s.exibir()}")

            if len(historico) > 0:
                print(f"Histórico de Entrgas: {len(historico)}\n")
        case 6:
            print("Saindo...")
            break

            