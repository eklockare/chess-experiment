from board_parts import ChessCoord

castling_moves_squares_and_rook_coord_dict = {
    str(ChessCoord('G', '8')): {'squares_in_between': [ChessCoord('G', '8'),
                                                       ChessCoord('F', '8')],
                                'rook_coord': ChessCoord('H', '8'),
                                'new_rook_coord': ChessCoord('F', '8')
                                },
    str(ChessCoord('B', '8')): {'squares_in_between': [ChessCoord('D', '8'),
                                                       ChessCoord('C', '8'),
                                                       ChessCoord('B', '8')],
                                'rook_coord': ChessCoord('A', '8'),
                                'new_rook_coord': ChessCoord('C', '8')
                                },
    str(ChessCoord('G', '1')): {'squares_in_between': [ChessCoord('G', '1'),
                                                       ChessCoord('F', '1')],
                                'rook_coord': ChessCoord('H', '1'),
                                'new_rook_coord': ChessCoord('F', '1')
                                },
    str(ChessCoord('B', '1')): {'squares_in_between': [ChessCoord('D', '1'),
                                                       ChessCoord('C', '1'),
                                                       ChessCoord('B', '1')],
                                'rook_coord': ChessCoord('A', '1'),
                                'new_rook_coord': ChessCoord('C', '1')
                                },
}
