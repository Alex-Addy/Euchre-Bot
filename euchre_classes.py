class Player(object):
	def __init__(self, name, partner, opponents, ai = None):
		# stats for a player, can have more and make them persistent
		self.name = name
		self.tricks = 0
		self.hand = []
		self.partner = partner
		self.opponents = opponents
		self.ai = ai
	
	def getMove(self, Round):
		# get a move from the player, whether that is an ai or real player
		if ai:
			ai.move(self.hand, Round)
		else:
			self.printHand()
			move = input("Please enter the # of the card you wish to play: ")
			while(True):
				if move is int and 0 <= move < len(hand) and hand[move] in validMoves(self.hand, cur_trick):
					return move
				else:
					move = input("Please enter a valid move: ")
	
	def printHand(self):
		for x in range(len(hand)):
			print(x, ": ", hand[x], end=" ")
		print()
		
	def orderUp(self, center_card, dealer):
		pass
		
	def pickSuit(self, out_suit):
		pass
	
class Round(object):
	def __init__(self, all_cards, players, dealer):
		self.deck = all_cards[:] # get a deep copy of all_cards for dealing
		
		
	def dealCards(self, deck, players, dealer):
		pass
		
	def orderUpDealer(self, players, dealer):
		pass
		
	def pickSuitSec(self, players, out_suit):
		pass
		
	def
	
class Trick(object):
	def __init__(self, center = {}, caller = None, lead = None):
		self.center = center # dict to hold information about the cards in play for the current trick of the form {card:player}
		self.caller = caller # the player who called the current suit, by ordering the dealer up or calling the suit afterwards
		self.lead = lead # the first card played
	
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