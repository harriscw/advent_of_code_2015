In my previous approach I searched all combinations of size 1, size 2, size 3,...
This became to slow to run around size 12 or so
In this approach I start by searching all combinations of size 1.
If there is no result (player win/lose, mana overspend, etc) then I append each of the 5 spells to be searched in round 2
for example: [sheild,recharge], [sheild,magic missle], [sheild,drain], etc
This does automatic pruning relative to my first approach.
Unfortunately its still too slow
Ultimately what I did was only search a single plausible starting point to try to get a win
For example [sheild,recharge,poison]
To speed this up I only continued searching a move combo if the difference in player and boss HP was <35
Eventually I got a win and an associated mana value
I then searched combos started with each individual spell limiting to combos with total mana spent <= the mana value for the win
This sped things up enough to get the minimum value after 2-3min
