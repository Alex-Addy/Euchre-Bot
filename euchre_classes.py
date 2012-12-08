from euchre_globals import *

class Round(object):
	def __init__(self, all_cards, players, team1, team2, dealer, allcards):
		self.deck = list(allcards[:]) # get a deep copy of all_cards for dealing
		self.trump = None
		self.dealCards(players, dealer)
		
	def setUp(self, players, dealer):
		self.dealCards(self, players, dealer)
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

	def dealCards(self, players, dealer):
		random.shuffle(self.deck) # mutates deck

		for x in range(1, len(players)+1):
			players[(x+dealer)%4].setHand(self.deck[:5])
			self.deck = self.deck[5:]
		
	def orderUpDealerSec(self, players, dealer):
		for x in range(1, len(players)+1):
			cur_player = self.players[(self.dealer+x)%len(players)]
			if cur_player.orderUp(self.deck[0], dealer):
				placed = self.players[dealer].pickUp(self.deck[0])
				self.deck[0] = placed
				return (self.dealer+x)%len(players)
			else:
				pass # display that the player passed
		return None
		
	def pickSuitSec(self, players, out_suit):
		for x in range(1, len(players)+1):
			cur_player = self.players[(self.dealer+x)%len(players)]
			picked = cur_player.pickSuit(out_suit):
			if picked:
				return (self.dealer+x)%len(players), picked
			else:
				pass # display that the player passed
		return None
	
class Trick():
	def __init__(self, center = {}, leader = None):
		self.center = center # dict to hold information about the cards in play for the current trick of the form {card:player}
		self.leader = leader # the player who will play the first card

	def play(self, players, trump):
		for x in range(len(players)):
			cur_player = self.players[(self.leader+x)%len(players)]
			played = cur_player.playCard(self, trump)
			self.center[played] = (self.leader+x)%len(players)		
	
	def __repr__(self):
		return "Trick(%r)" % (self.__dict)