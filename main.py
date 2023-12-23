ROWS = 3
COLS = 3

from setup import get_deposit, get_lines, place_bet

def main():

    balance = get_deposit()
    lines = get_lines()
    bet = place_bet()

    print(balance, lines, bet)

main()