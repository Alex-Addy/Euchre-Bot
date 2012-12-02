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
		
class Trick(object):
	def __init__(self, center = {}, caller = None, lead = None, trump = None):
		self.center = center # dict to hold information about the cards in play for the current trick of the form {card:player}
		self.caller = caller # the player who called the current suit, by ordering the dealer up or calling the suit afterwards
		self.lead = lead # the first card played
		self.trump = trump
	
	def __repr__(self):
		return "Trick(%r)" % (self.__dict)