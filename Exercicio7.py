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

idp = int(input("Número de urgência: \n"))
nome = input("Nome do paciente: \n")
paciente = f"{id} - {nome}"




