from abc import ABC, abstractmethod


class Pack(ABC):

    def __init__(self, n, m, dino_list):
        self.dino_list = dino_list
        self.tray = [[0 for x in range(n)] for y in range(m)]
        self.fill = 0
        self.num_dinos = 0

    """
    Returns a 2 dimensional array representing the packed tray
    """
    @abstractmethod
    def pack(self):
        return None

    def percent_full(self):
        num_full = 0
        for i in range(len(self.tray)):
            for j in range(len(self.tray[0])):
                if self.tray[i][j] == 1:
                    num_full += 1
        return 100 * num_full / (len(self.tray) * len(self.tray[0]))
