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
	"""
	for x in player_hand:
		if x.suit == trick.lead:
			return tuple(filter(lambda c: c.suit == trick.lead, player_hand)
	return tuple(player_hand)
	
class Card(object):
	def __init__(self, suit, num):
		self.suit = suit
		self.num = num
		
	def __str__(self):
		return str(self.suit) + str(self.num)

	def __repr__(self):
		return self.__str__()
		
if __name__ == "__main__":
	pass
	