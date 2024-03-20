class _QueueNode():
    def __init__(self, item):
        self.item = item
        self.next = None


class Queue():
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0

    def isEmpty(self):
        return self._qhead is None
    
    def mostrar(self):
        atual = self._qhead
        for i in range(self.__len__()):
            print(atual.item, end=" ")
            atual = atual.next   

    def __len__(self):
        return self._count

    def enqueue(self, item):
        node = _QueueNode(item) 
        if self.isEmpty():
            self._qhead = node
        else:
            self._qtail.next = node
        self._qtail = node
        self._count += 1

    def dequeue(self):
        if not self.isEmpty():
            node = self._qhead
            if self._qhead is self._qtail:
                self._qtail = None
            self._qhead = self._qhead.next
            self._count -= 1
            return node.item
        


def principal():
    lista = Queue()
    while True:
        value = int(input("Valor -> "))
        if value == 0:
            break
        lista.enqueue(value)
    lista.mostrar()




if __name__ == "__main__":
    principal()