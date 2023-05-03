from GameObject import GameObject
from settings import *
import math
import numpy as np
from angles import normalize
class Ball(GameObject):
    def __init__(self, name, type, x, y, w, h, color="white"):
        super().__init__(name, type, x, y, w, h, color)
        self.angle = 300.0
        self.direction = 's'
        self.speed = 1
        self.updated_angle_last_move = False
        self.out_of_screen = False
    '''
        This calculates the next position based on the speed, angle, and direction.
        Returns: 
            (x, y) of the next position.
        TODO: this method needs to be finished. Include the angle and direction to get the next position. 
    '''
    def next_position(self):
        
        return(self.x, self.y)

    '''
        This deletes the previous display of the ball, 
        gets the next position, and then calls the display method.
    '''
    def update(self, canvas, player_position):
        new_x = self.x + math.cos(np.deg2rad(self.angle))
        new_y = self.y -math.sin(np.deg2rad(self.angle)) 

        # check if still in boundries
        player_x = player_position[0]
        player_y = player_position[1]

        if new_x > player_x - PLAYER_LENGTH and new_x < player_x + PLAYER_LENGTH and\
            new_y > player_y - PLAYER_HEIGHT and new_y < player_y + PLAYER_HEIGHT:
            self.angle = normalize(self.angle + 90.0)
        if new_x + self.width > GAME_CANVAS_WIDTH:
            self.angle = normalize(self.angle - 90.0)
        if new_x < 0:
            self.angle = normalize(self.angle + 90.0)
        if new_y + self.height > GAME_CANVAS_HEIGHT:
           self.out_of_screen = 2
        if new_y < 0:
           self.out_of_screen = 1
        self.x = new_x
        self.y = new_y

        canvas.delete(self.id)
        self.display(canvas)
