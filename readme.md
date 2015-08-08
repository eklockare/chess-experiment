
The goal with this project is to create a fully working chess game played against an algorithm.


run with 'python chess.py'

TODO:

1. Pawn movement and taking (special)
    * ~~one direction~~
    * ~~two steps possible first move~~
    * ~~taking only diagonal, movement only straight~~
    * ~~en passant~~

2. All other pieces but king and knight general movement and taking
    * ~~Rook straight~~
    * ~~Bishop diagonal~~
    * ~~Queen is rook + bishop~~
    * ~~Knight is special case, can jump over pieces~~

3. Make piece movement that exposes the king illegal
    * ~~Detect if king is exposed~~

4. Only move that covers the king is legal if in check
    * ~~Restrict movement, detect if a piece is allowed to move~~

5. Use 3. logic when moving the king
    * ~~Restrict king movement~~

6. Castling
    * ~~Check if piece is blocking~~
    * ~~Move both rook and king~~
    * ~~Check that neither rook nor king have been moved during the game~~
    * ~~Check if piece is attacking in between squares~~
    * ~~Check if king is in check before castling~~
    * ~~Check if king would be in check after castling~~

7. Can't take king
    * ~~Block enemies from taking the king~~

8. Check mate
    * ~~Detect when it's check mate~~

9. Implement turns
    * ~~Make Player modules that can be played be a human or by the computer~~

10. Implement queening
    * When pawn reaches enemy back rank, make choice to have new piece

11. Implement draw detection
    * When no move can be made but it's not check mate
    * When only the same move can be made over and over

FIXME:
1. Castling doesn't work when playing
2. You shouldn't have to reselect piece when you tried to make an invalid move
3. Redraw board after invalid move attempt
