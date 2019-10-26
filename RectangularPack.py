test_matrix1 = [[0,0,0,0],[0,1,1,0],[1,0,1,0],[0,0,0,0],[0,0,0,0]]
test_matrix2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
test_matrix3 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
test_matrix4 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]


class RectangularPack():

    def print_matrix(matrix):
        """function that displays 2-d matrix"""


    def reduce_matrix(dino_matrix, rotation_angle = 0):
        """takes in a matrix, and returns the minimum sized rectangle. """
        def rotate_matrix(matrix, angle):
            """use aaron's matrix rotator"""
            """helper function that returns rotated matrix"""
            if angle == 0:
                rotated_matrix = matrix
            else:
                """need to implement rotation with linear alg"""
                #rotation matrix
                #rotated_matrix = rotation_matrix @ matrix
            return rotated_matrix

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