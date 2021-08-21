import chess 
def board_ui(board):
    beauty_board = [[j for j in range(0,8)] for i in range(0,8)]
    #beauty_board[0][0] = "fuck"
    #print(beauty_board)
    graphical_repr = {
    'R':'♜', 'N':'♞', 'B':'♝', 'Q':'♛', 'K':'♚', 'P':'♟',
    'r':'♖', 'n':'♘', 'b':'♗', 'q':'♕', 'k':'♔', 'p':'♙',
    '.':'·'
    }
    for square in range(0,64):
        piece = board.piece_at(square)
        if piece:
            beauty_board[square//8][square%8] = graphical_repr[piece.symbol()]
        else:
            beauty_board[square//8][square%8] = graphical_repr['.']
    beauty_board = list(reversed(beauty_board))	
    print("-------------------------------------")	
    for row in range(len(beauty_board)):
        print((len(beauty_board)-row),end=" ")
        print(' '.join(beauty_board[row]))
    print("  a b c d e f g h")
    print("-------------------------------------")

def is_game_over(board):
    if board.can_claim_draw() or board.is_stalemate() or board.is_insufficient_material():
        return True,"It's a draw"
    elif board.is_checkmate():
        return True (best_move,-20000) if board.turn else (best_move,20000)