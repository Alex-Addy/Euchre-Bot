
import AIs

def testAI(cur_ai):
	# if the attribute does not exist this will raise an attribute error for the missing function
	cur_ai.playCard
	cur_ai.updateInfo
	cur_ai.orderUp
	cur_ai.pickUp
	cur_ai.pickSuit
	cur_ai.reset
	cur_ai.setHand

# Test that all AIs have the necessary functions
testAI(AIs.RandomPlay("R"))
print "RandomPlay is good."
testAI(AIs.SimpleStat("SS"))
print "SimpleStat is good."
testAI(AIs.SimpleRules("SR"))
print "SimpleRules is good."
testAI(Ais.RealPlayer("RP"))
print "RealPlayer is good."