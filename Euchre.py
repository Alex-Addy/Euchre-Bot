import random
from my_classes import *
from my_globals import *
import AIs

def main():

	random.seed() # uses the system time by default
	
	# create team objects to hold information about the teams
	team1_score = 0
	team2_score = 0
	
	cur_trick = Trick()
	
	deck = list(allcards[:]) # shallow copy of allcards that gives you a regular list
	
	players = (AIs.RandomPlay("R1"), AIs.RandomPlay("R2"), AIs.RandomPlay("R3"), AIs.RandomPlay("R4"))
	team1 = [0, 1]
	team2 = [2, 3]
	dealer = 0 # any reference to a player will be an index to the tuple players
	
	while(team1_score < 10 and team2_score < 10):
		cur_round = Round(
		
	if team1_score == 10:
		print("Team 1 wins!") # placeholder
	elif team2_score == 10:
		print("Team 2 wins!") # placeholder
	else:
		pass
		
if __name__ == "__main__":
	pass
	