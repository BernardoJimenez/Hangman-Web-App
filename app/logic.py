import random

class GameLogic():
    # create new instance of GameLogic() for each new game played by user

    def __init__(self):
        self.my_dict = open("app/static/EnglishDictionary.txt")
        self.random_word = random.choice(self.my_dict.readlines()).strip()

        while len(self.random_word) < 3:
            self.random_word = random.choice(self.my_dict.readlines()).strip()

        self.my_dict.close() # CLOSE FILE
        # pick a random word WITH LENGTH GREATER THAN 2 from the dictionary. Remove any whitespace.
        self.length_notice = "The word you're guessing is {} letters long".format(len(self.random_word))

        self.current_progress = ""
        # create the starting state
        for letter in self.random_word:
            self.current_progress += "_"

        self.game_over = False
        self.current_index = 0
        self.changes = 0
        self.bad_guesses = 0
        self.all_guesses = []


    def process_guess(self, user_guess):
        if (user_guess[0].isalpha() == False or str(user_guess).lower()[0] in self.all_guesses):
            pass
        else:
            guess = str(user_guess).lower()[0]
            # clean the input: Make sure it's a lowercase string and take only the first character

            for letter in range(0, len(self.random_word)):
                # compare guess against each letter in random word chosen
                if (self.random_word[letter] == guess):
                    self.changes += 1
                    # replace where it matches in the respective index of current_progress
                    self.current_progress = self.current_progress[:self.current_index] + guess + self.current_progress[(self.current_index+1):]
                self.current_index += 1

            if (self.changes == 0):
                # if there were no changes, it was a bad guess
                self.bad_guesses += 1

            self.changes = 0
            self.current_index = 0
            # set back to zero, and add latest guess to list of previous guesses
            self.all_guesses.append(guess)

            if (self.bad_guesses == 10 or '_' not in self.current_progress):
                # check if that was the 10th bad guess or the final correct one needed
                self.game_over = True

            # No return statement. Only edits self varaibles based on guess


    def game_over_message(self):
        # used once game is over, for GameOverForm
        if (self.bad_guesses == 10):
            return "Better luck next time! You lost... The word was \"{}\".".format(self.random_word)
        else:
            return "Congrats! You won... The word is \"{}\".".format(self.random_word)
