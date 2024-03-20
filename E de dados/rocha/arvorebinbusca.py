from queue import Queue

# A classe nó da árvore
class _Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# A classe árvore
class BinSearchTree():
    def __init__(self):
        self._root = None
        self._size = 0

    def _minimum(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._minimum(subtree.left)

    def _maximum(self, subtree):
        if subtree is None:
            return None
        elif subtree.right is None:
            return subtree
        else:
            return self._maximum(subtree.right)

    def _height(self, subtree):
        if subtree is None:
            return -1
        else:
            hleft = self._height(subtree.left)
            hright = self._height(subtree.right)
            if hleft < hright:
                return hright + 1
            else:
                return hleft + 1

    # Função de percurso em pré-ordem
    def preorder(self, subtree):
        if subtree is not None:
            print(subtree.key, end=" ")
            self.preorder(subtree.left)
            self.preorder(subtree.right)

    # Função de percurso em ordem
    def inorder(self, subtree):
        if subtree is not None:
            self.inorder(subtree.left)
            print(subtree.key, end=" ")
            self.inorder(subtree.right)

    # Função de percurso em pós-ordem
    def postorder(self, subtree):
        if subtree is not None:
            self.postorder(subtree.left)
            self.postorder(subtree.right)
            print(subtree.key, end=" ")

    # Função de percurso em largura
    def breadthFirst(self, bintree):
        # Cria uma fila e enfila a raiz.
        q = Queue()
        q.enqueue(bintree)
        # Visita cada nó na árvore.
        while not q.isEmpty():
            # Remove o nó da fila e o visita.
            node = q.dequeue()
            print(node.key, end=" ")
            # Enfila os dois filhos.
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)

    # Método que pesquisa por uma chave na árvore.
    def _search(self, subtree, value):
        if subtree is None:  # caso base
            return None
        elif value < subtree.key:  # value está na sub-árvore a esquerda.
            return self._search(subtree.left, value)
        elif value > subtree.key:  # value está na sub-árvore a direita.
            return self._search(subtree.right, value)
        else:  # caso base... igual
            return subtree

    # Insere um novo nó na árvore
    def _insert(self, subtree, value):
        if subtree is None:
            subtree = _Node(value)
        elif value < subtree.key:
            subtree.left = self._insert(subtree.left, value)
        elif value > subtree.key:
            subtree.right = self._insert(subtree.right, value)
        return subtree

    def insert2(self, subtree, value):
        if subtree is None:
            novo = _Node(value)
            return novo
        else:
            if value > subtree.key:
                subtree.right = self.insert2(subtree.right, value)
            else:
                subtree.left = self.insert2(subtree.left, value)
            return subtree

    # Adiciona um novo nó na árvore.
    def add(self, value):
        # Busca o nó que contém a chave, se ele existe.
        node = self._search(self._root, value)
        # Se a chave não existe na árvore.
        if node is None:
            self._root = self._insert(self._root, value)
            self._size += 1
            return True
        # Se a chave já existe, não adiciona.
        else:
            return False

    # Helper method that removes an existing item recursively.
    def _remove(self, subtree, target):
        # Search for the item in the tree.
        if subtree is None:
            return subtree
        elif target < subtree.key:
            subtree.left = self._remove(subtree.left, target)
            return subtree
        elif target > subtree.key:
            subtree.right = self._remove(subtree.right, target)
            return subtree
        # We found the node containing the item.
        else:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:
                successor = self._minimum(subtree.right)
                subtree.key = successor.key
                subtree.right = self._remove(subtree.right, successor.key)
                return subtree

    # Removes the map entry associated with the given key.
    def remove(self, key):
        if self._search(self._root, key) is not None:
            self._root = self._remove(self._root, key)
            self._size -= 1
        else:
            print(f"\nInvalid key: {key}")


# Função principal
def main():
    arv = BinSearchTree()
    arv.add(60)
    arv.add(12)
    arv.add(90)
    arv.add(4)
    arv.add(41)
    arv.add(71)
    arv.add(100)
    arv.add(1)
    arv.add(29)
    arv.add(84)
    arv.add(23)
    arv.add(37)

    print("\nPré-ordem: ", end="")
    arv.preorder(arv._root)
    print("\nEm ordem: ", end="")
    arv.inorder(arv._root)
    print("\nPós-ordem: ", end="")
    arv.postorder(arv._root)
    print("\nPercurso em largura: ", end="")
    arv.breadthFirst(arv._root)

    h = arv._height(arv._root)
    print(f"\nAltura da árvore: {h}", end="")

    arv.remove(23)
    arv.remove(41)
    arv.remove(68)
    print("\nEm-ordem: ", end="")
    arv.inorder(arv._root)



if __name__ == "__main__":
    main()