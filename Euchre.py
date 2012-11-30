import random

heart = "h"
spade = "s"
diamond = "d"
club = "c"

def main():

	random.seed() # uses the system time by default

	# a list of all possible cards, done as a tuple so that it cannot be accidently changed at runtime
	allcards = tuple([Card(s, c) for s in (diamond, spade, club, heart) for c in (14, 13, 12, 11, 10, 9)])
	
	# create team objects to hold information about the teams
	team1.score = 0
	team2.score = 0
	team1.tricks = 0
	team2.tricks = 0
	
	trick.center = {} # dict to hold information about the cards in play for the current trick of the form {card:player}
	trick.caller = None # the player who called the current suit, by ordering the dealer up or calling the suit afterwards
	trick.lead = None # the first card played
	trick.trump = None
	
	deck = list(allcards[:]) # shallow copy of allcards that gives you a regular list
	
	pass

def validMove(player_hand, trick):
	"""
	Returns a tuple of cards that the player can play.
	
	Given a list of the players hand, and the trick information.
	""" # not complete yet
	for x in player_hand:
		if x.suit == trick.lead:
			return tuple(filter(lambda c: c.suit == trick.lead, player_hand)
	return tuple(player_hand)
	
def trickWinner(trick):
	pass

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
	
class Card(object):
	def __init__(self, suit, num):
		self.suit = suit
		self.num = num
		
	def __str__(self):
		return str(self.suit) + str(self.num)

	def __repr__(self):
		return self.__str__()
		
class Trick(object):
	def __init__(self, center = {}, caller = None, lead = None, trump = None):
		self.center = center
		self.caller = caller
		self.lead = lead
		self.trump = trump
	
	def __repr__(self):
		return "Trick(%r)" % (self.__dict)
		
if __name__ == "__main__":
	pass
	