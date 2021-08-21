from src.engine import Engine
from src.database import Database
from src.ui import board_ui
import chess
board = chess.Board()

database = Database()
position_eval = database.get_position_eval()
piece_eval = database.get_piece_eval()
computer = Engine(3,position_eval,piece_eval)

while not board.is_game_over():
    board_ui(board)
    user_move = chess.Move.from_uci(input("MOVE: "))
    while user_move not in board.legal_moves:
        user_move = chess.Move.from_uci(input("MOVE: "))
    board.push(user_move)
    computer.play(board)