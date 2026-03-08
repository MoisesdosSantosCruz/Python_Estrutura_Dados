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


def verifica_balanceamento(ex):
        for caracter in ex: #Para cada caracter, ele vai verificar se tem parenteses
            if caracter == '(': 
                s.push(caracter)
            elif caracter == ')':
                if s.isEmpty(): #Caso só tenha um ele vai indicar falso
                    return False
                s.pop()
            else: # Caso não tenha parenteses
                return print("Sem parenteses")
        return s.isEmpty()

#ex = "((2+3)*(1+4))"
#ex = "2 + (5 x 3) - 4"
#ex = "(15 + 7) x 6 "
ex = "8 - 3 x 4"
if(verifica_balanceamento(ex)): 
    print("Balanceada")
else:
    print("Não balanceada")    
