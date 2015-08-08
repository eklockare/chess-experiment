# -*- coding: utf-8 -*-
from detect_check_mate import detect_if_king_is_mate
import drawing as dr
from board_parts import chess_coord_to_grid_coord, white, black
from players.random_player import RandomPlayer
from starting_pieces import starting_pieces
from players.human_player import HumanPlayer
import copy


def select_piece(pieces, selected_coord, moved_to_coords, player_who_has_turn, other_player):
    dr.draw_board(pieces, selected_coord, moved_to_coords)
    print "%s's turn" % player_who_has_turn.colour_name

    selected_piece = player_who_has_turn.select_piece(pieces)
    move_piece(pieces, None, selected_piece, player_who_has_turn, other_player)

def move_piece(pieces, moved_to_coord, piece_to_move, player_who_has_turn, other_player):
    selected_coord = piece_to_move.grid_coord
    dr.draw_board(pieces, selected_coord, moved_to_coord)
    print "%s's turn" % player_who_has_turn.colour_name

    new_coordinates = player_who_has_turn.make_move(pieces, piece_to_move)

    move_inspect_result = piece_to_move.inspect_move(pieces, new_coordinates)

    if move_inspect_result.possible_piece:
        pieces.remove(move_inspect_result.possible_piece)

    piece_to_move.update_coord(new_coordinates)
    if move_inspect_result.was_castling_attempt:
        move_inspect_result.castling_rook.update_coord(
            move_inspect_result.new_coord_rook)
    moved_to_coord = chess_coord_to_grid_coord(new_coordinates)

    check_mate = detect_if_king_is_mate(other_player.colour, pieces)
    if check_mate:
        print "%s wins!" % player_who_has_turn.colour_name
        game_over()

    select_piece(pieces, None, moved_to_coord, other_player, player_who_has_turn)

select_piece(starting_pieces, None, None, HumanPlayer(white), RandomPlayer(black))

def game_over():
    print "Game over!"
    exit()
