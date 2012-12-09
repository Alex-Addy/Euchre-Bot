from my_globals import *

# holder and runner of the entire game
class Euchre():
	def __init__(self):
		self.playerA1 = None # will initialize AI's here
		self.playerA2 = None
		self.playerB1 = None
		self.playerB2 = None
		self.players = [self.playerA1, self.playerB1, self.playerA2, self.playerB2]
		self.deck = list(allcards[:]) # get a deep copy of all_cards for dealing

	def start(self): # begins the first round
		# determine first dealer

		# moved the multiple playRound calls into here
		# iterative instead of recursive
		while not self.hasWinner():
			self.playRound()
		self.endGame()

	def dealCards(self):
		random.shuffle(self.deck) # mutates deck

		for x in range(1, len(players)+1):
			deal_index = self.players.index(game.dealer)
			self.players[(x+deal_index)%4].setHand(self.deck[:5])
			self.deck = self.deck[5:]

	def rotateDeal(self): # rotate the dealer
		# use this if game.dealer is a direct reference
		game.dealer = self.players[(self.players.index(game.dealer)+1)%4]

	def playRound(self): # begins the next 5 tricks
		self.rotateDeal()
		self.dealCards()

		# order up

		# play 5 tricks
		pass

	def playTrick(self):
		pass

	def hasWinner(self):
		if game.teamA >= 10:
			print "Team A Has won!"
			return True
		elif game.teamB >= 10:
			print "Team B Has won!"
			return True
		else:
			return False

	def endGame(self): # ends the game
		pass
		
	def getWinningCard(self):
		temp = [(x, self.curCardVal(x)) for x in game.center]
		best = temp[0][1]
		bext_x = 0
	
		for x in range(1, len(temp)):
			if temp[x][1] > best:
				best = temp[x][1]
				best_x = x
		
		return temp[x][0]
		
	def curCardVal(self, card):
		"""This might need to become a global function"""
		if card.suit == game.trump:
			if card.num == 11: # card is right bower
				return card.num + 15
			else:
				return card.num + 10

		elif card.num == 11 and card.suit == offSuit(game.trump):
			# card is left bower
			return card.num + 14
		elif card.suit == game.lead.suit:
			return card.num
		else:
			return 0

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
			picked = cur_player.pickSuit(out_suit)
			if picked:
				return (self.dealer+x)%len(players), picked
			else:
				pass # display that the player passed
		return None

