''' 模拟一个三阶魔方'''
import numpy as np
from enum import Enum, unique

class MagicCube:
    def __init__(self):
        self.front = np.array([['y', 'y', 'y'], ['y', 'y', 'y'],['y', 'y', 'y']])
        self.back = np.array([['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']])
        self.top = np.array([['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']])
        self.bottom = np.array([['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']])
        self.left = np.array([['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]) 
        self.right = np.array([['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']])
    
    def show(self):
        print('front:')
        print(self.front)
        print('back:')
        print(self.back)
        print('top:')
        print(self.top)
        print('bottom:')
        print(self.bottom)
        print('left:')
        print(self.left)
        print('right:')
        print(self.right)

    def show_side(self, side):
        if isinstance(side, CubeSide):
            if side.value == 0:
                print('top:')
                print(self.top)
            if side.value == 1:
                print('bottom:')
                print(self.bottom)
            if side.value == 2:
                print('left:')
                print(self.left)
            if side.value == 3:
                print('right:')
                print(self.right)
            if side.value == 4:
                print('front:')
                print(self.front)
            if side.value == 5:
                print('back:')
                print(self.back)

    def top_turn(self):
        pass 

    def bottom_turn(self):
        pass

    def left_turn(self):
        pass
    
    def right_turn(self):
        pass
    
    def front_turn(self):
        pass

    def back_turn(self):
        pass

@unique
class CubeSide(Enum):
    Top = 0
    Bottom = 1
    Left = 2
    Right = 3
    Front = 4
    Back = 5

def main():
    cube = MagicCube()
    cube.show()


if __name__ == '__main__':
    main()