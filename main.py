import tkinter
from tkinter import Button, Canvas, Frame, BOTTOM, LEFT
from loguru import logger
from Player import Player
from Ball import Ball
from settings import *

GAME_ON = False
player1 = None
bot = None
ball = None
after_listener_id = 0

class PongGame():
    def __init__(self):
        self.game_on = False
        self.player1 = None
        self.bot = None
        self.ball = None
        self.game_canvas = None
        self.window = None
    
    def start_game(self):
        logger.debug("Starting...")
        print("Starting...")

        self.game_on = True

        self.bot = Player(
            name="BOT", 
            type="rectangle", 
            x=BOT_START_X, 
            y=BOT_START_Y, 
            w=BOT_LENGTH,
            h=BOT_HEIGHT,
            color=BOT_COLOR
        )
        self.player1 = Player(
            name="PLAYER",
            type="rectangle",
            x=PLAYER_START_X,
            y=PLAYER_START_Y,
            w=PLAYER_LENGTH,
            h=PLAYER_HEIGHT,
            color=PLAYER_COLOR
        )
        self.ball = Ball(
            name="Ball",
            type="oval",
            x=BALL_START_X,
            y=BALL_START_Y,
            w=BALL_LENGTH,
            h=BALL_HEIGHT,
            color=BALL_COLOR
        )
        self.display()
        self.window.event_generate('<Motion>', warp=True, x=PLAYER_START_X + PLAYER_LENGTH, y=PLAYER_START_Y)
        self.window.after(3, self.update)

    def display(self):
        self.bot.display(self.game_canvas)
        self.player1.display(self.game_canvas)
        self.ball.display(self.game_canvas)
        
    def setup(self):
        logger.add("logs/log_file_{time}.log")
        self._create_window()
        self._create_game_canvas()
        self._display_mid_line()
       
        self.game_canvas.pack()

        button_frame = Frame(self.window)
        button_frame.pack(side=BOTTOM)

        start_button = Button(button_frame, text="Start", width=25, command=self.start_game)
        start_button.pack(side=LEFT, padx=10)
        exit_button = Button(button_frame, text="Exit", width=25, command=self.end_game)
        exit_button.pack(side=LEFT, padx=10)

    def run(self):
        self.window.mainloop()

    def update(self):
        if self.ball.out_of_screen:
            self.reset_game()
            return
        self.ball.update(self.game_canvas, self.player1.get_position())
        self.window.after(3, self.update)

    def reset_game(self):
        print("Reseting...")
        self.game_canvas.delete(["BOT", "PLAYER1", "BALL"])
        self.start_game()
    
    def end_game(self):
        print("Exiting...")
        self.game_on = False
        self.window.destroy()

    def _mouse_movement_call_back(self, e):
        if not self.game_on:
            return
        if e.x > 0 and e.x < GAME_CANVAS_WIDTH and \
            e.y < GAME_CANVAS_HEIGHT and e.y > GAME_CANVAS_HEIGHT / 2:
            x = e.x
            y = e.y
            self.player1.set_position(x,y)
            self.player1.update(self.game_canvas)
    
    def _create_window(self):
        self.window = tkinter.Tk()
        self.window.title("Pong Game")
        self.window.bind("<Motion>", self._mouse_movement_call_back)
    
    def _create_game_canvas(self):
        self.game_canvas = Canvas(
            self.window, 
            width=GAME_CANVAS_WIDTH, 
            height=GAME_CANVAS_HEIGHT
        )
        self.game_canvas.create_rectangle(
            0, 
            0, 
            GAME_CANVAS_WIDTH, 
            GAME_CANVAS_HEIGHT, 
            fill="black"
        )

    def _display_mid_line(self):
        for i in range(0, GAME_CANVAS_WIDTH, 5):
            self.game_canvas.create_line(
                i, 
                GAME_CANVAS_HEIGHT / 2, 
                i+1, GAME_CANVAS_HEIGHT / 2, 
                fill="white"
            )

pong_game = PongGame()
pong_game.setup()
pong_game.run()