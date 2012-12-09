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