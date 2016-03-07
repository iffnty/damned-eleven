from collections import namedtuple
from random import sample
from time import time


def deal_cards(deck):
    player = set(sample(deck, 5))
    house = set(sample(deck - player, 5))
    last_card = (deck - player - house).pop()
    return player, house, last_card


def play_card(player_hand, house_hand):
    return player_hand.pop(), house_hand.pop()


def open_cards(player_card, house_card):
    table = (player_card, house_card)
    # If Joker was played
    if "J" in table:
        other_card_index = 1 - table.index("J")
        if table[other_card_index] == 1:
            # 1 beats Joker, player with 1 wins
            return ("Player", "House")[other_card_index]
        else:
            # Joker beats every other card except 1, player with Joker wins
            return ("Player", "House")[table.index("J")]
    # Otherwise, compare numeric values of cards
    return ("Player", "House")[player_card < house_card]


def determine_winner(player_score, house_score, last_card):
    Result = namedtuple("Result", ["winner", "win_by_joker"])
    if player_score == 3:
        return Result("Player", False) #  Player Clear win
    elif house_score == 3:
        # Check last card
        if last_card == "J":
            return Result("Player", True) # Player Joker win
        else:
            return Result("House", False) #  House win


def play(deck):
    player_hand, house_hand, last_card = deal_cards(deck)
    player_score, house_score = 0, 0
    for r in range(5):
        player_card, house_card = play_card(player_hand, house_hand)
        outcome = open_cards(player_card, house_card)
        if outcome == "Player":
            player_score += 1
        else:
            house_score += 1

        if player_score == 3 or house_score == 3:
            return determine_winner(player_score, house_score, last_card)


def main():
    start_time = time()
    deck = set(range(1,11)) ^ {"J"}
    total_games = 10**4
    player_stats = {"wins": 0, "by_joker": 0}
    house_stats = {"wins": 0}
    for i in range(total_games):
        outcome = play(deck)
        if outcome.winner == "Player":
            player_stats["wins"] += 1
            if outcome.win_by_joker:
                player_stats["by_joker"] += 1
        else:
            house_stats["wins"] += 1

    # Display statistics
    delta = time() - start_time
    print("-"*40)
    print("Total games played: {total_games} (in {delta:.2f} seconds)".format(total_games=total_games, delta=delta))
    print("-"*40)
    # Player
    print("Player win rate: {rate:.2f}%".format(rate=player_stats["wins"] / total_games * 100))
    joker_stats = {"joker_total": player_stats["by_joker"] / total_games * 100,
                    "joker_wins_pecentage": player_stats["by_joker"] / player_stats["wins"] * 100 if player_stats["wins"] else 0}
    print("Joker win percentage: {joker_wins_pecentage:.2f}% ({joker_total:.2f}% of all games)".format(**joker_stats))
    print("-"*40)
    # House
    print("House win rate: {rate:.2f}%".format(rate=house_stats["wins"] / total_games * 100))
    print("-"*40)


if __name__ == '__main__':
    main()
