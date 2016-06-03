import Game
import MCTS
import cPickle as cp

if __name__ == "__main__":
    game_stats = {1:0, 2:0}
    magic = True
    for i in range(10):
        print i
        game = Game.Game();
        with open("plays") as f:
            plays = cp.loads(f.read())
        
        with open("wins") as f:
            wins = cp.loads(f.read())
        
        ai = MCTS.MonteCarlo(game, plays=plays, wins=wins)
        while 1:
            play = ai.get_play()
            print play
            win = game.execute_turn(play)
            if win == 2:
                game_stats[game.current_player_num] += 1
                break
            play = game.get_random_move()
            if magic:
                play = "H8f"
                magic = False
            win = game.execute_turn(play)
            ai.update(game.next_state(ai.states[-1], play))
            if win == 2:
                game_stats[game.current_player_num] += 1
                break

    

