Euchre-Bot
==========

An implementation of the card game euchre and a bot to play it.



Setup
=====

Player
------
name:str
tricks:int
...

Card
-----
suit:suit
num:int

Trick
-----
center:[(player:Card),...]
lead:player

Round
----
trump:suit
caller:player
deck:cards


Rules
=====
We will be using rules to determine what the possible moves are as well as what other possibilities there are.

They will be in a string of the form "conditional ? then : else" this will allow us to easily add and change rules in the future.
```python
moving_rules = ["trick.lead in hand ? [x for x in hand if x.suit == trick.lead] : hand[:]]
poss_moves = []
poss_moves.extend(eval(moving_rules[0]))
```