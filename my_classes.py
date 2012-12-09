from my_globals import *

# holder and runner of the entire game
class Euchre():
    def __init__(self, ):
		self.playerA1 = None
        self.playerA2 = None
        self.playerB1 = None
        self.playerB2 = None
        self.deck = list(allcards[:]) # get a deep copy of all_cards for dealing
            
    def start(self, ): # begins the first round
        # determine first dealer
        playRound()
        
    def dealCards(self, ):
		random.shuffle(self.deck) # mutates deck
            
        for x in range(1, len(players)+1):
            players[(x+dealer)%4].setHand(self.deck[:5])
            self.deck = self.deck[5:]
		
	def playRound(self, ): # begins the next 5 tricks
        # Plays 5 tricks
        if hasWinner():
            endGame() # if winner is found, end the game
        else
            playRound() # no winner, play another round
	
	def playTrick(self, ):
		pass
        
    def hasWinner(self, ):
        if game.teamA >= 10:
            print "Team A Has won!"
            return true
        elif game.teamB >= 10:
            print "Team B Has won!"
            return true
        else
            return false

    def endGame(self, ): # ends the game
        pass
		
	def getWinningCard(self, ):
		temp = [(x, self.curCardVal(x)) for x in game.center]
		best = temp[0][1]
		bext_x = 0
	
		for x in range(1, len(temp)):
			if temp[x][1] > best:
				best = temp[x][1]
				best_x = x
		
		return temp[x][0]
		
	def curCardVal(card, ):
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

class Round(object):
	def __init__(self, all_cards, players, dealer):
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
		
	def play(self, players, dealer)
		self.setUp(players, dealer)
		self.tricks = []
		cur_leader = (dealer+1)%4
		for x in range(1,6):
			self.tricks.append(Trick(leader=cur_leader))
			cur_leader = self.tricks[x].play(players, self.
	
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