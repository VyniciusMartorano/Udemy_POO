from enum import Enum, auto

class Directions(Enum):
    up = auto()     #gera valores insignificantes
    down = auto()   # apenas para fazer funcionar o codigo
    right = auto()
    left = auto()


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction')
    else:
        print(f'Moving {direction.name}')


if __name__ == "__main__":
    move(Directions.up)
    move(Directions.down)
    move(Directions.left)
    move(Directions.right)

print('#'*30)
#mostrar opções dentro de Directions
for direction in Directions:
    print(f'Value: {direction.value}')
    print(f'name: {direction.name}')
    print('#' * 30)











