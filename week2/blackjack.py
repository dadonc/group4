import random

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
suits_values = {"Spades": "\u2664", "Hearts": "\u2661",
                "Clubs": "\u2667", "Diamonds": "\u2662"}
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards_values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}


class Card:
    def __init__(self, suit, card, value):
        self.suit = suit
        self.card = card
        self.value = value

    def __str__(self):
        return f"[{self.suit} {self.card}]"


def create_deck():
    deck = []
    for suit in suits:
        for card in cards:
            deck.append(Card(suits_values[suit], card, cards_values[card]))
    random.shuffle(deck)
    assert len(deck) == 52
    return deck


def print_cards(cards, prefix="", hide_first=False):
    print(prefix, end=" ")
    if hide_first:
        print("[??]", end=" ")
        cards = cards[1:]
    for card in cards:
        print(card, end=" ")
    if not hide_first:
        print(f"(sum: {sum([card.value for card in cards])})", end=" ")
    print()


if __name__ == "__main__":
    deck = create_deck()
    player_hand = []
    player_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand = []
    dealer_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    print_cards(dealer_hand, "Computer's cards:", True)
    print_cards(player_hand, "Player's cards:", False)

    while True:
        draw_new = input("\nDraw a new card? (y/n)")
        if draw_new == "y":
            new_card = deck.pop()
            player_hand.append(new_card)
            print(f"Player drew a/an {new_card}")
            sum_player = sum([card.value for card in player_hand])
            if sum_player > 21:
                # print computer's full hand if player has lost
                print_cards(dealer_hand, "Computer's cards:", False)
            else:
                print_cards(dealer_hand, "Computer's cards:", True)
            print_cards(player_hand, "Player's cards:", False)
            if sum([card.value for card in player_hand]) > 21:
                print("\nUser went over 21. COMPUTER WINS!\n")
                break
        elif draw_new == "n":
            print("User holds.")
            print_cards(dealer_hand, "Computer's cards:", False)
            print_cards(player_hand, "Player's cards:", False)
            sum_player = sum([card.value for card in player_hand])
            sum_dealer = sum([card.value for card in dealer_hand])
            if (sum_player > sum_dealer):  # assuming dealer never draws a new card
                print("\nPLAYER WINS!\n")
            else:  # assuming dealer wins ties
                print("\nCOMPUTER WINS!\n")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
