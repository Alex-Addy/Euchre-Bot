import random
from euchre_classes import *
import AIs


if True: # black characters
	heart = u"\u2665"
	spade = u"\u2660"
	diamond = u"\u2666"
	club = u"\u2663"
else:
	heart = u"\u2661"
	spade = u"\u2664"
	diamond = u"\u2662"
	club = u"\u2667"

# a list of all possible cards, done as a tuple so that it cannot be accidently changed at runtime
allcards = tuple([Card(s, c) for s in (diamond, spade, club, heart) for c in (14, 13, 12, 11, 10, 9)])

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
	dealer = 0
	
	while(team1_score < 10 and team2_score < 10):
		cur_round = Round(
		
	if team1_score == 10:
		pass
	else:
		pass
	
def winningCard(trick, trump):
	temp = [(x, curCardVal(x, trick)) for x in trick.center]
	best = temp[0][1]
	bext_x = 0
	
	for x in range(1, len(temp)):
		if temp[x][1] > best:
			best = temp[x][1]
			best_x = x
	
	return temp[x][0]


def curCardVal(card, trick):
	if card.suit == trick.trump:
		if card.num == 11: # card is right bower
			return card.num + 15
		else:
			return card.num + 10
			
	elif card.num == 11 and card.suit == offSuit(trick.trump):
		# card is left bower
		return card.num + 14
	elif card.suit == trick.lead:
		return card.num
	else:
		return 0

def offSuit(trump_suit):
	"""
	Takes a suit and returns what the off hand suit would be.
	"""
	if trump_suit == heart:
		return diamond
	elif trump_suit == diamond:
		return heart
	elif trump_suit == spade:
		return club
	else:
		return spade
		
if __name__ == "__main__":
	pass
	