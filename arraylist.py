class ArrayList:

    def __init__(self):

        self.MEMORY_SPACE = 10
        self.lastPosition = 0
        self.array = [None] * self.MEMORY_SPACE

    
    def capacity(self):
        return len(self.array)

    
    def size(self):
        return self.lastPosition

    
    def add(self, value):

        
        if self.lastPosition == self.capacity():
            self.resizeMemory()

        
        self.array[self.lastPosition] = value

        
        self.lastPosition += 1

    
    def resizeMemory(self):

        print("\n[INFO] Aumentando memória...\n")

        newArray = [None] * (self.capacity() * 2)

        
        for i in range(self.lastPosition):
            newArray[i] = self.array[i]

        self.array = newArray

    
    def remove(self, index):

        
        if index < 0 or index >= self.lastPosition:
            print("\n[ERRO] Índice inválido!\n")
            return

        
        for i in range(index, self.lastPosition - 1):
            self.array[i] = self.array[i + 1]

        
        self.array[self.lastPosition - 1] = None

        
        self.lastPosition -= 1

    
    def show(self):

        
        if self.lastPosition == 0:
            print("\nLista vazia!\n")
            return

        print("\n===== CONTATOS =====")

        
        for i in range(self.lastPosition):

            contato = self.array[i]

            print(f"{i} - Nome: {contato['nome']} | Telefone: {contato['telefone']}")

        print("====================\n")




listaTelefonica = ArrayList()

while True:

    print("====== MENU ======")
    print("1 - Adicionar contato")
    print("2 - Mostrar contatos")
    print("3 - Remover contato")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    
    if opcao == "1":

        nome = input("Digite o nome: ")

        
        while True:

            telefone = input("Digite o telefone: ")

            
            if telefone.isdigit():
                break

            print("\n[ERRO] Digite apenas números!\n")

        contato = {
            "nome": nome,
            "telefone": telefone
        }

        listaTelefonica.add(contato)

        print("\nContato adicionado com sucesso!\n")

    
    elif opcao == "2":

        listaTelefonica.show()

        print(f"Quantidade de contatos: {listaTelefonica.size()}")
        print(f"Capacidade da lista: {listaTelefonica.capacity()}\n")

    
    elif opcao == "3":

        listaTelefonica.show()

        
        if listaTelefonica.size() == 0:
            continue

        try:

            indice = int(input("Digite o índice do contato: "))

            listaTelefonica.remove(indice)

            print("\nContato removido com sucesso!\n")

        except ValueError:

            print("\n[ERRO] Digite apenas números!\n")

    
    elif opcao == "4":

        print("\nEncerrando sistema...")
        break

   
    else:

        print("\n[ERRO] Opção inválida!\n")