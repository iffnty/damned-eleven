# Damned Eleven
![Build status](https://api.travis-ci.org/iffnty/damned-eleven.svg)

Game playing simulation

# Gameplay
*"Damned Eleven"* is a card game played by two players (Stranger (Player) and Innkeeper (House)) with an 11-card deck composed of number cards 1 through 10 and a Joker. Each player receives 5 cards, 1 at a time, and the last card forms a talon.
At the start of each turn each player picks one card and lays it on the table face-down. Then the cards are revealed and compared.

# Earning points
The following rules are applied when comparing cards:
- 1 beats Joker
- Joker beats every other card (except 1)
- Greater number card beats lesser number card

Round winner receives 1 point. Game ends when one player has 3 points.

# Determining the winner

If Stranger has 3 points, he wins.

If Innkeeper has 3 points, the talon card is revealed:
- If the talon card is Joker, Stranger wins
- Otherwise, Innkeeper wins

# Possible modifications
- Innkeeper is always dealt 6
- Joker and 1 are always dealt into different hands
