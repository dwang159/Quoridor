# Plays 2 AIs against each other

from Game import *
from Randomizer import *
import random

def playGame():
	randomizerGame = Game()
	turn = 0

	move = randomizerGame.getRandomMove()

	# Let Randomizer begin game
	while randomizerGame.execute_turn(move) == 1:
		if turn == 0:
			# TO-DO: REPLACE WITH SMART AI FUNCTION WHATEVER IT MAY BE
			move = randomizerGame.getRandomMove()
		else:
			move = randommizerGame.getRandomMove()

		turn = (turn + 1) % 2

	if turn == 0:
		print "Randomizer wins"
	else:
		print "MCTS wins"