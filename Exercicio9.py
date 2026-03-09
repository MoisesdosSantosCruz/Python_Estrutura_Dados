class Node:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class ListaEncadeadaDuplicada:
    def __init__(self):
        self.inicio_lista = None # Inicia lista com o primeiro elemento
        self.fim_lista = None # Armazena outros dados adicionados

    def esta_Vazia(self):
        return self.inicio_lista is None #Verifica se está vazio
    
    #É como uma fila, vai adicionando no final
    def adicionar_Inicio(self, nome, telefone, email):
        dado = f"{nome} - {telefone} - {email}" 
        novo = Node(dado) 
        if self.esta_Vazia():
            self.inicio_lista = novo 
            self.fim_lista = novo
        else:
            novo.proximo = self.inicio_lista
            self.inicio_lista.anterior = novo
            self.inicio_lista = novo

    #É como uma pilha, vai adicionando ao topo
    def adicionar_fim(self, nome, telefone, email): 
        dado = f"{nome} - {telefone} - {email}" 
        novo = Node(dado) 
        if self.esta_Vazia():
            self.inicio_lista = novo 
            self.fim_lista = novo
        else:
            novo.proximo = self.fim_lista
            novo.anterior = self.fim_lista
            self.fim_lista = novo
        
    def exibir_tras_para_frente(self):
        atual = self.inicio_lista #Atualizando os dados
        while atual: #Enquanto houver dados adicionados, mostra
            print(atual.dado)
            atual = atual.proximo

    def exibir_frente_para_tras(self):
        atual = self.fim_lista #Atualizando os dados
        while atual: #Enquanto houver dados adicionados, mostra
            print(atual.dado)
            atual = atual.anterior

    def remover_inicio(self):
        if self.esta_Vazia():
            print ("Sem elemento")
        else:
            removido = self.inicio_lista.dado # Com a variavel, guarda o primeiro dado
            self.inicio_lista = self.inicio_lista.proximo # Substitui o primeiro pelo segundo
            return removido
    
    def remover_fim(self):
        if self.esta_Vazia():
            print( "Sem elemento")
        else:
            removido = self.fim_lista.dado # Com a variavel, guarda o primeiro dado
            self.fim_lista = self.fim_lista.proximo # Substitui o primeiro pelo segundo
            return removido
    
    def tamanho_inicio(self):
        contador = 0
        atual = self.inicio_lista 
        while atual:
            contador += 1
            atual = atual.proximo 
        return contador

    def tamanho_fim(self):
        contador = 0
        atual = self.fim_lista 
        while atual:
            contador += 1
            atual = atual.anterior
        return contador

l = ListaEncadeadaDuplicada()

print("Nome - Telefone - Email\n")
print(l.esta_Vazia())
l.adicionar_Inicio("José", "999999-99", "José@gmail.com")
l.remover_inicio()
l.adicionar_Inicio("Pedro", "23213-99", "Pedro@gmail.com")
l.adicionar_Inicio("Lucas", "45546-99", "Lucas@gmail.com")
l.exibir_tras_para_frente()
print(l.esta_Vazia())
print(l.tamanho_inicio())


'''print("Nome - Telefone - Email\n")
l.adicionar_fim("Miguel", "12312323-55", "Miguel@gmail.com")
l.remover_fim()
l.adicionar_fim("João", "5432342-88", "João@gmail.com")
l.adicionar_fim("Lúcia", "23231245-44", "Lucia@gmail.com")
l.exibir_frente_para_tras()
print(l.tamanho_fim())'''

       
