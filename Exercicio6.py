
#Nó da lista encadeada
class Node:
    def __init__ (self, dado):
        self.dado = dado 
        self.proximo = None #Guarda os dados e avança 
        
class ListaEncadeada:
    def __init__(self):
        self.inicio_lista = None # Inicia lista com o primeiro elemento
        self.fim_lista = None # Armazena outros dados adicionados

    def esta_Vazia(self):
        return self.inicio_lista is None #Verifica se está vazio

    
    def adicionar(self, nome, telefone):
        dado = f"{nome} - {telefone}" 
        novo = Node(dado) # Ele pega o conteúdo da variável dado na Classe Node
        #Caso estiver vazio, o primeiro elemento é adicionado. Caso o contrário, segue adicionando em outras posições
        if self.esta_Vazia():
            self.inicio_lista = novo 
            self.fim_lista = novo
        else:
            self.fim_lista.proximo = novo
            self.fim_lista = novo

    def exibir(self):
        atual = self.inicio_lista #Atualizando os dados
        while atual: #Enquanto houver dados adicionados, mostra
            print(atual.dado)
            atual = atual.proximo

    def remover_inicio(self):
        removido = self.inicio_lista.dado # Com a variavel, guarda o primeiro dado
        self.inicio_lista = self.inicio_lista.proximo # Substitui o primeiro pelo segundo
        return removido

l = ListaEncadeada()    

print("Anterior a remoção:")
l.adicionar("José", "999999-99")
l.adicionar("Pedro", "23213-99")
l.adicionar("Lucas", "45546-99")
l.exibir()
print("\nApós a remoção:")
l.remover_inicio()
l.exibir()



