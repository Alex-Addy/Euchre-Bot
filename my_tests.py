
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
testAI(RandomPlay())
testAI(SimpleStat())
testAI(SimpleRules())
testAI(RealPlayer())