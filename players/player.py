from board_parts import white


class Player:
    def __init__(self, colour):
        self.colour = colour
        if colour == white:
            self.colour_name = "White"
        else:
            self.colour_name = "Black"
