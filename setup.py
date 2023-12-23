MAX_LINES = 7

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
            return print('Input must be numeric')
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