class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def get_area(self):
        return self.x * self.y


    def __repr__(self):
        return f'<class "Retangulo({self.x}, {self.y}">'


    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

r1 = Retangulo(10, 8)
r2 = Retangulo(5, 8)
r3 = r1 + r2
print(r3)
print(r1.get_area())