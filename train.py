import MCTS
import Game
import cPickle as cp

def main():
    game = Game.Game()
    ai = MCTS.MonteCarlo(game)
    for i in range(5000):
        ai.random_game()
        print i
        if i % 100 == 0:
            with open("plays.pkl", "w") as f:
                f.write(cp.dumps(ai.plays))
            with open("wins.pkl", "w") as f:
                f.write(cp.dumps(ai.wins))

    
    with open("plays.pkl", "w") as f:
        f.write(cp.dumps(ai.plays))
    with open("wins.pkl", "w") as f:
        f.write(cp.dumps(ai.wins))


if __name__ == "__main__":
    main()
