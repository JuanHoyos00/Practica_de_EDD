from src.Stacks_and_Queues.Implementation.Queue import Queue

mi_cola = Queue()
mi_cola.enqueue(7)
mi_cola.enqueue(8)
mi_cola.enqueue(4)
mi_cola.enqueue(1)
mi_cola.enqueue(3)
print(mi_cola)

def sumar(cola, numero):
    for _ in range(len(cola)):
        a = cola.peek()
        cola.enqueue(cola.dequeue())

        for _ in range(len(cola)):
            if a + cola.peek() == numero:
                y = a
                x = cola.peek()

                cola.enqueue(cola.dequeue())
            else:
                cola.enqueue(cola.dequeue())
    for _ in range(len(cola)):
        if cola.peek() == x:
            cola.dequeue()
            cola.enqueue(y)
        elif cola.peek() == y:
            cola.dequeue()
            cola.enqueue(x)
        else:
            cola.enqueue(cola.dequeue())

    return cola,x,y
print(sumar(mi_cola,5))
