class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    # INSERÇÃO DE NÓ
    def insert(self, root, value):

        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)

        elif value > root.value:
            root.right = self.insert(root.right, value)

        return root

    # BUSCA DE NÓ
    def search(self, root, value):

        if root is None:
            return False

        if root.value == value:
            return True

        if value < root.value:
            return self.search(root.left, value)

        return self.search(root.right, value)

    # ENCONTRAR O MENOR VALOR (SUCESSOR IN-ORDER)
    def find_min(self, root):

        current = root

        while current.left is not None:
            current = current.left

        return current.value

    # REMOÇÃO DE NÓ
    def delete(self, root, value):

        # Caso base: árvore vazia
        if root is None:
            return root

        # Percorre a árvore até encontrar o nó
        if value < root.value:
            root.left = self.delete(root.left, value)

        elif value > root.value:
            root.right = self.delete(root.right, value)

        else:
            # Caso 1: nó folha (sem filhos)
            if root.left is None and root.right is None:
                return None

            # Caso 2: apenas um filho (direito)
            elif root.left is None:
                return root.right

            # Caso 2: apenas um filho (esquerdo)
            elif root.right is None:
                return root.left

            # Caso 3: dois filhos
            successor = self.find_min(root.right)

            root.value = successor

            root.right = self.delete(root.right, successor)

        return root

    # PERCURSO EM ORDEM (ORDERED OUTPUT)
    def inorder(self, root):

        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)


# Interação de todo o programa

tree = BinarySearchTree()

while True:

    print("\n===== MENU =====")
    print("1 - Inserir produto")
    print("2 - Buscar produto")
    print("3 - Remover produto")
    print("4 - Mostrar produtos (ordem crescente)")
    print("5 - Sair")

    option = input("Escolha uma opção: ")

    if option == "1":

        value = int(input("Digite o código do produto: "))

        tree.root = tree.insert(tree.root, value)

        print("Produto inserido com sucesso!")

    elif option == "2":

        value = int(input("Digite o código do produto: "))

        found = tree.search(tree.root, value)

        if found:
            print("Produto encontrado!")
        else:
            print("Produto não encontrado!")

    elif option == "3":

        value = int(input("Digite o código do produto: "))

        tree.root = tree.delete(tree.root, value)

        print("Produto removido com sucesso!")

    elif option == "4":

        print("Produtos em ordem crescente:")

        tree.inorder(tree.root)

        print()

    elif option == "5":

        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")