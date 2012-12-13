from my_globals import *
import AIs
import random

# holder and runner of the entire game
class Euchre():
	def __init__(self):
		# initialize AI's here
		self.playerA1 = AIs.SimpleStat("Alex")
		self.playerA2 = AIs.RandomPlay("Brian")
		self.playerB1 = AIs.RandomPlay("Katrina")
		self.playerB2 = AIs.RandomPlay("Sandy")

		# make a list of the players for rotations
		self.players = [self.playerA1, self.playerB1, self.playerA2, self.playerB2]
		
		self.playerA1.setRelations(self.playerA2, self.playerB1, self.playerB2)

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

		# prepare for round
		game.caller = self.orderUpDealerSec()
		if game.caller:
			# TODO
			# have dealer pick up and discard
			game.trump = self.deck[0].suit
			self.deck[0] = game.dealer.pickUp(self.deck[0])
		else:
			game.caller, game.trump = self.pickSuitSec(self.deck[0].suit)
			# TODO
			# stick the dealer
			pass
		
		# play 5 tricks
		winner = self.players[(self.players.index(game.dealer) + 1)%4]
		for x in range(5):
			winner = self.playTrick(winner)
			keys = game.center.keys()
			txt = "End of trick:\n\t%s, %s, %s, %s\n\tWinner:%s\n" % (keys[0], keys[1], keys[2], keys[3],winner.name)
			out.log(txt)
			for p in self.players:
				p.updateInfo(winner)
				
		self.allotScore()
		out.log("End of round:\n\tTrump: %s\n\tCaller: %s\n\tScores A: %d B: %d\n" % \
			(game.trump, game.caller.name, game.scoreA, game.scoreB))
		

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
		win_card = self.getWinningCard()
		win_player = game.center[win_card]
		if win_player == self.playerA1 or win_player == self.playerA2:
			game.tricksA += 1
		else:
			game.tricksB += 1
		return win_player
		
	def allotScore(self):
		# simple rules used, no going alone
		if game.caller == self.playerA1 or game.caller == self.playerA2: # caller is in team A
			c_team = "A"
			c_tricks = game.tricksA
		else:
			c_tricks = game.tricksB
			c_team = "B"
			
		out.log("\t\tCaller: %s  Tricks: A; %d B; %d C: %d" % (c_team, game.tricksA, game.tricksB, c_tricks))
			
		if c_tricks == 0:
			if c_team != "A":
				game.scoreA += 4
			else:
				game.scoreB += 4
		elif c_tricks == 1 or c_tricks == 2:
			if c_team != "A":
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
		if game.scoreA >= 10:
			print "Players %s and %s have won!" % (self.playerA1.name, self.playerA2.name)
			out.log("Players %s and %s have won!" % (self.playerA1.name, self.playerA2.name))
		elif game.scoreB >= 10:
			print "Players %s and %s have won!" % (self.playerB1.name, self.playerB2.name)
			out.log("Players %s and %s have won!" % (self.playerB1.name, self.playerB2.name))
		print "With a score of %d to %d." % (game.scoreA, game.scoreB)
		out.log("With a score of %d to %d." % (game.scoreA, game.scoreB))
		
	def getWinningCard(self):
		return sorted(game.center, key=curCardVal, reverse=True)[0]
	
		# temp = [(x, self.curCardVal(x)) for x in game.center]
		# best = temp[0][1]
		# bext_x = 0
	
		# for x in range(1, len(temp)):
			# if temp[x][1] > best:
				# best = temp[x][1]
				# best_x = x
		
		# return temp[x][0]

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