import MCTS
import Game

def main():
    game = Game.Game()
    ai = MCTS.MonteCarlo(game)
    ai.random_game()
    print "------------------------------------"
    print ai.plays[1].values()
    print ai.plays[2].values()
    print ai.wins[1].values()
    print ai.wins[2].values()


if __name__ == "__main__":
    main()
