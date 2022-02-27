# Raichu:
### Approach:
This board game is played using minimax algorithm using alpha-beta pruning. The game runs for different depth, from 1 to 20 and returns the best board found after every depth so we can break at any point and get the best answer time can give. The function will return the state if the very next state is the winning state and won't run for further depth. Though program rarely go beyond depth 4-5 as the states increases exponentially even when using alpha-beta pruning (For depth 20, number of states will be approximately 40^20!).


### Successor:
Successors are created in the succ() function which stores all the possible successor in the fringe and returns it.


### Evaluation function:
(10*(W-B)+ 10*(w-b) + 50*(w_raichu-b_raichu)+depth) is my evaluation function. Where W == White Pikachu, w == white pichu, B == Black Pikachu, b == black pichu.
Both the raichus are given given higher weights then pikachus and pichus as they have more freedom of movement. And depth is also one factor where we can get better result at shallow depth(root node have higher number).
