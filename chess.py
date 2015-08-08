# -*- coding: utf-8 -*-
from detect_check_mate import detect_if_king_is_mate
from drawing import draw_board
from board_parts import chess_coord_to_grid_coord, white, black
from players.random_player import RandomPlayer
from starting_pieces import starting_pieces
from players.human_player import HumanPlayer

check_mate = False
white_player = HumanPlayer(white)
black_player = RandomPlayer(black)
player_who_has_turn = white_player
other_player = black_player
global pieces
pieces = starting_pieces
turn_number = 0
global last_moved_piece_new_coord
last_moved_piece_new_coord = None
global last_moved_piece_old_coord
last_moved_piece_old_coord = None

def get_players_order(turn_number):
    if turn_number % 2 == 0:
        return white_player, black_player
    else:
        return black_player, white_player

while not check_mate:
    draw_board(pieces, None, last_moved_piece_new_coord)
    piece_to_move, new_coordinates = player_who_has_turn.make_move(pieces, last_moved_piece_new_coord)
    last_moved_piece_new_coord = chess_coord_to_grid_coord(new_coordinates)
    last_moved_piece_old_coord = piece_to_move.grid_coord

    move_inspect_result = piece_to_move.inspect_move(pieces, new_coordinates)

    if move_inspect_result.possible_piece:
        pieces.remove(move_inspect_result.possible_piece)

    piece_to_move.update_coord(new_coordinates)
    if move_inspect_result.was_castling_attempt:
        move_inspect_result.castling_rook.update_coord(
            move_inspect_result.new_coord_rook)

    draw_board(pieces, last_moved_piece_old_coord, last_moved_piece_new_coord)
    check_mate = detect_if_king_is_mate(other_player.colour, pieces)
    if check_mate:
        print "Check mate!"

    turn_number += 1
    player_who_has_turn, other_player = get_players_order(turn_number)

print "Check mate! %s wins!" % player_who_has_turn.colour_name
