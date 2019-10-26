from math import sin, cos, pi, sqrt
import numpy as np

from Display import *
from ImageReader import *
from Pack import Pack



class BinaryPack(Pack):

    def __init__(self, n, m, dino_list):
        super().__init__(n, m, dino_list)
        for i in range(len(self.dino_list)):
            dino_list[i] = self.reduce_matrix(dino_list[i])
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
                    self.num_dinos += 1
                    for x in range(x_start, x_start + len(dino[0])):
                        for y in range(y_start, y_start + len(dino)):
                            if dino[y - y_start][x - x_start]:
                                self.tray[y][x] = 1
                    x_inc = len(dino[0])
                    y_inc = len(dino)
                    self.dino_list.append(self.dino_list.pop(self.dino_list.index(dino)))
                    break
            if fits:
                recursivePack(x_start + x_inc, y_start, x_end, y_start + y_inc)
                recursivePack(x_start, y_start + y_inc, x_end, y_end)
        recursivePack(0, 0, len(self.tray[0]), len(self.tray))
        return self.tray

    def reduce_matrix(self, dino_matrix):
        """takes in a matrix, and returns the minimum sized rectangle. through rotating and cutting"""
        possible_matrixes = [self.remove_edges(self.rotate_dino(dino_matrix, angle)) for angle in range(0, 181, 5)]
        area_matrixes = [len(matrix) * len(matrix[0]) for matrix in possible_matrixes]
        small_index = area_matrixes.index(min(area_matrixes))
        return possible_matrixes[small_index]

    def rotate_dino(self, dino_matrix, angle):

        angle = angle * pi/2
        length = int(sqrt((len(dino_matrix) ** 2 + len(dino_matrix[0]) ** 2)))
        rotated = [[0 for x in range(length)] for y in range(length)]

        origin_x = len(dino_matrix[0]) // 2
        origin_y = len(dino_matrix) // 2
        rotMat = [[cos(angle), -1 * sin(angle)],
                  [sin(angle), cos(angle)]]

        for y in range(len(dino_matrix)):
            for x in range(len(dino_matrix[0])):
                if dino_matrix[y][x]:
                    vector = [x - origin_x, origin_y - y]
                    rot_vector = np.matmul(rotMat, vector)
                    rotated[int(length//2 - rot_vector[1])][int(length//2 + rot_vector[0])] = 1

        return rotated

    def remove_edges(self, matrix):
        """Inputting a matrix of ones and zeros, """
        rows = len(matrix)
        """remove excess rows"""
        new_matrix = []
        for i in range(rows):
            if not sum(matrix[i]) == 0:
                """delete row"""
                new_matrix.append(matrix[i])
        cols = len(new_matrix[0])
        """remove excess columns"""
        col_to_keep = []
        for i in range(cols):
            columns = [row[i] for row in new_matrix]
            if not sum(columns) == 0:
                col_to_keep += [i]

        new_matrix = [[rows[i] for i in col_to_keep] for rows in new_matrix]

        return new_matrix


