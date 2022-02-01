theboard = {'top-l': ' ', 'top-m': ' ', 'top-r':' ',
		'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
		'low-l': ' ', 'low-m': ' ', 'low-r': ' '}

def printboard(board):
	print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
	print('-+-+-')
	print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
	print('-+-+-')
	print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])

def win(board):
	if board['top-l'] == 'x' and board['top-m'] == 'x' and board['top-r'] == 'x':
		print('x wins')
		return True
	if board['low-l'] == 'x' and board['mid-m'] == 'x' and board['mid-r'] == 'x':
		print('x wins')
		return True
	if board['low-l'] == 'x' and board['low-m'] == 'x' and board['low-r'] == 'x':
		print('x wins')
		return True
	if board['top-l'] == 'x' and board['mid-m'] == 'x' and board['low-r'] == 'x':
		print('x wins')
		return True
	if board['low-l'] == 'x' and board['mid-m'] == 'x' and board['top-r'] == 'x':
		print('x wins')
		return True
	if board['top-l'] == 'x' and board['mid-l'] == 'x' and board['low-l'] == 'x':
		print('x wins')
		return True
	if board['top-m'] == 'x' and board['mid-m'] == 'x' and board['low-m'] == 'x':
		print('x wins')
		return True
	if board['top-r'] == 'x' and board['mid-r'] == 'x' and board['low-r'] == 'x':
		print('x wins')
		return True

	if board['top-l'] == 'o' and board['top-m'] == 'o' and board['top-r'] == 'o':
		print('o wins')
		return True
	if board['low-l'] == 'o' and board['mid-m'] == 'o' and board['mid-r'] == 'o':
		print('o wins')
		return True
	if board['low-l'] == 'o' and board['low-m'] == 'o' and board['low-r'] == 'o':
		print('o wins')
		return True
	if board['top-l'] == 'o' and board['mid-m'] == 'o' and board['low-r'] == 'o':
		print('o wins')
		return True
	if board['low-l'] == 'o' and board['mid-m'] == 'o' and board['top-r'] == 'o':
		print('o wins')
		return True
	if board['top-l'] == 'o' and board['mid-l'] == 'o' and board['low-l'] == 'o':
		print('o wins')
		return True
	if board['top-m'] == 'o' and board['mid-m'] == 'o' and board['low-m'] == 'o':
		print('o wins')
		return True
	if board['top-r'] == 'o' and board['mid-r'] == 'o' and board['low-r'] == 'o':
		print('o wins')
		return True

turn = 'x'
for i in range(9):
	printboard(theboard)
	print(turn +' make your move')
	move = input()
	theboard[move] = turn
	if turn == 'x':
		turn = 'o'
	else:
		turn = 'x'
	if(win(theboard)):
		break
printboard(theboard)