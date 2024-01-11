from Guessing import MiniGame

def main():
    game = MiniGame(range_limit= 100)
    game.game_msg()

    while True:
        game.print_game_status()
        guess = game.guess_action()
        state = game.parse_guess(guess)
        game.parse_game_state(state)



if __name__ == "__main__":
    main()