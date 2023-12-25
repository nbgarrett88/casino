import random

ROWS = 3
COLS = 3
MAX_LINES = 8

item_set =['A','B','C','D']

def get_deposit():
    while True:
        amt = input('How much money will you deposit?\n')
        
        if amt.isdigit():
            amt = int(amt)
            if amt > 0:
                break
            else:
                print('Amount must be greater than 0')
        else:
            print('Amount must be numeric')
    return amt
    
def get_lines():
    while True:
        lines = input(f'How many lines do you want to play? (1-{MAX_LINES})\n')
        
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print(f'Input must be between 1 and {MAX_LINES}')
        else:
                print('Input must be numeric')
    return lines
    
def place_bet():
    while True:
        bet = input('How much do you wish to bet per line?\n')
        
        if bet.isdigit():
            bet = int(bet)
            if bet > 0:
                break
            else:
                print('Amount must be greater than 0') 
        else:
            print('Amount must be numeric')
    return bet

def pull_handle(item_set):
    res = []
    for column in range(COLS):
        line=[]
        for rows in range(ROWS):
            line.append(random.choice(item_set))
        res.append(line)
    return res

def draw_board(board):
    print()
    for row in range(len(board[0])):
        for i, column in enumerate(board):
            if i != len(board)-1:
                print(column[row],end=' | ')
            else:
               print(column[row])

def score_board(board):
    wins = []
    score = 0
    for line in range(len(board)):
        count = 0
        for char in board[line]:
            found_char = board[line][0]
            if char == found_char:
                count += 1
        if count == len(board[line]):
            wins.append(line+1)
            score += 3
    
    if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        wins.append(4)
        score += 4
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        wins.append(5)
        score += 4
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        wins.append(6)
        score += 4
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        wins.append(7)
        score += 5
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        wins.append(7)
        score += 5

    if len(wins) == 0:
        return 0, 'LOSE', 0
    else:
        return score, 'WIN', wins
        
def leave_game(balance):
    answer = input('Enter to continue... (q to quit)\n')
    if answer == 'q':
        print(f'Thank you for playing! You left with ${balance}\n')
        return 0
    else:
        return balance
    
def play_game():
        balance = get_deposit()
        
        while balance > 0:
            lines = get_lines()
            bet = place_bet()
            if bet * lines > balance:
                print('Your max bet exceeds your total balance.')
                bet = place_bet()
            board = pull_handle(item_set)
            score, res, winners = score_board(board)
            draw_board(board)
            if res == 'WIN':
                balance += (score * bet * len(winners)) - (bet * lines) 
                score = score * bet * len(winners)
            else: 
                balance -= bet * lines
                score = bet * lines * -1
            
            print(f'\nYou {res} ${score}! You hit on these lines: {winners}. New balance is ${balance}\n')
            balance =  leave_game(balance)

def main():
    
    answer = input('Welcome to the Slot Machine!\nWould you like to play? (y or n)\n')
    if answer == 'y':
        play_game()
    
main()