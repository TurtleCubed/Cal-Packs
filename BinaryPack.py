from math import sin, cos, pi
import numpy as np

from Display import *
from ImageReader import *
from Pack import Pack



class BinaryPack(Pack):

    def __init__(self, n, m, dino_list):
        super().__init__(n, m, dino_list)
        for dino in self.dino_list:
            dino = self.optimize_dino(dino)
        self.dino_list.sort(key=lambda x: len(x) * len(x[0]))


    def pack(self):
        def recursivePack(x_start, y_start, x_end, y_end):
            if x_start >= x_end or y_start >= y_end:
                return None
            fits = False
            x_inc = 0
            y_inc = 0
            for dino in self.dino_list:
                if x_end - x_start >= len(dino[0]) and y_end - y_start >= len(dino):
                    fits = True
                    for x in range(x_start, x_start + len(dino[0])):
                        for y in range(y_start, y_start + len(dino)):
                            if dino[y - y_start][x - x_start]:
                                self.tray[y][x] = 1
                    x_inc = len(dino[0])
                    y_inc = len(dino)
                    break
            if fits:
                recursivePack(x_start + x_inc, y_start, x_end, y_start + y_inc)
                recursivePack(x_start, y_start + y_inc, x_end, y_end)
        recursivePack(0, 0, len(self.tray[0]), len(self.tray))
        return self.tray

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

        return dino


test = [ImageReader.text_to_array("triceratops.dino")]

a = BinaryPack(800, 800, test)
image = Display.tray_to_image(a.pack())
image.show()