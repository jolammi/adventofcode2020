import traceback
from collections import deque


def read_data():
    with open("input.txt", "r") as handle:
        data = handle.read()
        data = data.replace("Player 1:", "")
        data = data.replace("Player 2:", "")
        print(data)
        data = data.split("\n\n")
        data = [i.split("\n") for i in data]
        data = [[int(i) for i in player_cards if i] for player_cards in data]
        return deque(data[0]), deque(data[1])


def play_game(p1_deck, p2_deck):
    while p1_deck and p2_deck:
        print(f"Player1 deck: {p1_deck}")
        print(f"Player2 deck: {p2_deck}")
        p1 = p1_deck.popleft()
        p2 = p2_deck.popleft()
        print("P1:", p1)
        print("P2:", p2)
        if p1 > p2:
            p1_deck.append(p1)
            p1_deck.append(p2)
            print("p1 wins round")
        elif p2 > p1:
            p2_deck.append(p2)
            p2_deck.append(p1)
            print("p2 wins round")
    winner_deck = []
    if p1_deck:
        print("P1 won game")
        print("P1 deck", p1_deck)
        winner_deck = list(p1_deck)
    if p2_deck:
        print("P2 won game")
        print("P2 deck", p2_deck)
        winner_deck = list(p2_deck)
    winner_score = 0

    length = len(winner_deck)
    for idx, i in enumerate(winner_deck):
        winner_score += i*(length-idx)
    return winner_score


if __name__ == "__main__":
    try:
        player1_deck, player2_deck = read_data()
        winner_score = play_game(player1_deck, player2_deck)
        assert winner_score == 29764
        print(f"The winner wins with a score of {winner_score}")
    except Exception:
        print("Please learn how to code")
        traceback.print_exc()
