#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.my_move = self.moves
        self.their_move = random.choice(self.moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class TheRock(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)
# 'random'


class HumanPlayer(Player):
    def move(self):
        while True:
            MakeAMove = input('Rock, Paper, Scissors? > ')
            if MakeAMove.lower() in self.moves:
                return MakeAMove.lower()
            print("Sorry that is an invalid option, please try again!")


class ReflectPlayer(Player):
    def move(self):
        return self.their_move
# 'looks at last move played by user'


class CyclePlayer(Player):
    def move(self):
        if self.my_move == self.moves[0]:
            return self.moves[1]
        elif self.my_move == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]
# 'looks at last move played and cycles to next'


class Game:
    print("Rock, Paper Scissors, Go!")
# 'what beats what'

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0
# 'define players and score'

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if self.beats(move1, move2):
            self.score_p1 += 1
            winner = f"player one wins with {move1}!"
        elif move1 == move2:
            self.score_p1 = self.score_p1
            self.score_p2 = self.score_p2
            winner = "Its a tie!"
        else:
            self.score_p2 += 1
            winner = f"Player two wins with {move2}!"
        print(
            f"Player one chose {move1}\n"
            f"Player two chose {move2}\n"
            f"{winner}\n"
            f"The score is now:\n"
            f"Player one -- {self.score_p1}\n"
            f"Player two -- {self.score_p2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
# 'who beat who with what move'

    def play_game(self):
        for round in range(3):
            print(f"Round {round} --")
            self.play_round()
        if self.score_p1 > self.score_p2:
            print(
                "Player one has won the game with the score of:\n"
                f"Player one -- {self.score_p1}\n"
                f"Player two -- {self.score_p2}\n"
                "Great job! ヽ(^o^)")
        elif self.score_p1 < self.score_p2:
            print(
                "Player two has won the game with the score of:\n"
                f"Player one -- {self.score_p1}\n"
                f"Player two -- {self.score_p2}\n"
                "Better luck next time! (>_<)")
        else:
            print(
                "The game has ended in a tie with the score being:\n"
                f"Player one -- {self.score_p1}\n"
                f"Player two -- {self.score_p2}\n"
                "Can't win them all ¯\_(ツ)_/¯")

# 'who wins the game and why'


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(
        [TheRock(), RandomPlayer(), ReflectPlayer(), CyclePlayer()]))
    game.play_game()

