import random as rd
class Person:
    def __init__(self):
        self.name: None|str = None
        self.position = (0,0)
        self.level_defense: int = 3
        self.color = 'Green'

class Matrix:
    def __init__(self, n: int):
        self.matrix: list[list[int|Person]] = []
        self.people: list[Person] = []
        self.n: int = n

    def create_people(self):
        positions = [(i, j) for i in range(self.n) for j in range(self.n)]
        rd.shuffle(positions)
        for i in range(self.n):
            person = Person()
            person.name = f'P{i+1}'
            person.position = (positions[i])
            self.people.append(person)
        return self.people

    def create_matrix(self):
        self.matrix = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for person in self.people:
            self.matrix[person.position[0]][person.position[1]] = person.name

    def start(self):
        patient_0 = rd.choice(self.people)
        patient_0.level_defense = 0
        patient_0.color = 'Red'

    def move(self):
        movements = ['UP', 'DOWN', 'RIGHT', 'LEFT', 'CUR', 'CUL', 'CDR', 'CDL']
        for person in self.people:
            movement = rd.choice(movements)
            a,b = person.position
            if movement == 'UP':
                if a-1 <= 0:
                    person.position = (a-1,b)
            elif movement == 'DOWN':
                if a+1 < self.n:
                    person.position = (a+1,b)
            elif movement == 'RIGHT':
                if b+1 < self.n:
                    person.position = (a,b+1)
            elif movement == 'LEFT':
                if b-1 >= 0:
                    person.position = (a,b-1)
            elif movement == 'CUR':
                if a-1 <= 0 or b+1 < self.n:
                    person.position = (a-1,b+1)
            elif movement == 'CUL':
                if a-1 <= 0 or b-1 >= 0:
                    person.position = (a-1,b-1)
            elif movement == 'CDR':
                if a+1 < self.n or b+1 < self.n:
                    person.position = (a+1,b+1)
            elif movement == 'CDL':
                if a+1 < self.n or b-1 >= 0:
                    person.position = (a+1,b+1)
    def infect(self):
        positions = []
        for person in self.people:
            positions.append(person.position)







