from math import sin, cos, pi
import numpy as np

from Pack import Pack

test = [[1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1]]

result = [[0, 0, 0, 0, 0],
          [1, 0, 1, 1, 0],
          [1, 0, 0, 0, 1],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]

class BinaryPack(Pack):


    def pack(self):
        return None




a = BinaryPack()
print(a.optimizeDino(test))
