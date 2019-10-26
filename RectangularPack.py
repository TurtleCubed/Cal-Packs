test_matrix1 = [[0,0,0,0],[0,1,1,0],[1,0,1,0],[0,0,0,0],[0,0,0,0]]
test_matrix2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
test_matrix3 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
test_matrix4 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

from math import sin, cos, pi
import numpy as np

from Pack import Pack


class RectangularPack():

    def print_matrix(matrix):
        """function that displays 2-d matrix"""


    def reduce_matrix(dino_matrix, rotation_angle = 0):
        """takes in a matrix, and returns the minimum sized rectangle. """

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

        return rotate_matrix(remove_edges(dino_matrix),rotation_angle)

a = RectangularPack.reduce_matrix(test_matrix1)
print(a)