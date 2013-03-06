Euchre-Bot
==========

An implementation of the card game euchre and a bot to play it.
It currently has two bots; a random play bot and a simple stat bot. Both bots play within the rules.
The simple stat bot uses some knowledge of the rules of the game to determine the what cards the other players may or may not have, then makes a move based upon that. Rather simplistic and arbitrary.



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
(This is wrong, merely kept here for possible future work)
We will be using rules to determine what the possible moves are as well as what other possibilities there are.

They will be in a string of the form "conditional ? then : else" this will allow us to easily add and change rules in the future.
```python
moving_rules = ["trick.lead in hand ? [x for x in hand if x.suit == trick.lead] : hand[:]]
poss_moves = []
poss_moves.extend(eval(moving_rules[0]))
```
