class Queue:
    def __init__(self):
        self._qList = list()

    def isEmpty(self):
        return len(self) == 0
    
    def mostrar(self):
        print(self._qList)

    def __len__(self):
        return len(self._qList)

    def enqueue(self, item):
        self._qList.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self._qList.pop(0)



def principal():
    lista = Queue()
    while True:
        value = int(input("Valor -> "))
        if value == 0:
            break
        lista.enqueue(value)
    lista.isEmpty()
    lista.__len__()
    lista.mostrar()


if __name__ == "__main__":
    principal()