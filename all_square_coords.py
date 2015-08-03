
from board_parts import NUM_ROWS, NUM_COLS, GridCoord, grid_coord_to_chess_coord
import util


def make_row(columns):
    return lambda row_num: zip(([row_num] * len(columns)), columns)


all_coords = util.flatten_list(map(make_row(NUM_COLS), NUM_ROWS))
all_grid_coords = map(lambda coords: GridCoord(coords[0], coords[1]), all_coords)

all_chess_coords = map(grid_coord_to_chess_coord, all_grid_coords)
