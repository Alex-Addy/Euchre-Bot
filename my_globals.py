if True: # black characters
	heart = u"\u2665"
	spade = u"\u2660"
	diamond = u"\u2666"
	club = u"\u2663"
else: # white characters
	heart = u"\u2661"
	spade = u"\u2664"
	diamond = u"\u2662"
	club = u"\u2667"
	
class Info:
	def __init__(self):
		# trick level
		self.dealer = None # player
		self.lead   = None # suit
		self.center = {} # array of {card:player} for cards in center of table
		
		# round level
		self.trump  = None # suit
		self.caller = None # player
		self.tricksA = 0 # tricks gotten
		self.tricksB = 0
		
		# game level
		self.scoreA  = 0 # total score
		self.scoreB  = 0

	def resetTrick(self):
		self.lead = None
		self.center = {}
	   
	def resetRound(self):
		self.trump = None
		self.caller = None
		self.tricksA = 0
		self.tricksB = 0

game = Info()

class Card(object):
	def __init__(self, suit, num):
		self.suit = suit
		self.num = num

	def __str__(self):
		if self.num > 10:
			return ["Jack", "Queen", "King", "Ace"][self.num - 11] + "|" + self.suit
		else:
			return str(self.num) + "|" + self.suit

	def __repr__(self):
		return '<%s %s>' % (self.__class__.__name__, self.__dict__)

# a list of all possible cards, done as a tuple so that it cannot be accidently changed at runtime
allcards = tuple([Card(s, c) for s in (diamond, spade, club, heart) for c in (14, 13, 12, 11, 10, 9)])

def offSuit(trump_suit):
	"""
	Takes a suit and returns what the off hand suit would be.
	"""
	if trump_suit == heart:
		return diamond
	elif trump_suit == diamond:
		return heart
	elif trump_suit == spade:
		return club
	else:
		return spade