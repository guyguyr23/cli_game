class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y
        
    def get_position_x(self):
        return self.x

    def get_position_y(self):
        return self.y

    def get_next_possiotn_x(self, x=1):
        return Position(self.x + x , self.y)

    def get_next_possiotn_y(self, y=1):
        return Position(self.x, self.y + y)
    
    def get_previos_possiotn_x(self):
        return Position(self.x - 1 , self.y)

    def get_previos_possiotn_y(self):
        return Position(self.x, self.y - 1)

    def move_x(self, dx):
        self.x += dx

    def move_y(self, dy):
        self.y += dy

    def move_to_postion(self, dx, dy):
        self.x = dx
        self.y = dy

    def copy(self):
        return Position(self.x, self.y)

    def __str__(self):
        return f"Position(x={self.x}, y={self.y})"