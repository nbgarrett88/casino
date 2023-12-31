import numpy as np
import random

ROWS = 3
COLS = 3
MAX_LINES = ROWS + COLS + 2
ITEM_SET = ['A','B','C','D','X']

balance = 0

def menu_options():
    global balance

    print('\n1. Play game')
    print('2. Deposit cash')
    print('3. Get current balance')
    print('4. Quit')

    ans = input()

    match ans:
        case '1':
            prepare_game()
        case '2':
            balance += ask_question('deposit')
            menu_options()
        case '3':
            print(f'\nCurrent balance is: ${balance}')
            menu_options()
        case '4':
            leave_game()
        case _:
            pass

def prepare_game():     
    
    if balance <= 0:
        print('\nYour balance is empty. Deposit cash to play.')
        menu_options() 
    else:
        lines = ask_question('lines')
        bet = ask_question('bet')
        play_game(lines, bet)

def play_game(lines, bet):
    global balance
        
    if bet * lines > balance:
            print('\nYour max bet exceeds your total balance.')
            prepare_game()
    else:
        board = pull_handle(ITEM_SET)
        draw_board(board)
        score, res, winners = score_board(board, lines)
        
        if res == 'WIN':
            balance += (score * bet * len(winners)) - (bet * lines) 
            score = score * bet * len(winners)
            print(f'You {res} ${score}! You hit on these lines: {winners}. New balance is ${balance}\n')
        else: 
            balance -= bet * lines
            score = bet * lines
            print(f'You {res} -${score}! New balance is ${balance}\n')

        continue_screen(lines, bet)

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

def continue_screen(lines, bet):
    ans = input('Enter to continue... (c: change bet m: menu)\n')
    if ans.lower() == 'c':
        prepare_game()
    elif ans.lower() == 'm':
        menu_options()
    else:
        play_game(lines, bet)

def leave_game():
    print(f'\nThank you for playing! You left with ${balance}\n')

def pull_handle(item_set):
    board = []
    for column in range(COLS):
        line = []
        for rows in range(ROWS):
            line.append(random.choice(item_set))
        board.append(line)
    return board

def draw_board(board):
    print()
    for row in range(len(board[0])):
        for ix, column in enumerate(board):
            if ix != len(board)-1:
                print(column[row],end=' | ')
            else:
               print(column[row])
    print()

def score_board(board, lines):
    dict = {}
    wins = []
    score = 0
    for line in range(len(board)):
        if all(x == board[line][0] for x in board[line]):
            wins.append(line+1)
            score += MAX_LINES - 2

        for ix, char in enumerate(board[line]):
            if (ix,char) in dict:
                dict[(ix,char)] += 1
            else:
                dict[(ix, char)] = 1
        
    for key, val in dict.items():
        if val == len(board):
            wins.append(key[0]+len(board)+1)
            if key[1] == 'X' and key[0] == COLS//2 and wins[-1] <= lines:
                print("***Jackpot!!!***")
                score += MAX_LINES * 25
            else:
                score += MAX_LINES

    board = np.array(board)

    diags = [
        board[::-1,:].diagonal(i) for i in range(-board.shape[0]+1,board.shape[1]) 
            if len(board[::-1,:].diagonal(i)) == COLS
        ]
    diags.extend(
        board.diagonal(i) for i in range(board.shape[1]-1,-board.shape[0],-1) 
            if len(board.diagonal(i)) == COLS
        )

    for ix, line in enumerate(diags):
        if all(x == line[0] for x in line):
            if ix == 1:
                 wins.append(MAX_LINES)
            else:
                 wins.append(MAX_LINES-1)
            score += MAX_LINES + 4

    for line in list(wins):
        if line > lines:
            wins.remove(line)
            if ROWS < line > ROWS + COLS:
                score -= MAX_LINES + 4
            elif line > ROWS + COLS:
                score -= MAX_LINES
            else:
                score -= MAX_LINES - 2

    if not wins:
        return 0, 'LOSE', []
    else:
        return score, 'WIN', wins
        
def main():
    
    input('\nWelcome to the Slot Machine!\n')
    menu_options()
    
if __name__ == "__main__":
    main()