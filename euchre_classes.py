class Round(object):
	def __init__(self, all_cards, players, team1, team2, dealer):
		self.deck = None # get a deep copy of all_cards for dealing
		self.trump = None
		self.dealCards(players, dealer, allcards)
		
	def setUp(self, players, dealer, allcards):
		self.dealCards(self, players, dealer, allcards)
		who_ordered = self.orderUpDealer(players, dealer)
		if who_ordered:
			# pass message to each player about who ordered who to pick up
			# then have dealer pick up and discard
			return
		else:
			who, what = self.pickSuitSec(players, dealer)
			# stick the dealer
			# communicate who picked and what was picked to each player
			return

	def dealCards(self, players, dealer, allcards):
		self.deck = allcards[:]
		random.shuffle(self.deck) # mutates deck

		for x in range(1, 5):
			players[(x+dealer)%4].setHand(self.deck[:5])
			self.deck = self.deck[5:]
		
	def orderUpDealerSec(self, players, dealer):
		pass
		
	def pickSuitSec(self, players, out_suit):
		pass
	
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