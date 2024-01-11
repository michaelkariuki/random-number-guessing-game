# ideas:
    #Class that generates a random number(1, 10/ 1, 100)

# functions:
    # Generates random number ✔
    # finds factors of the number ✔
    # Calculates distance to number ✔
    # Displays if user input is close to number ✔
    # Gives hints:
        # You are warm!!(Range for warmness) ✔
        # Colder...(Range past which it gets cold) ✔
        # Factor of 2 ✔
        # factor of 3 ✔
        # factor of 5 ✔
    # Lose points with every wrong guess (1 pt) ✔
        # maximum of 10 points ✔

import random
import sys

class MiniGame:
    def __init__(self, range_limit= 30):
        super().__init__()
        self.range_limit = range_limit
        self.random_num = random.randint(1, self.range_limit+1)
        self.points = 10
        self.guess_range_threshold = 10
        self.guess_list = []

    #*************************************************************************************
    #prints intro to game message 
    def game_msg(self):
        print('*!RANDOM NUMBER GUESSING GAME!*\n')


    def print_game_status(self):
        print(f'Range: 1 - {self.range_limit} || Points : {self.points}\n')

    #*************************************************************************************

    #Takes user input
    def guess_action(self):
        guess = input("Please input a number : ")

        try:
            guess = int(guess)
        except:
            print(f'An error occurred : {sys.exc_info()[0]} ')
            print("Try again...")
            self.guess_action()

        self.guess_list.append(guess)
        return guess

    #*************************************************************************************
    def rem_point(self):
        self.points -= 1

    #*************************************************************************************
    def parse_guess(self, guess):

        assert isinstance(guess, int) , "input has to be an integer"

        if guess == self.random_num:
            return 1

        hint_list = ['', self.give_factor(guess)]

        print(self.guess_state(guess))
        print(random.choice(hint_list))

        return 0
    
    #*************************************************************************************
    #Find factors of the random number
    def find_factors(self):
        factor_list = []
        
        for x in range(2, self.random_num+1):
            if self.random_num%x == 0:
                factor_list.append(x) 
            else:
                continue

        # print(f'factor list  : {factor_list}')
        return factor_list

    #*************************************************************************************
    #Return distance from guess to actual number
    def get_guess_range(self, num):
        assert isinstance(num, int) , "input has to be an integer"

        return self.random_num - num

    #*************************************************************************************
    #Return  (warm) ,  (Cold) on the guessed number
    def guess_state(self, num):
        assert isinstance(num, int) , "input has to be an integer"

        guess_range = self.get_guess_range(num)

        if guess_range < 0:
            guess_range  = -guess_range

        if guess_range <= self.guess_range_threshold:
            return "Hint : You are warm!"
        else:
            return "Hint : You are cold!"

    #*************************************************************************************
    #Return  a random factor from factor list
    def give_factor(self, num):
        assert isinstance(num, int) , "input has to be an integer"

        factor_list = self.find_factors()

        weights_list = []
        for x in range(0, len(factor_list)):
            if x < 3:
                weights_list.append(random.randint(2, 5))
            else:
                weights_list.append(1)

        random_factor = random.choices(factor_list, weights= weights_list , k= 1)
        return f'Hint : Number is a factor of {random_factor[0]}'

    #*************************************************************************************
    #Exits game
    def finish_game(self):
        print("Game has closed.")
        sys.exit()

    #*************************************************************************************
    #Sets points depending on game state
    def parse_game_state(self, state):
        assert isinstance(state, int) , "input has to be an integer"

        if state == 1:
            print(f"You Won!!! Number to guess : {self.random_num} Guesses : {self.guess_list}")
            self.finish_game()

        self.rem_point()
        if self.points < 1:
            print(f"You lost!!! Number to guess : {self.random_num} Guesses : {self.guess_list}")
            self.finish_game()