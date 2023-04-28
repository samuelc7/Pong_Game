class GameObject():
    '''
        Constructor:

        Creates a new GameObject
        Params:
            name  - the name/tag of the object which can be used to reference later
            type  - the type of object. Options are (rectangle or oval)
            x     - the x coordinate of their initial position
            y     - the y coordinate of their initial position
            w     - the width in pixels
            h     - the height in pixels
            color - the color of the object - default is white
    '''
    def __init__(self, name, type, x, y, w, h, color="white"):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.id = name
        self.color = color
        self.type = type
        self.speed = None
        self.num = NotImplemented
    
    '''
        Displays the GameObject onto the canvas passed in.
        Params:
            canvas - the canvas that the GameObject will be displayed on.
    '''
    def display(self, canvas):
        if self.type == "rectangle":
            canvas.create_rectangle(
                self.x - self.width, 
                self.y, 
                self.x + self.width, 
                self.y + self.height, 
                tags=(self.id,), 
                fill=self.color)
        elif self.type == "oval":
            self.num = canvas.create_oval(
                self.x - self.width,
                self.y,
                self.x + self.width,
                self.y + self.height,
                tags=(self.id,),
                fill=self.color)
    '''
        Returns the current coordinates of the GameObject
    '''
    def get_position(self):
        return (self.x, self.y)
    
    '''
        Sets the GameObjects position
        Params: 
            x - the x coordinate of the new position
            y - the y coordinate of the new position
    '''
    def set_position(self, x, y):
        self.x = x
        self.y = y

    '''
        This is to be called after any positional change. 
        This deletes the last display of the GameObject and then creates a new one 
        for the updated GameObject. 
    '''
    def update(self, canvas):
        canvas.delete(self.id)
        self.display(canvas)