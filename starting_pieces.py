from board_parts import black, ChessCoord, white
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook
from directions import go_south, go_north

starting_pieces = [
    # black pawns
    Pawn(ChessCoord('A', '7'), black, go_south),
    Pawn(ChessCoord('B', '7'), black, go_south),
    Pawn(ChessCoord('C', '7'), black, go_south),
    Pawn(ChessCoord('D', '7'), black, go_south),
    Pawn(ChessCoord('E', '7'), black, go_south),
    Pawn(ChessCoord('F', '7'), black, go_south),
    Pawn(ChessCoord('G', '7'), black, go_south),
    Pawn(ChessCoord('H', '7'), black, go_south),
    # black back row
    Rook(ChessCoord('A', '8'), black),
    Knight(ChessCoord('B', '8'), black),
    Bishop(ChessCoord('C', '8'), black),
    Queen(ChessCoord('D', '8'), black),
    King(ChessCoord('E', '8'), black),
    Bishop(ChessCoord('F', '8'), black),
    Knight(ChessCoord('G', '8'), black),
    Rook(ChessCoord('H', '8'), black),
    # white pawns
    Pawn(ChessCoord('A', '2'), white, go_north),
    Pawn(ChessCoord('B', '2'), white, go_north),
    Pawn(ChessCoord('C', '2'), white, go_north),
    Pawn(ChessCoord('D', '2'), white, go_north),
    Pawn(ChessCoord('E', '2'), white, go_north),
    Pawn(ChessCoord('F', '2'), white, go_north),
    Pawn(ChessCoord('G', '2'), white, go_north),
    Pawn(ChessCoord('H', '2'), white, go_north),
    # white back row
    Rook(ChessCoord('A', '1'), white),
    Knight(ChessCoord('B', '1'), white),
    Bishop(ChessCoord('C', '1'), white),
    Queen(ChessCoord('D', '1'), white),
    King(ChessCoord('E', '1'), white),
    Bishop(ChessCoord('F', '1'), white),
    Knight(ChessCoord('G', '1'), white),
    Rook(ChessCoord('H', '1'), white),
]
