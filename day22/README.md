# Unsuccessful approaches

- In my previous approach I searched all combinations of size 1, size 2, size 3,...
- This became to slow to run around size 12 or so
- I tried some things like generator instead of list, filtering out certain combos, etc.
- Unfortunately this still didn't work - sometimes filtering made things take longer!

# More Successful approaches

- In my ultimately successful approach I start by searching all combinations of size 1.
- If there is no result (player win/lose, mana overspend, etc) then I append each of the 5 spells to be searched in round 2
- For example: [sheild] -> [sheild,recharge], [sheild,magic missle], [sheild,drain], etc
- The key idea is that this does automatic pruning relative to my first approach - I don't continue to check paths that already had a result somewhere previously
- Unfortunately this was still too slow
- What I did then was only search a single plausible starting point to try to get a win
- For example [sheild,recharge,poison]
- To speed this up I only continued searching a move combo if the difference in player and boss HP was < some number, e.g. 35
- If things got too far apart then the boss was probably gonna win
- Eventually I found a winning combo and an associated value for total mana spent
- I then used this total mana spent value to help prune further combos - if total mana spent goes higher that that of my win then stop checking
- Ultimately, I then started with each individual spell and built up moveset combos limiting to those combos with total mana spent <= the total mana value for the win I got
- This sped things up enough to get the minimum value after 2-3min

- Part 2 was a straightforward modificationa and ran even faster
