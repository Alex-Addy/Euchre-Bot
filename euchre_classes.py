

class Round(object):
	def __init__(self, all_cards, players, dealer):
		self.deck = all_cards[:] # get a deep copy of all_cards for dealing
		pass
		
	def dealCards(self, players, dealer):
		self.deck = random.shuffle(self.deck)
		pass
		
	def orderUpDealer(self, players, dealer):
		pass
		
	def pickSuitSec(self, players, out_suit):
		pass
	
class Trick(object):
	def __init__(self, center = {}, caller = None, lead = None):
		self.center = center # dict to hold information about the cards in play for the current trick of the form {card:player}
		self.caller = caller # the player who called the current suit, by ordering the dealer up or calling the suit afterwards
		self.lead = lead # the first card played
		self.trump = trump # the suit that is trump
	
	def __repr__(self):
		return "Trick(%r)" % (self.__dict)
	
class Card(object):
	def __init__(self, suit, num):
		self.suit = suit
		self.num = num
		
	def __str__(self):
		if self.num > 10:
			return list("Jack", "Queen", "King", "Ace")[self.num - 11] + "|" + self.suit
		else:
			return str(self.num) + "|" + self.suit

	def __repr__(self):
		return "Card(%r)" % (self.__dict)