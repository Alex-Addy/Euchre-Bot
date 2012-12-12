from my_globals import *
import AIs
import random

# holder and runner of the entire game
class Euchre():
	def __init__(self):
		# initialize AI's here
		self.playerA1 = AIs.RandomPlay("Susan")
		self.playerA2 = AIs.RandomPlay("Mary")
		self.playerB1 = AIs.RandomPlay("Katrina")
		self.playerB2 = AIs.RandomPlay("Sandy")

		# make a list of the players for rotations
		self.players = [self.playerA1, self.playerB1, self.playerA2, self.playerB2]

		self.deck = list(allcards[:]) # get a deep copy of all_cards for dealing

	def playGame(self): # begins the first round
		# determine first dealer
		# start at last player so that the first rotate in playRound has the first player deal
		game.dealer = self.playerB2

		# moved the multiple playRound calls into here
		# iterative instead of recursive
		while not self.hasWinner():
			self.playRound()
		self.endGame()

	def dealCards(self):
		random.shuffle(self.deck) # mutates deck
		deal_index = self.players.index(game.dealer)

		for x in range(1, 5):
			self.players[(x+deal_index)%4].setHand(self.deck[:5])
			self.deck = self.deck[5:]

	def rotateDeal(self): # rotate the dealer
		# use this if game.dealer is a direct reference
		game.dealer = self.players[(self.players.index(game.dealer)+1)%4]

	def playRound(self): # begins the next 5 tricks
		game.resetRound()
		self.rotateDeal()
		self.deck = list(allcards[:])
		self.dealCards()
#		print self.playerA1.name
#		print self.playerA1.hand
#		print self.playerA2.name
#		print self.playerA2.hand
#		print self.playerB1.name
#		print self.playerB1.hand
#		print self.playerB2.name
#		print self.playerB2.hand

		# prepare for round
		game.caller = self.orderUpDealerSec()
		if game.caller:
			# TODO
			# have dealer pick up and discard
			game.dealer.pickUp(self.deck[0])
		else:
			game.caller, game.trump = self.pickSuitSec(self.deck[0].suit)
			# TODO
			# stick the dealer
			pass
			
#		print self.playerA1.name
#		print self.playerA1.hand
#		print self.playerA2.name
#		print self.playerA2.hand
#		print self.playerB1.name
#		print self.playerB1.hand
#		print self.playerB2.name
#		print self.playerB2.hand
		
		# play 5 tricks
		winner = self.players[(self.players.index(game.dealer) + 1)%4]
		for x in range(5):
			winner = self.playTrick(winner)
		
		self.allotScore()

	def playTrick(self, leader):
		game.resetTrick()
		
		# get the start card from leader
		# assume cards played are legal
		played = leader.playCard()
		game.center[played] = leader
		
		# handle the lead/left bower problem
		if played.num == 11 and played.suit == offSuit(game.trump):
			game.lead = offSuit(game.trump)
		else:
			game.lead = played.suit
		
		# play the trick
		leader_index = self.players.index(leader)
		for x in range(1, 4):
			played = self.players[(leader_index+x)%4].playCard()
			game.center[played] = self.players[(leader_index+x)%4]
		
		# return the winner of the trick
		return game.center[self.getWinningCard()]
		
	def allotScore(self):
		# simple rules used, no going alone
		if self.players.index(game.caller) in (0, 2): # caller is in team A
			c_team = "A"
			c_tricks = game.tricksA
		else:
			c_tricks = game.tricksB
			c_team = "B"
			
		if c_tricks == 0:
			if c_team == "A":
				game.scoreA += 4
			else:
				game.scoreB += 4
		elif c_tricks == 1 or c_tricks == 2:
			if c_team == "A":
				game.scoreA += 2
			else:
				game.scoreB += 2
		elif c_tricks == 3 or c_tricks == 4:
			if c_team == "A":
				game.scoreA += 1
			else:
				game.scoreB += 1
		else:
			if c_team == "A":
				game.scoreA += 2
			else:
				game.scoreB += 2

	def hasWinner(self):
		if game.scoreA >= 10:
			print "Team A Has won!"
			return True
		elif game.scoreB >= 10:
			print "Team B Has won!"
			return True
		else:
			return False

	def endGame(self): # ends the game
		pass
		
	def getWinningCard(self):
		# TEST THIS
		#return sorted(game.center, key=self.curCardVal, reverse=True)[0]
	
		temp = [(x, self.curCardVal(x)) for x in game.center]
		best = temp[0][1]
		bext_x = 0
	
		for x in range(1, len(temp)):
			if temp[x][1] > best:
				best = temp[x][1]
				best_x = x
		
		return temp[x][0]
		
	def curCardVal(self, card):
		# This might need to become a global function
		if card.suit == game.trump:
			if card.num == 11: # card is right bower
				return card.num + 15
			else:
				return card.num + 10

		elif card.num == 11 and card.suit == offSuit(game.trump):
			# card is left bower
			return card.num + 14
		elif card.suit == game.lead:
			return card.num
		else:
			return 0

	def orderUpDealerSec(self):
		deal_index = self.players.index(game.dealer)
		for x in range(1, 5):
			cur_player = self.players[(deal_index+x)%4]
			if cur_player.orderUp(self.deck[0]):
				placed = game.dealer.pickUp(self.deck[0])
				self.deck[0] = placed
				return cur_player
			else:
				pass # display that the player passed
		return None
		
	def pickSuitSec(self, out_suit):
		for x in range(1, 5):
			cur_player = self.players[(self.players.index(game.dealer)+x)%4]
			picked = cur_player.pickSuit(out_suit)
			if picked:
				return self.players[(self.players.index(game.dealer)+x)%4], picked
			else:
				pass # display that the player passed
		return None