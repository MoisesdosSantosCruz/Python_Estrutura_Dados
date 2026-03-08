class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpity(self):
        return self.items == []
    
    def enqueue(self, item, prioridade, tipo_prioridade):
        self.items.append((prioridade, item, tipo_prioridade))  # final
        self.items.sort()                      # organiza por urgência

    def dequeue(self):
        return self.items.pop(0)[1]
    
    def exibir(self):
        return self.items.copy() 
    
    def size(self):
        return len(self.items)

q = Queue()

print(q.isEmpity())
q.enqueue("José", 3, "Normal")
q.enqueue("Sofia", 1, "Urgente")
q.enqueue("Marcos", 2, "Moderado")
q.enqueue("Lucas",1, "Urgente")
print(q.isEmpity())
print(q.exibir())