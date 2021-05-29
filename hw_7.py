#задача 1
matrix_a = [[31,22], [37,43], [51,16]]
matrix_b = [[49,22], [89,23], [54,16]]

class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        
    def __str__(self):
        return '\n'.join(map(str, self.matrix))

    
    def __add__(self, other):
        c =[]
        for i in range(len(self.matrix)):
            c.append([])
            for j in range(len(self.matrix[0])):
                c[i].append(self.matrix[i][j] + other.matrix[i][j])
        return '\n'.join(map(str, c))

mtr_a = Matrix (matrix_a)
mtr_b = Matrix (matrix_b)
print(mtr_a)
print("*"*20)
print(mtr_b)
print("*"*20)
print(mtr_a+mtr_b)
print("*"*20)


#задача 2
class Coat():
    def __init__(self, size):
        self.size = size
    @property
    def expenditure(self):
        coat_expenditure = self.size/6.5 + 0.5
        return round(coat_expenditure,2)

class Suit():
    def __init__(self, size):
        self.size = size

    def expenditure(self, height):
        suit_expenditure =2*height+0.3
        return round(suit_expenditure,2)

red_coat = Coat(44)
print(red_coat.expenditure)
blue_suit = Suit (1.75)
print(blue_suit.expenditure(1.75))
sum = red_coat.expenditure+blue_suit.expenditure(1.75)
print(f'Суммарные затраты ткани на пошив пальто и костюма {sum} м')


#задача 3
class Cell():
    def __init__(self,quantity):
        self.quantity = quantity


    def __add__(self, other):
        return (self.quantity+other.quantity)

    def __sub__(self, other):
        dif = self.quantity-other.quantity
        return (dif if  dif>0 else f'Вычитание клеток не возможно!')

    def __mul__(self, other):
        return (self.quantity*other.quantity)

    def __truediv__(self, other):
        return (round(self.quantity/other.quantity, 0))

    def make_order(self, cells):
        self.cells = cells
        rows = self.quantity//cells
        row = self.quantity % cells
        return '\n'.join(['*'*cells for _ in range (rows)]) +'\n'+'*'*row


cell_a = Cell(32)
cell_b = Cell(35)
print(cell_b+cell_a)
print(cell_b-cell_a)
print(cell_b*cell_a)
print(cell_b/cell_a)
print(cell_a.make_order(6))