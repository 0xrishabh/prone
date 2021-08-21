from src.engine import Engine
from src.database import Database
from src.ui import board_ui
import chess

## Basic Setup
database = Database()
position_eval = database.get_position_eval()
piece_eval = database.get_piece_eval()
engine = Engine(5,position_eval,piece_eval)
## END


def split(string):
	string.replace("\n","")
	return string.split("|")

def solve(puzzle,solution):
	global puzzle_solved
	solution = solution.split(",")
	board = chess.Board(puzzle)
	while solution:
		board_ui(board)
		move,evaluation = engine.find_move(board)
		print(move,evaluation)
		if move != board.parse_san(solution.pop(0)):
			#print("fail")
			return
		board.push(move)

		#Playing the opponent's move
		if solution:
			board.push_san(solution.pop(0))
	puzzle_solved += 1
	#print("success")


filename = "/home/cypher/Desktop/projects/chessPuzzle/puzzle.txt"
lines = open(filename).readlines()[:10]
total_puzzle = len(lines)
puzzle_solved = 0
progress = 0
for line in lines:
	print('-----------------------------------------')
	puzzle,solution,elo = split(line)
	solve(puzzle,solution)
	progress+=1
	print('-----------------------------------------')
print("{}/{}".format(puzzle_solved,total_puzzle))