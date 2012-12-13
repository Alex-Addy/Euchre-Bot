# coding:utf-8

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

class Logger:
	def __init__(self, logging_file):
		self.log = open(logging_file, 'w')
		
	def log(self, info):
		self.log.write(info)
		self.log.write('\n')
		
out = Logger()

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
		keys = game.center.keys()
		out.log("End of trick:\n\t%s, %s, %s, %s\n" % (keys[0], keys[1], keys[2], keys[3]))
		self.lead = None
		self.center = {}
	
	def resetRound(self):
		out.log("End of round:\n\tTrump: %s\n\tCaller: %s\n\tScores A: %d B: %d\n" % \
			(self.trump, self.caller.name, self.scoreA, self.scoreB))
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
		
def query_yes_no(question, default="yes"):
    """
	Ask a yes/no question via raw_input() and return their answer.
	source: http://stackoverflow.com/a/3041990
    """
    valid = {"yes":True,   "y":True,  "ye":True,
             "no":False,     "n":False}
			 
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        print (question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print "Please respond with 'yes' or 'no' (or 'y' or 'n').\n"