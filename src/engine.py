import chess
class Engine():
	def __init__(self, depth, position_eval, piece_eval):
		self.depth = depth
		self.position_eval = position_eval
		self.piece_eval = piece_eval
	def genereate_legal_moves(self,board):
		return board.legal_moves
	def get_ordered_moves(self,board):
		'''
			Ordering moves help in alpha-beta pruning
			Priority:
				- Checks
				- Promotion
				- Captures
		'''
		ordered_moves = [[],[],[],[]]
		for move in self.genereate_legal_moves(board):
			if board.gives_check(move):
				ordered_moves[0].append(move)
			elif move.promotion:
				ordered_moves[1].append(move)
			elif board.is_capture(move):
				ordered_moves[2].append(move)
			else:
				ordered_moves[3].append(move)
		ordered_moves = [move for order in ordered_moves for move in order]
		return ordered_moves
	def search(self,board,depth,alpha,beta,maximizing_player):
		# Check if the game is over or search depth is reached
		best_move = None
		if depth == 0:
			return (best_move,self.evaluate(board)) 
		elif board.can_claim_draw() or board.is_stalemate() or board.is_insufficient_material():
			return (best_move,0)
		elif board.is_checkmate():
			return (best_move,-20000) if board.turn else (best_move,20000)

		# Recursive Search Logic
		if maximizing_player:
			evaluation = -float("inf")
			for move in self.get_ordered_moves(board):
				board.push(move)	
				_,new_eval = self.search(board,depth-1,alpha, beta,not maximizing_player)
				board.pop()
				if new_eval>=evaluation:
					best_move = move
					evaluation = new_eval 
					alpha = max(alpha, evaluation)

				if beta <= alpha:
					break
		else:
			evaluation = float("inf")
			for move in self.get_ordered_moves(board):
				board.push(move)
				_,new_eval = self.search(board,depth-1, alpha, beta,not maximizing_player)
				board.pop()
				if new_eval<=evaluation:
					best_move = move
					evaluation = new_eval
					beta = min(evaluation, beta)
				if beta <= alpha:
					break
				
		return best_move,evaluation
	def find_move(self,board):
		alpha,beta = float("-inf"),float("inf")
		
		# board.turn return 1 for white and 0 for black
		maximizing_player = board.turn 
		
		best_move,evaluation = self.search(board,self.depth,alpha,beta,maximizing_player)
		return best_move,evaluation

	def play(self,board):
		best_move, _ = self.find_move(board)
		if best_move:
			board.push(best_move)

	def evaluate(self,board):
		white,black = 0,0
		for square in chess.SQUARES:
		    piece = board.piece_at(square)
		    if not piece:
		        continue
		    elif piece.color == chess.WHITE:
		        white += self.piece_eval[piece.piece_type] + self.position_eval[piece.piece_type][square]
		    else:
		        black += self.piece_eval[piece.piece_type] + list(reversed(self.position_eval[piece.piece_type]))[square]
		return white - black
