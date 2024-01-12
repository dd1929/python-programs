# Tic Tac Toe!
# Uses the MiniMax algorithm to defeat you ;D

# imports and stuff
import random
from math import ceil, inf

# returns a fresh, empty board
def new_board():
	return [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
	
# prints the board to screen nicely (I guess)
def show_board(board):
	print('\n-----------')
	print('Present state of board:')
	print('-----------')
	print("", board[0][0], "|", board[0][1], "|", board[0][2], "")
	print("——— ——— ———")
	print("", board[1][0], "|", board[1][1], "|", board[1][2], "")
	print("——— ——— ———")
	print("", board[2][0], "|", board[2][1], "|", board[2][2], "")
	print('-----------\n')

# returns the number of free spots in the board
def free_spots(board):
	free_spots = 0
	for row in range(3):
		for col in range(3):
			if board[row][col] in 'abcdefghi':
				free_spots += 1
	return free_spots

# tells if someone has won yet or not	
def winner(board):
	
	for num in range(3):
		
		# horizontally
		if board[num][0] == board[num][1] and board[num][1] == board[num][2]:
			return board[num][0]
			
		# vertically
		if board[0][num] == board[1][num] and board[1][num] == board[2][num]:
			return board[0][num]
	
	# diagonally
	if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
		return board[1][1]
	if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
		return board[1][1]
	
	# checks if the board is filled up with no winner, then it's a tie
	for row in range(3):
		for col in range(3):
			if not (board[row][col] == 'X' or board[row][col] == 'O'):
				return None
	else:
		return 'Nobody'	

# plays a move at a chosen spot for a chosen player
def play_move(board, spot, player):
	for row in range(3):
		for col in range(3):
			if (spot not in 'XO') and board[row][col] == spot:
				board[row][col] = player
				return True
	return False
	
# returns the best possible score for a player
def minimax(board, depth, is_maximising):
	if winner(board) == 'X': return 1
	elif winner(board) == 'O': return -1
	elif winner(board) == 'Nobody': return 0
	
	# return a score if we've already reached the deepest depth
	if depth == 0:
		if winner(board) == 'X': return 1
		elif winner(board) == 'O': return -1
		else: return 0
		
	if is_maximising:
		bestScore = -inf
		for row in range(3):
			for col in range(3):
				if board[row][col] in 'abcdefghi':
					temp = board[row][col]
					board[row][col] = 'X'
					score = minimax(board, depth-1, False)
					board[row][col] = temp
					bestScore = max(score, bestScore)
		return bestScore # best maximum score possible
		
	else:
		bestScore = inf
		for row in range(3):
			for col in range(3):
				if board[row][col] in 'abcdefghi':
					temp = board[row][col]
					board[row][col] = 'O'
					score = minimax(board, depth-1, True)
					board[row][col] = temp
					bestScore = min(score, bestScore)
		return bestScore # best minimum score possible

# returns the best possible move spot for a player and given depth
def best_move(board, player, depth):
	best_score = -inf if player == 'X' else inf
	for row in range(3):
		for col in range(3):
			if board[row][col] in 'abcdefghi':
				temp = board[row][col]
				board[row][col] = player
				is_maximising = not (player == 'X')
				score = minimax(board, depth-1, is_maximising)
				if player == 'X':
				    if score > best_score:
					    best_score = score
					    best_move_spot = temp
				else:
				    if score < best_score:
					    best_score = score
					    best_move_spot = temp
				board[row][col] = temp
	return best_move_spot
	
# takes move input from a human player and plays it
def human_input(board, player_1):
	while True:
		player_name = 'Player 1' if player_1 else 'Player 2'
		symbol = 'X' if player_1 else 'O'
		spot = input(player_name + ', enter letter of spot to enter "' + symbol + '": ')
		if play_move(board, spot, symbol):
			print(player_name, ' plays "', symbol, '" at ', spot, sep='')
			return not player_1
		else:
			print('That spot isn\'t there. Try again!')

# starts a game against the computer
def play_computer(board):
	print('\nChoose difficulty, 1 or 2:')
	print('1. Easy')
	print('2. Medium')
	print('3. Impossible')
	diff = input('> ')
		
	print('\nChoose who goes first, 1 or 2:')
	print('1. You')
	print('2. Computer')
	player_1 = True if input('> ') == '1' else False
	
	# easy difficulty - computer plays random moves	
	if diff == '1':
		while(not winner(board)):
			show_board(board)
			if player_1:
				player_1 = human_input(board, player_1)
				continue
			else:
				while True:
					spot = random.choice('abcdefghi')
					if play_move(board, spot, 'O'):
						player_1 = True
						print('Computer plays "O" at', spot)
						break
				continue
	
	# medium difficulty - computer plays best move based on limited depth	
	elif diff == '2':
		while(not winner(board)):
			show_board(board)
			if player_1:
				player_1 = human_input(board, player_1)
				continue
			else:
				best_move_spot = best_move(board, 'O', ceil(free_spots(board)/2))
				play_move(board, best_move_spot, 'O')
				player_1 = True
				print('Computer plays "O" at', best_move_spot)
				continue
	
	# impossible difficulty - computer plays best move based on full depth
	elif diff == '3':
		while(not winner(board)):
			show_board(board)
			if player_1:
				player_1 = human_input(board, player_1)
				continue
			else:
				best_move_spot = best_move(board, 'O', free_spots(board))
				play_move(board, best_move_spot, 'O')
				player_1 = True
				print('Computer plays "O" at', best_move_spot)
				continue

# starts a game between two human players			
def play_human(board):
	player_1 = True
	while(not winner(board)):
		show_board(board)
		player_1 = human_input(board, player_1)

def main():
	print('Welcome to Tic Tac Toe!')
	
	while True:
	    print('\nChoose 1, 2 or 3:')
	    print('1. Play vs computer')
	    print('2. Play vs another human')
	    print('3. Exit')
	    choice = input('> ')
	    
	    if choice == '1':
	    	board = new_board()
	    	play_computer(board)
	    	print('Board:')
	    	show_board(board)
	    	print('-----------')
	    	print(winner(board), "wins!")
	    	print('-----------')
	    elif choice == '2':
	    	board = new_board()
	    	play_human(board)
	    	print('Board:')
	    	show_board(board)
	    	print('-----------')
	    	print(winner(board), "wins!")
	    	print('-----------')
	    elif choice == '3':
	    	print('Exiting program, thanks for playing! :D')
	    	break
	    else:
	    	print('Invalid input! :(')
	
if __name__ == "__main__":
	main()
	