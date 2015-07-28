very WIP

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
    * Check that neither rook nor king have been moved during the game
    * Check if piece is attacking in between squares
    * Check if king is in check before castling
    * Check if king would be in check after castling

7. Can't take king
    * Block enemies from taking the king

8. Check mate
    * Detect when it's check mate

9. Implement turns
    * Make Player modules that can be played be a human or by the computer



