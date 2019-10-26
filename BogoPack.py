from Pack import Pack
import random

class BogoPack(Pack):

    def __init__(self, n, m, dino_list):
        Pack.__init__(self, n, m, dino_list)

    def pack(self):
        NUM_ATTEMPTS = 10000
        attempts = NUM_ATTEMPTS
        dino_number = 0

        while attempts > 0:
            trayCopy = self.tray
            current_dino = self.dino_list[dino_number % len(self.dino_list)]
            startx = random.randint(0, len(self.tray[0]) - len(current_dino[0]))
            starty = random.randint(0, len(self.tray) - len(current_dino))
            success = True
            for i in range(len(current_dino)):
                for j in range(len(current_dino[0])):
                    if trayCopy[starty + i][startx + j] == 0 and current_dino[i][j] == 0:
                        trayCopy[starty + i][startx + j] = 0
                    elif trayCopy[starty + i][startx + j] == 0 and current_dino[i][j] == 1:
                        trayCopy[starty + i][startx + j] = 1
                    elif trayCopy[starty + i][startx + j] == 1 and current_dino[i][j] == 0:
                        trayCopy[starty + i][startx + j] = 1
                    else:
                        success = False
                        attempts -= 1

            if success:
                dino_number += 1
                self.num_dinos += 1
                self.tray = trayCopy
                attempts = NUM_ATTEMPTS
        '''
        dino_number = 0
        trayCopy = self.tray
        current_dino = self.dino_list[dino_number % len(self.dino_list)]
        startx = random.randint(0, len(self.tray[0]) - len(current_dino[0]))
        starty = random.randint(0, len(self.tray) - len(current_dino))
        for i in range(len(current_dino)):
            for j in range(len(current_dino[0])):
                if trayCopy[starty + i][startx + j] == 0 and current_dino[i][j] == 0:
                    trayCopy[starty + i][startx + j] = 0
                elif trayCopy[starty + i][startx + j] == 0 and current_dino[i][j] == 1:
                    trayCopy[starty + i][startx + j] = 1
                elif trayCopy[starty + i][startx + j] == 1 and current_dino[i][j] == 0:
                    trayCopy[starty + i][startx + j] = 1
                else: 
                    
                trayCopy[starty + i][startx + j] = current_dino[i][j]
        self.tray = trayCopy
        '''
        return self.tray


