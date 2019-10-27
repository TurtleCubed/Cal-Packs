from Pack import Pack
import random
from math import *
import numpy as np


class BogoPack(Pack):

    def __init__(self, n, m, dino_list):
        Pack.__init__(self, n, m, dino_list)

    def pack(self):
        NUM_ATTEMPTS = 10000
        attempts = NUM_ATTEMPTS
        dino_number = 0

        while attempts > 0:
            tray_copy = self.tray
            current_dino = self.dino_list[dino_number % len(self.dino_list)]
            # rotation_angle = random.random() * 180
            # current_dino = self.rotate_dino(current_dino, rotation_angle)
            # current_dino = self.remove_edges(current_dino)
            startx = random.randint(0, len(self.tray[0]) - len(current_dino[0]))
            starty = random.randint(0, len(self.tray) - len(current_dino))
            success = True
            for i in range(len(current_dino)):
                for j in range(len(current_dino[0])):
                    if tray_copy[starty + i][startx + j] == 1 and current_dino[i][j] == 1:
                        success = False

            if not success:
                attempts -= 1

            if success:
                for i in range(len(current_dino)):
                    for j in range(len(current_dino[0])):
                        if tray_copy[starty + i][startx + j] == 0 and current_dino[i][j] == 1:
                            tray_copy[starty + i][startx + j] = current_dino[i][j]
                dino_number += 1
                self.num_dinos += 1
                self.tray = tray_copy
                attempts = NUM_ATTEMPTS

        return self.tray

    def rotate_dino(self, dino_matrix, angle):

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
                    rotated[int(length // 2 - rot_vector[1])][int(length // 2 + rot_vector[0])] = 1

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