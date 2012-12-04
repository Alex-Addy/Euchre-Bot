import random
from euchre_classes import *

heart = "h"
spade = "s"
diamond = "d"
club = "c"

# a list of all possible cards, done as a tuple so that it cannot be accidently changed at runtime
allcards = tuple([Card(s, c) for s in (diamond, spade, club, heart) for c in (14, 13, 12, 11, 10, 9)])

def main():

	random.seed() # uses the system time by default
	
	# create team objects to hold information about the teams
	team1.score = 0
	team2.score = 0
	team1.tricks = 0
	team2.tricks = 0
	
	cur_trick = Trick()
	
	deck = list(allcards[:]) # shallow copy of allcards that gives you a regular list
	
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

def validMoves(hand, trick):
    """
    Changing the lead suit to trump may cause issues to arise
    """
    # assume that the lead, left bower problem is taken care of
	validmoves = []
	for x in hand:
		if x.num == 11:
			if lead == trump and x.suit == offSuit(trump):
				validmove.append(x)
		elif x.suit == lead:
			validmoves.append(x)
	return tuple(validmoves)

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
	