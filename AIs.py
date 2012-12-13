# Collection of functions each AI should implement:
# __init__(self, name)
# playCard(self)
# updateInfo(self)
# orderUp(self, center_card)
# pickUp(self, card)
# pickSuit(self, out_suit)
# reset(self)
# setHand(self, new-hand)

from my_globals import *

import random
random.seed() # automatically uses system time

class Player(object):
	def __init__(self, name):
		self.BaseSetUp(name)
		
	def printHand(self):
		for x in range(len(self.hand)):
			print "[%d: %s], " % (x, self.hand[x]),
		print
		
	def BaseSetUp(self, name):
		self.name = name # name is a unique identifier
		self.tricks = 0
		self.hand = []
		
	def validMoves(self):
		# assume that the lead, left bower problem is taken care of
		validmoves = [] 
		for x in self.hand:
			if x.num == 11:
				if game.lead == game.trump and x.suit == offSuit(game.trump):
					validmoves.append(x)
			elif x.suit == game.lead:
				validmoves.append(x)
	
		if not validmoves:
			validmoves = self.hand
			
		return tuple(validmoves)
		
	def setHand(self, hand):
		assert len(hand) == 5, "from setHand of %s, hand needs to be 5" % self.name
		self.hand = hand

class RandomPlay(Player):
	def __init__(self, name):
		self.BaseSetUp(name)
		
	def playCard(self):
		moves = self.validMoves()
		chosen = random.choice(moves)
		self.hand.remove(chosen)
		return chosen
		
	def updateInfo(self, winner):
		# not necessary for random play
		pass

	def orderUp(self, center_card):
		return random.choice([True, False])

	def pickSuit(self, out_suit):
		if random.choice([True, False]) or game.dealer == self:
			return random.choice([x for x in [heart, spade, club, diamond] if x != out_suit])
		else:
			return None

	def pickUp(self, top):
		assert type(top) == Card, "pickUp was given a %s, it wants a Card" % type(top)
		discard = random.choice(self.hand)
		self.hand.remove(discard)
		self.hand.append(top)
		return discard
		
	def reset(self):
		# not necessary for random play
		pass

class SimpleStat(Player):
	def __init__(self, name):
		self.BaseSetUp(name)
		
		self.tfc = set(allcards) # tfc stands for total free cards
		self.pm = set(allcards) # partner model
		self.opp1m = set(allcards) # opponent 1 model
		self.opp2m = set(allcards) # opponent 2 model
		
		self.reset()
		
	def setHand(self, hand):
		Player.setHand(self, hand)
		self.tfc -= set(self.hand)
		
	def setRelations(self, partner, opp1, opp2)
		self.partner = partner
		self.opp1 = opp1
		self.opp2 = opp2
		
	def playCard(self):
		pass

	def updateInfo(self, winner):
		assert len(game.center) == 4, "there should be four cards in the center"
		self.tfc -= set(finished_trick.center.keys())
		
		for c, p in game.center.items():
			if p == self: continue
			
			# if they lost then we can consider that they do not have any better cards in their hand
			if self.opp1 != winner and self.opp2 != winner
				
			else:
				pass

	def orderUp(self, center_card):
		pass

	def pickSuit(self, out_suit):
		pass

	def pickUp(self, card):
		pass

	def reset(self):
		"""Reset the information gathered by the ai without reinstatiating it.
		
			For use between rounds. Useful for those that need to keep their statistics.
		"""
		self.hearts = set(filter(lambda c: c.suit == heart, allcards))
		self.spades = set(filter(lambda c: c.suit == spade, allcards))
		self.clubs = set(filter(lambda c: c.suit == club, allcards))
		self.diamonds = set(filter(lambda c: c.suit == diamond, allcards))

class SimpleRules(Player):
	# this ai will use arbitrary rules created by us to play the game
	# defaulting to random play when unsure
	def __init__(self, name):
		self.BaseSetUp(name)
		
	def playCard(self):
		pass

	def updateInfo(self, winner):
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
		
class RealPlayer(Player):
	def __init__(self, name):
		self.BaseSetUp(name)
	
	def playCard(self):
		self.printHand()
		move = int(raw_input("Please enter the # of the card you wish to play: "))
		valid = self.validMoves()
		while True:
			if type(move) is int and 0 <= move < len(self.hand) and self.hand[move] in valid:
				choice = self.hand.remove(move)
				return choice
			else:
				move = int(input("Please enter a valid move: "))
				
	def updateInfo(self, winner):
		print "The scores are A: %s, B %s" % (game.scoreA, game.scoreB)
		print "The winner of the previous trick was %s" % (winner)
		print "The center of the table is %s" % ", ".join(game.center.keys())

	def orderUp(self, center_card):
		self.printHand()
		if self == game.dealer:
			if query_yes_no("Do you want to pick up %s?" % (center_card)):
				return True

		else:
			return query_yes_no("Do you want to order the dealer up: %s?" % (center_card))

	def pickSuit(self, out_suit):
		open_suits = (set(heart, spade, diamond, club) - set(out_suit))
		if query_yes_no("Do you want to pick a suit? (out suit is %s)" % out_suit):
			print "Pick %s, %s, or %s." % (open_suits[0], open_suits[1], open_suits[2])
			
			while True:
				choice = raw_input("Enter the first letter of the suit name: ").lower()
				if choice[0] == 'd':
					if diamond in open_suits:
						return diamond
				elif choice[0] == 'h':
					if heart in open_suits:
						return heart
				elif choice[0] == 's':
					if spade in open_suits:
						return spade
				elif choice[0] == 'c':
					if club in open_suits:
						return club
				else:
					print "Please enter a valid choice."
		else:
			return False
		
	def pickUp(self, center_card):
		print "You are picking up %s." % (center_card)
		print "Your hand contains:",
		self.printHand()
		
		move = int(raw_input("Please enter the # of the card you wish to discard: "))
		while True:
			if type(move) is int and 0 <= move < len(self.hand):
				choice = self.hand.remove(move)
				self.hand.append(center_card)
				return choice
			else:
				move = int(input("Please enter a valid discard: "))
	
	def reset(self):
		# not necessary for a real player
		pass
