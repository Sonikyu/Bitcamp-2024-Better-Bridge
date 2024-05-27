# Modified Bridge Card Game
 A Python implementation of the popular card game [Bridge](https://en.wikipedia.org/wiki/Contract_bridge) with a few modifications to the rules. 
 Originally, built during the hackathon Bitcamp to make it easier for our team to play our version of bridge virtually during the Summer Break when we would be separated.

## How It's Made
**Tech Used:** Python, Pygame

We chose python, because we wanted to implement a Reinforcement Learning algorithm interface from RLCard to improve our bot players.

## How to play
The 4 players are each given 13 cards. 
There are two teams of 2 with your partner being across from you. You cannot see your partners card and you can't discuss what cards you have with your partner.

The game is split into 2 parts
1. The Auction
2. The Game
### The Auction
**Goal:** To bet on the amount of wins that you and your partner can fulfill during the game. 

**Order of Suits:** Low -> Clubs -> Diamonds -> Hearts -> Spades -> High (Lowest to highest)

1. A random person is picked to start the auction. They need to choose the trump suit and the number of wins they can fulfill with their partner.
  - Players can only bet their number of wins between 7-13
  - Low and High means there are no trump suits and that either the lowest or highest card of the round that is the same suit as the first card placed down will win)

2. The next player (the order of players is clockwise) chooses whether or not to bet over the first player or to pass (meaning they accept the contract chosen)
  - If they make the bet they'll have to bet higher based on the order of suit or the number of wins they have to make and the betting round will start over
  - If all 3 other player chose pass, the game will start with the trump suit and number of wins picked. **Note:** the team that didn't win the bet will have to win 13 - the amount of wins the other team betted.

3. The Auction stage ends

### The Game
**Goal:** To fulfill your teams contract before the other team does
**Order of Rank** 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace (lowest to highest)
1. The person who won the bet will have to play their card first
2. The person who goes next (clockwise order) will have to pick a card from the same suit, unless they don't have any cards of that suit in which case they could choose any card from their deck
3. After all players have drawn a card from their deck, the winner will start the next game
4. The team that fulfills their contract first wins
5. The game will end once all 13 rounds have been played

## RoadMap
- [X] Game Stage
- [ ] Auction Stage
- [X] Start Screen
  - [X] Multiplayer, Single Player, Settings, and Quit Button
- [X] Proper End Screen
  - [X] Leaderboard
  - [X] Quit and Try Again Buttons
- [ ] Setting
  - [ ] Option to change music volume
  - [ ] Option to change sound effect volume
- [ ] Multiplayer
  - [ ] 4-2 player mode
- [ ] Proper Reinforcement Learning Interface Implementation 
- [ ]  Quality of Life Improvements
  - [X] Show how many wins each team has to fulfill
  - [ ] Show which team the player is on
  - [ ] Animations
  - [ ] An error box in response to the user clicking on a move they can't make
  - [X] Music
  - [X] Sound effects

## Credit
### Authors
1. [Alex Tsai](https://github.com/Sonikyu) (Backend)
2. [Andy Liao](https://github.com/AndyLiao1) (Backend & Front-end)
3. [John Riganati](https://github.com/JPR3) (Front-end)
5. [Max Park](https://github.com/Parkm465) (Backend & Front-end)

### Acknowledgements
[RLCard](https://rlcard.org/index.html)
