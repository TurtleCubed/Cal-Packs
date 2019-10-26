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

    def optimize_dino(self, dino):

        def rotate_dino(angle):

            rotated = [[0 for x in range(len(dino))] for y in range(len(dino[0]))]

            origin_x = len(dino[0]) // 2
            origin_y = len(dino) // 2
            rotMat = [[cos(angle), -1 * sin(angle)],
                      [sin(angle), cos(angle)]]

            for y in range(len(rotated)):
                for x in range(len(rotated[0])):
                    if dino[y][x]:
                        vector = [x - origin_x, origin_y - y]
                        rot_vector = np.matmul(rotMat, vector)
                        rot_vector[0] = max(-origin_x, min(rot_vector[0], origin_x))
                        rot_vector[1] = max(-origin_y, min(rot_vector[1], origin_y))
                        rotated[int(round(origin_y - rot_vector[1]))][int(round(origin_x + rot_vector[0]))] = 1

            return rotated


a = BinaryPack()
print(a.optimizeDino(test))
