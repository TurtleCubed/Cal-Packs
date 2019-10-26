from abc import ABC, abstractmethod


class Pack(ABC):

    def __init__(self, n, m, dino_list):
        self.dino_list = dino_list
        self.tray = [[0 for x in range(n)] for y in range(m)]
        self.fill = 0
        self.num_dinos = 0

    """
    pack takes in the dimensions of the "tray" and the list of dinosaurs 
    """
    @abstractmethod
    def pack(self):
        return None

    def percent_full(self):
        return 100 * self.fill / (len(self.tray) * len(self.tray[0]))