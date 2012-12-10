# Collection of AI's each one should implement:
# init(self, name)
# playCard(self)
# updateInfo(self)
# orderUp(self, center_card)
# pickUp(self, deck)
# pickSuit(self, out_suit)
# reset(self)
# setHand(self, new-hand)

from my_globals import *

import random
random.seed() # automatically uses system time

class Player():
	def __init__(self, name):
		self.name = name # name is a unique identifier
		self.tricks = 0
		self.hand = []
		
	def printHand(self):
		for x in range(len(self.hand)):
			print x, ":", self.hand[x],
		print
		
	def validMoves(self, trick, trump):
		"""
		Changing the lead suit to trump may cause issues to arise
		"""
		# assume that the lead, left bower problem is taken care of
		validmoves = []
		for x in hand:
			if x.num == 11:
				if lead == trump and x.suit == offSuit(trump):
					validmove.append(x)
			elif x.suit == lead:
				validmoves.append(x)
		return tuple(validmoves)
		
	def setHand(self, hand):
		assert len(hand) == 5, "from setHand %s, hand needs to be 5" % self.name
		self.hand = hand

class RandomPlay(Player):
	def __init__(self, name):
		super(Player, self).__init__(name)

	def playCard(self):
		moves = validMoves(self.hand, trick)
		chosen = random.choice(moves)
		self.hand.remove(chosen)
		return chosen
		
	def updateInfo(self):
		# not necessary for random play
		pass

	def orderUp(self, center_card):
		return random.choice([True, False])

	def pickSuit(self, out_suit):
		if random.choice([True, False]):
			return random.choice([x for x in [heart, spade, club, diamond] if x != out_suit])
		else:
			return None
		
	def reset(self):
		# not necessary for random play
		pass

class SimpleStat():
	def __init__(self, name):
		super(Player, self).__init__(name)
		self.tfc = set(allcards) # tfc stands for total free cards
		self.partner = set(allcards)
		self.opp1 = set(allcards)
		self.opp2 = set(allcards)
		
	def setHand(self, hand):
		super(Player, self).setHand(hand)
		self.tfc -= set(self.hand)
	
	def playCard(self):
		pass

	def updateInfo(self):
		assert len(finished_trick.center) == 4, "there should be four cards in the center"
		self.tfc -= set(finished_trick.center.keys())
		
		for c, p in finished_trick.center.items():
			if player == finished_trick.leader:
				lead_suit = c.suit
		
		lead_set = set([x for x in allcards if x.suit == heart])
		pass

	def orderUp(self, center_card):
		pass

	def pickSuit(self, out_suit):
		pass

	def reset(self):
		"""Reset the information gathered by the ai without reinstatiating it.
		
			For use between rounds. Useful for those that need to keep their statistics.
		"""
		pass

class SimpleRules():
	# this ai will use arbitrary rules created by us to play the game
	# defaulting to random play when unsure
	def __init__(self, name):
		super(Player, self).__init__(name)
		
	def playCard(self):
		pass

	def updateInfo(self):
		pass

	def orderUp(self, center_card):
		pass

	def pickSuit(self, out_suit):
		pass

	def reset(self):
		"""Reset the information gathered by the ai without reinstatiating it.
		
			For use between rounds.
		"""
		pass
		
class RealPlayer():
	def __init__(self, name):
		super(Player, self).__init__(name)
	
	def playCard(self):
		self.printHand()
		move = input("Please enter the # of the card you wish to play: ")
		while(True):
			if move is int and 0 <= move < len(hand) and hand[move] in validMoves(self.hand, cur_trick):
				return move
			else:
				move = input("Please enter a valid move: ")
				
	def updateInfo(self):
		# not necessary for a real player
		pass

	def orderUp(self, center_card):
		if self == dealer:
			self.dealerPickUp(self, center_card) # is this what I want
			
		self.printHand()
		while(True):
			choice = raw_input("Do you want to order the dealer up? ")
			choice = choice.lower()
			if choice == "y" or choice == "yes":
				return True
			elif choice == "n" or choice == "no":
				return False
			else:
				print("Please enter yes or no.")

	def pickSuit(self, out_suit):
		pass
		
	def reset(self):
		# not necessary for a real player
		pass