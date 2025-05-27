import random


class BingoGame:
    player_list = []

    def __init__(self):
        self.name = input("Enter your name: ")
        self.__rand_num = random.randint(0, 10)
        self.__guess_left = 3
        self.__win_state = False
        self.player_list.append(self)

    def check_answer(self):
        answer = int(input(f"{self.name}, enter your guess (0-10): "))
        if answer > self.__rand_num:
            print("Choose lower number")
        elif answer < self.__rand_num:
            print("Choose higher number")
        else:
            print("Bingo!")
            self.__win_state = True
        self.__minus_guess_left()

    def __minus_guess_left(self):
        self.__guess_left -= 1

    def has_guess_left(self):
        return self.__guess_left > 0

    def has_won(self):
        return self.__win_state

    @classmethod
    def game_has_winner(cls):
        return any(player.has_won() for player in cls.player_list)


class GameController:
    def __init__(self):
        while True:
            for player in BingoGame.player_list:
                if not player.has_won() and player.has_guess_left():
                    player.check_answer()
            if BingoGame.game_has_winner():
                print("Game Over! We have a winner!")
                break
            if all(not p.has_guess_left() for p in BingoGame.player_list):
                print("Game Over! No one won.")
                break


if __name__ == "__main__":
    while True:
        order = input("What do you want to do? (add/start/exit): ").strip().lower()
        if order == "add":
            BingoGame()
        elif order == "start":
            GameController()
        elif order == "exit":
            break
