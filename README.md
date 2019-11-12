# Zombie-game
A small game that finds the optimal strategy for Alice to score more "brains" than Bob, given full information disclosure.

Sample input and output: 
input: "BSS|BFS|BBF|SFS|SBF|BSB|SSF|BSB|BBB|FFB|BSS"
output: "Alice's optimal strategy is to stick with rule of  2;
               scores: Alice 5 , Bob 2"

Game rules (note: it is originally a board game designed by Steve Jackson, but I made substantial changes to it):

In this game you play a zombie who must balance its desire for human brains with its fear of getting blasted to necrotic bits by a shotgun.

The rules are simple: The game comes with specially marked dice. The dice have three kinds of markings: brains(B), shotgun blasts(S), and footprints(F). Both Alice and Bob are zombies. When it's your turn, pull three dice from the cardboard cup (without looking) and roll them. Set any brains to one side. Set any shotgun blasts to the other side. Footprints mean the human got away - keep those in front of you. Do you want to roll again? No problem. Just re-roll the footprints dice along with enough fresh dice from the cup so that you roll three dice. You can roll as many times as you like in an effort to eats lots of brains in your turn, but if you end up accumulating three shotgun blasts, you lose all your brain points for that turn and the next player-zombie gets its turn. When all inputs are read, whoever scores most brains wins.

Alice has a rule of m, which means she will not stop in her turn unless she scores at least m brains or she accumulates 3 shotguns. Bob always sticks to the rule of 3. And this small program is designed to find out the optimal m value that Alice should take to maximize her scores.
