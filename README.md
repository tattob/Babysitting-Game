# Babysitting-Game
A text based hide and seek game made in python that randomizes layout and hiding location. Plays in terminal.

Each new room is generated as you enter it, including its spots and number of exits. Until the kid is placed, each newly generated spot has a 1-in-30 chance of containing them.

There are several possible softlocks, though none are particularly likely. You could run out of paths before the kid is generated, get unlucky with one of the few rooms that can generate with only a single exit, or run out of rooms before either the kid or the key item needed to unlock their hiding spot is generated.

Both of the latter scenarios are phenomenally unlikely. If any of these softlocks happen to you, please let me know. It would be a statistical marvel.
