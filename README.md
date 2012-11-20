Euchre-Bot
==========

An implementation of the card game euchre and a bot to play it.

#Player
name:str
tricks:int
...

#Card
suit:suit
num:int

##team
score:int
tricks:int

##trick
center:[(player:Card),...]
lead:player

##hand
trump:suit
caller:player