very WIP

The goal with this project is to create a fully working chess game played against an algorithm.


run with 'python chess.py'

TODO:

1. Pawn movement and taking (special)
    * one direction
    * two steps possible first move
    * taking only diagonal, movement only straight
    * en passant

2. All pieces but king general movement and taking
    * Rook straight
    * Bishop diagonal
    * Queen is rook + bishop
    * Knight is special case, can jump over pieces

3. Make piece movement that exposes the king illegal
    * Detect if king is exposed

4. Only move that covers the king is legal if in check
    * Restrict movement, detect which pieces can do that

5. Use 3. logic when moving the king

6. Castling
    * Check if piece is blocking
    * Check if piece is attacking inbetween squares

7. Implement turns




