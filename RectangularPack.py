test_matrix1 = [[0,0,0,0],
                [0,1,1,0],
                [1,0,1,0],
                [0,0,0,0]]
test_matrix2 = [[0, 0, 0, 0, 0],
                [1, 0, 1, 1, 0],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
test_matrix3 = [[0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0]]

from math import sin, cos, pi
import numpy as np

from Pack import Pack


class RectangularPack(Pack):

    def print_matrix(self, matrix):
        """function that displays 2-d matrix in some viewable form"""


    def reduce_matrix(self, dino_matrix):
        """takes in a matrix, and returns the minimum sized rectangle. through rotating and cutting"""

        def rotate_dino(angle):

            rotated = [[0 for x in range(len(dino_matrix))] for y in range(len(dino_matrix[0]))]

            origin_x = len(dino_matrix[0]) // 2
            origin_y = len(dino_matrix) // 2
            rotMat = [[cos(angle), -1 * sin(angle)],
                      [sin(angle), cos(angle)]]

            for y in range(len(rotated)):
                for x in range(len(rotated[0])):
                    if dino_matrix[y][x]:
                        vector = [x - origin_x, origin_y - y]
                        rot_vector = np.matmul(rotMat, vector)
                        rot_vector[0] = max(-origin_x, min(rot_vector[0], origin_x))
                        rot_vector[1] = max(-origin_y, min(rot_vector[1], origin_y))
                        rotated[int(round(origin_y - rot_vector[1]))][int(round(origin_x + rot_vector[0]))] = 1

            return rotated

        def remove_edges(matrix):
            """Inputting a matrix of ones and zeros, """
            rows = len(matrix)
            """remove excess rows"""
            new_matrix =[]
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

            new_matrix =[[rows[i] for i in col_to_keep] for rows in new_matrix]

            return new_matrix
        possible_matrixes = [remove_edges(rotate_dino(angle)) for angle in range(0,181,5)]
        area_matrixes = [len(matrix)*len(matrix[0]) for matrix in possible_matrixes]
        small_index = area_matrixes.index(min(area_matrixes))
        return possible_matrixes[small_index]

a = RectangularPack.reduce_matrix(1,test_matrix3)
print(a)
