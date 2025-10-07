from typing import List
class PriorityQueue:
  def __init__(self, priority):
    self.__queue = [] #Estructura de Datos implementadora
    self.__priority: str = priority

  def enqueue(self, element: int) -> None: #Agrega después del First
    if(self.__priority == "min"):
      self.__queue.append(element)
      self.__queue.sort()
    elif(self.__priority == "max"):
      self.__queue.append(element)
      self.__queue.sort(key=lambda x: x[1], reverse=True)
    else:
      raise ValueError("Grave... Este tipo de cola no existe...")

  def dequeue(self) -> int : #Retorna y elimina el First
    if(len(self.__queue) == 0):
      raise TypeError("Cola vacía... No podés hacer dequeue")

    return self.__queue.pop(0)


  def peek(self) -> int: #Retorna el First
    if(len(self.__queue) == 0):
      raise TypeError("Cola vacía... No podés hacer dequeue")

    return self.__queue[0]

  def __repr__(self) -> str:
    return str(self.__queue)

  def __len__(self) -> int:
    return len(self.__queue)

class Queue:
  def __init__(self):
    self.__queue: List[int] = [] #Estructura de Datos implementadora

  def enqueue(self, element: int) -> None: #Agrega después del First
    self.__queue.append(element)
    return None

  def dequeue(self) -> int : #Retorna y elimina el First
    if(len(self.__queue) == 0):
      raise TypeError("Cola vacía... No podés hacer dequeue")

    return self.__queue.pop(0)


  def peek(self) -> int: #Retorna el First
    if(len(self.__queue) == 0):
      raise TypeError("Cola vacía... No podés hacer dequeue")

    return self.__queue[0]

  def __repr__(self) -> str:
    return str(self.__queue)

  def __len__(self) -> int:
    return len(self.__queue)
class Stack:
  #estructura --> atributos
  def __init__(self):
    self.__stack: list[int] = [] #estructura de datos implementadora

  #comportamiento --> métodos
  def push(self, element: int) -> None: #agrega después del tope
    self.__stack.append(element)
    return None

  def pop(self) -> int: #retorna y elimina el tope
    if(len(self.__stack) == 0):
      raise TypeError("No puedes hacer pop... La pila está vacía")
    return self.__stack.pop()

  def peek(self) -> int: #retorna el tope
    if(len(self.__stack) == 0):
      raise TypeError("No puedes hacer peek... La pila está vacía")
    return self.__stack[-1]

  def add_from_list(self, data: list[int]) -> None:
    for i in data:
      self.push(i)

  def __repr__(self) -> str:
    return f"{self.__stack}"

  def __len__(self) -> int:
    return len(self.__stack)

def calcular_puntaje(pacientes, pesos):
    calculo = {}
    for i in pacientes:
        for clave, valor in i.items():
            if clave == "nombre":
                nombre = valor
            if clave == "edad":
                edad = valor
            if clave == "diagnostico":
                puntaje_max = 0
                for condicion, puntaje in pesos.items():
                    if condicion in valor.lower():
                        puntaje_max += puntaje
                        punt = puntaje_max + edad/100
                calculo[nombre] = punt

    return calculo




pacientes = [
    {"nombre": "Ana", "edad": 72, "diagnostico": "Desmayos frecuentes y dolor en el corazón"},
    {"nombre": "Luis", "edad": 34, "diagnostico": "Dolor de cabeza intenso y mareo"},
    {"nombre": "Marta", "edad": 65, "diagnostico": "Dolor en el corazón"},
    {"nombre": "Diego", "edad": 50, "diagnostico": "Caída con golpe en la cabeza y náuseas"}
]

pesos = {
    "dolor en el corazón": 10,
    "desmayos frecuentes": 15,
    "mareo": 5,
    "dolor de cabeza": 3,
    "náuseas": 2,
    "golpe en la cabeza": 8
}
print(calcular_puntaje(pacientes, pesos))

calculo = calcular_puntaje(pacientes,pesos)
cola = PriorityQueue("max")
for nombre, puntaje in calculo.items():
    cola.enqueue((nombre, puntaje))




def ciclo_infinito(pacientes,pesos):
    while True:

        accion = input("uqe accion")
        match accion:
            case "atender":
                if len(cola) == 0:
                    print("Ya no quedan pacientes")
                else:
                    print(cola.dequeue())
            case "ver":
                if len(cola) == 0:
                    print("Ya no quedan pacientes")
                else:
                    print(cola.peek())
            case "agregar":
                nombre = input("ingresa el nombre")
                try:
                    edad = int(input("Ingresa la edad: "))

                except:
                    print("Edad inválida")
                    continue

                diagnostico = input("ingresa el diagnostico")
                pacientes.append({"nombre":nombre, "edad":edad,"diagnostico": diagnostico})
                def nuevo(nombre,edad,diagnostico,pesos):
                    puntaje_max = 0
                    for condicion, puntaje in pesos.items():
                        if condicion in diagnostico.lower():
                            puntaje_max += puntaje
                            punt = puntaje_max + edad / 100
                    return (nombre,punt)
                nuevo_nombre = nuevo(nombre,edad,diagnostico,pesos)[0]
                nuevo_puntaje = nuevo(nombre, edad, diagnostico, pesos)[1]
                cola.enqueue((nuevo_nombre,nuevo_puntaje))
            case "listar":
                pila = Stack()
                n=int(input("Cuántos quieres listar"))
                if n > len(cola):
                    print(f"Solo hay {len(cola)} pacientes")
                else:
                    for _ in range(n):
                        pila.push(cola.dequeue())
                        print(pila.peek())
                    for _ in range(n):
                        cola.enqueue(pila.pop())

            case "salir":
                break


ciclo_infinito(pacientes,pesos)