from entity.Player import Player
from entity.Dice import Dice
from service.ArenaService import ArenaService

class MagicalArenaApp:
    def main():

        # Print a welcome message
        print("Hello World! Welcome to Magical Arena!")
        player1 = Player(100,50,30)
        player2 = Player(100,50,20)
        arena = ArenaService(player1, player2)
        arena.play_match()



if __name__ == "__main__":
    MagicalArenaApp.main()
