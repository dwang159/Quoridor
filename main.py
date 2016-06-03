import MCTS
import Game
import cPickle as cp

def main():
    game = Game.Game()
    ai = MCTS.MonteCarlo(game)
    for i in range(1000):
        ai.random_game()
        print i
    
    with open("plays.pkl", "w") as f:
        f.write(cp.dumps(ai.plays))
    with open("wins.pkl", "w") as f:
        f.write(cp.dumps(ai.wins))
    print "------------------------------------"
    print ai.plays[1].values()
    print ai.plays[2].values()
    print ai.wins[1].values()
    print ai.wins[2].values()


if __name__ == "__main__":
    main()
