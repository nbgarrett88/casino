import random

ROWS = 3
COLS = 3
MAX_LINES = ROWS + COLS + 2

item_set = ['A','B','C','D']
balance = 0

def ask_question(question_type):
    dict = {
        'deposit':['\nHow much money will you deposit?\n','ans > 0','\nAmount must be greater than 0'],
        'lines':[f'\nHow many lines do you want to play? (1-{MAX_LINES})\n','0 < ans <= MAX_LINES',f'\nNumber must be between 1 and {MAX_LINES}'],
        'bet': ['\nHow much do you wish to bet per line?\n','ans > 0','\nAmount must be greater than 0']
    }

    while True:
        ans = input(dict[question_type][0])

        if ans.isdigit():
            ans = int(ans)
            if eval(dict[question_type][1]):
                break
            else:
                print(dict[question_type][2])
        else:
            print('\nInput must be numeric')
    return ans

def pull_handle(item_set):
    res = []
    for column in range(COLS):
        line = []
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

def score_board(board, lines):
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
            score += 4

    dict = {}
    for line in range(len(board)):
        for ix, char in enumerate(board[line]):
            if (ix,char) in dict:
                dict[(ix,char)] += 1
            else:
                dict[(ix, char)] = 1
        for key, val in dict.items():
            if val == len(board):
                wins.append(key[0]+len(board)+1)
                score += 6

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        wins.append(MAX_LINES - 1)
        score += 8
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        wins.append(MAX_LINES)
        score += 8

    for line in wins:
        if line > lines:
            wins.remove(line)
            if 3 < line > 7:
                score -= 4
            if line > 6:
                score -= 5
            else:
                score -= 3

    if len(wins) == 0:
        return 0, 'LOSE', []
    else:
        return score, 'WIN', wins 

def leave_game():
    print(f'\nThank you for playing! You left with ${balance}\n')
    return 0
    
def continue_screen():
    answer = input('Enter to continue... (q to quit to menu)\n')
    if answer == 'q':
        menu_options()
    else:
        play_game()

def play_game():
    global balance

    if balance <= 0:
        print('\nYour balance is empty. Deposit cash to play.')
        menu_options()        
    
    if balance > 0:
        lines = ask_question('lines')
        bet = ask_question('bet')
        if bet * lines > balance:
            print('\nYour max bet exceeds your total balance.')
            bet = ask_question('bet')
        board = pull_handle(item_set)
        score, res, winners = score_board(board, lines)
        draw_board(board)
        if res == 'WIN':
            balance += (score * bet * len(winners)) - (bet * lines) 
            score = score * bet * len(winners)
        else: 
            balance -= bet * lines
            score = bet * lines * -1
        
        print(f'\nYou {res} ${score}! You hit on these lines: {winners}. New balance is ${balance}\n')
        continue_screen()

def menu_options():
    global balance

    print('\n1. Play game')
    print('2. Deposit cash')
    print('3. Get current balance')
    print('4. Quit')

    ans = input()

    match ans:
        case '1':
            play_game()
        case '2':
            balance = ask_question('deposit')
            menu_options()
        case '3':
            print(f'\nCurrent balance is: ${balance}')
            menu_options()
        case '4':
           balance = leave_game()
        case _:
            pass
        
def main():
    
    input('\nWelcome to the Slot Machine!')
    menu_options()
    
main()