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

# a list of all possible cards, done as a tuple so that it cannot be accidently changed at runtime
allcards = tuple([Card(s, c) for s in (diamond, spade, club, heart) for c in (14, 13, 12, 11, 10, 9)])