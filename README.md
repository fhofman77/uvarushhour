# UvA Rushhour Algorithms
### Breadth-First, Depth-First & Random
# Description
<img src="https://user-images.githubusercontent.com/70511386/122947786-b8831000-d37a-11eb-9ccc-5ed741d6cb63.png" alt="Image of what a board could look like" width="300"/>

The goal of this project was to find moves used to finish a game of Rush Hour. Rush Hour is a well known game, in which certain car needs to exit the field on the right side. However, other cars are in the way. Cars can only move in the oriëntation in which they set on the field. The algorithm worked on the principle of moving cars, but only if this move would result in a board-state (the way the cars are on the field) was not seen before. Repeating board states will cause the algorithm to drop that path as a winning path (unless it's the random algorithm).

![Board states traversal tree](https://user-images.githubusercontent.com/70511386/122955302-48778880-d380-11eb-8afd-8c2a3416fddd.png)




## Breadth First
The Breadth first algorithm was used to fulfill the main goal of this project, to win the game, with the least amount of moves. It was not the fastest in terms of time, as it would branch out from the original board state, to all possible board states within 1 move (child board states), before moving to the children of these new board states. While this takes more time, it would always result in the solution with the least amount of moves possible, as it would traverse the 'board-states' tree horizontally first. The numbers here indicate how the algorithm would traverse the board states. 

![Breadth first numbering of board states](https://user-images.githubusercontent.com/70511386/122954299-993ab180-d37f-11eb-8266-57d87909d400.png)


## Depth First
The depth first algorithm would continue on the first found child board state as a parent-board, instead of returning to the layer before and calculating all possible moves/child board states, like breadth first did. This resulted in the algorithm finding a possible solution more quickly most of the time, but it is mostly left to chance if this solution with not a lot of moves, as the algorithm traverses the 'board-states tree' downwards. Repeating board states will cause the algorithm to drop that path as a winning path.
![Board states in a tree: Depth first](https://user-images.githubusercontent.com/70511386/122954259-92ac3a00-d37f-11eb-8b4c-86b0e0cb002b.png)



## Random
As the name suggests, this algorithm takes a random car from the board, and performs a random legal move. While over time this will almost always lead to a game being won, the amount of moves that are made is left totally to chance. Solutions of this algorithm differ alot in terms of the amount of moves it takes to win, however the runtime of this algorithm is still very quick, as it consists of just a few lines of code and no remembering of whole board states.



<sub><sup>By: Felix Blom, Frank Hofman & Merrin Maas</sup></sub>
