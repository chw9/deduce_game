# Caroline Winakur 2022
# Based on Deduce or Die game

import random
from os.path import exists
from readline import get_history_length

class Card:
    def __init__(self, value, suit):
         self.val = value
         self.suit = suit

    def __str__(self):
        if self.val == 1:
            return f"A of {self.suit}"
        return f"{self.val} of {self.suit}"
    
    def __eq__(self, other): 
        if not isinstance(other, Card):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.val == other.val and self.suit == other.suit

numbers = (1, 2, 3, 4, 5, 6)
suits = ("spades", "hearts", "clubs")
murderer = Card
p1, p2, p3 = [], [], []

deck = []

for i in range(len(numbers)):
    deck.append(Card(numbers[i], suits[0]))
    deck.append(Card(numbers[i], suits[1]))
    deck.append(Card(numbers[i], suits[2]))

q_deck = deck + deck

def copy_deck(deck):
    new_deck = []
    for i in range(len(deck)):
        new_deck.append(deck[i])
    return new_deck

"""
make a copy of the question cards deck so you can track which are left.
once remaining = 0, reset by making a new copy of q_deck then shuffling
"""
q_deck_remaining = copy_deck(q_deck)

""" 
reorders the deck list. alternately could implement so that it creates a new deck 
to maintain order of previous deck, but really no reason to (this saves memory)
"""
def shuffle(deck):
    for i in range(len(deck)):
        rand = random.randrange(0, i + 1)
        temp = deck[i]
        deck[i] = deck[rand]
        deck[rand] = temp

# in future: add num_players variable?? not sure about game rules
def deal(deck):
    """
    returns the hands for three players and evidence cards as lists, returns the witness card as int
    """
    p1 = []
    p2 = []
    p3 = []
    e = []
    w = Card
    
    for i in range(len(deck)):
        if i == len(deck) - 1 or i == len(deck) - 3:
            e.append(deck[i])
        elif i == len(deck) - 2:
            w = deck[i]
        elif i % 3 == 2:
            p1.append(deck[i])
        elif i % 3 == 1:
            p2.append(deck[i])
        else:
            p3.append(deck[i])

    # assign murderer value
    val = e[0].val + e[1].val
    val = val%6 if val > 6 else val

    suit = str

    if e[0].suit == e[1].suit:
        suit = e[0].suit
    else:
        cards = (e[0].suit, e[1].suit)
        suit = list(set(suits) - set(cards))
        suit = suit[0]
    
    m = Card(val, suit)

    f = open("dontread.txt", "w")
    f.write(f"p1 hand: {p1[0]}, {p1[1]}, {p1[2]}, {p1[3]}, {p1[4]}\n")
    f.write(f"p2 hand: {p2[0]}, {p2[1]}, {p2[2]}, {p2[3]}, {p2[4]}\n")
    f.write(f"p3 hand: {p3[0]}, {p3[1]}, {p3[2]}, {p3[3]}, {p3[4]}\n")
    f.write(f"evidence cards: {e[0]}, {e[1]}; murderer: {m}")

    return p1, p2, p3, e, w, m

def show_q_cards(q_deck_remaining):
    if len(q_deck_remaining) == 0:
        q_deck_remaining = shuffle(copy_deck(q_deck))

    three_q_cards = (q_deck_remaining[0], q_deck_remaining[1], q_deck_remaining[2])
    for i in range(3):
        q_deck_remaining.remove(q_deck_remaining[0])
    return three_q_cards

# TODO: maybe add "confirm selection? y/n"
# player = 1, 2, or 3 depending on whose turn it is; default is 1
def get_q_selection(three_cards, player=1):
    print(f"  Card options: 1.) {three_cards[0]}, 2.) {three_cards[1]}, 3.) {three_cards[2]} ")
    print("  Remember: order matters! Range will be determined in order of selection.")
    choice = input("> Select two cards for your question by typing two numbers (no spaces or punctuation): ")
    c1 = int(choice[0:1]) - 1
    c2 = int(choice[1]) - 1

    selected = (three_cards[c1], three_cards[c2])

    p = list(set((1, 2, 3)) - set([player]))

    player = input(f"\nWould you like to interrogate player {p[0]} or player {p[1]}? ({p[0]}/{p[1]}): ")

    return selected, player

def parse_question(two_cards, player):
    c1 = two_cards[0]
    c2 = two_cards[1]

    hand = ()
    if player == "1":
        hand = p1
    elif player == "2":
        hand = p2
    else:
        hand = p3

    q = str
    a = 0

    if c1.val == c2.val and c1.suit == c2.suit:
        q = f"do you have the {c1}?"
        a = 1 if c1 in list(hand) else 0
    elif c1.val == c2.val:
        q = f"how many {c1.val}s do you have?"

        for card in hand:
            if card.val == c1.val:
                a=a+1
    elif c1.suit == c2.suit:
        q = f"how many {c2.suit} do you have between {c1.val} and {c2.val}, inclusive?"

        for card in hand:
            if c1.val < c2.val:
                if card.suit == c1.suit and card.val >= c1.val and card.val <= c2.val:
                    a=a+1
            else:
                if card.suit == c1.suit and (card.val >= c1.val or card.val <= c2.val):
                    a=a+1
    else:
        q = f"how many cards do you have between {c1.val} and {c2.val}, inclusive?"

        for card in hand:
            if c1.val < c2.val:
                if card.val >= c1.val and card.val <= c2.val:
                    a=a+1
            else:
                if card.val >= c1.val or card.val <= c2.val:
                    a=a+1

    print(f"    @ player {player}: {q}")
    s = "" if a == 1 else "s"
    print(f"> Player {player} has {a} card{s} in this range")

def accusation(player=1):
    if (player == 1):
        guess = input("\nWhich player is the murderer? (2 or 3): ")
        player_hand = p1
    elif (player == 2):
        guess = input("\nWhich player is the murderer? (1 or 3): ")
        player_hand = p2
    else:
        guess = input("\nWhich player is the murderer? (1 or 2): ")
        player_hand = p3


    hand = p1 if guess == "1" else p2 if guess == "2" else p3
    one_higher = Card(murderer.val + 1, murderer.suit)

# TODO: account for if one higher is also in the player's hand
    if murderer in hand or (murderer in player_hand and one_higher in hand) or (murderer == w and one_higher in hand):
        evidence_guess_one = input("What do you think the first evidence card is? Order doesn't matter.\nFormat as [number 1-6][suit: c, h, s]. eg 3h is 3 of hearts.\nYour guess: ")
        evidence_guess_two = input("What do you think the second evidence card is? Order doesn't matter.\nFormat as [number 1-6][suit: c, h, s]. eg 3h is 3 of hearts.\nYour guess: ")

        suit1 = "clubs" if evidence_guess_one[1] == "c" else "hearts" if evidence_guess_one[1] == "h" else "spades"
        suit2 = "clubs" if evidence_guess_two[1] == "c" else "hearts" if evidence_guess_two[1] == "h" else "spades"

        e1 = Card(int(evidence_guess_one[0:1]), suit1)
        e2 = Card(int(evidence_guess_two[0:1]), suit2)

        if (e1 == e[0] and e2 == e[1]) or (e2 == e[0] and e1 == e[1]):
            print("Congratulations, you win!")
        else:
            print("Sorry, that's not correct... look at dontread.txt for the answer.")
    else:
        print("Sorry, that's not correct... look at dontread.txt for the answer.")


################################## gameplay: ##################################

shuffle(deck)
shuffle(q_deck_remaining)
p1, p2, p3, e, w, murderer = deal(deck)

playing = True
q_num = 1

print(f"\nQuestion {q_num}: ")

while playing:
    a = show_q_cards(q_deck_remaining)
    sel_cards, p = get_q_selection(a)
    parse_question(sel_cards, p)
    guess = input("\nWould you like to make an accusation (y), continue (n), or quit (q)? (y/n/q): ")

    if guess == "y":
        accusation()
        playing = False
    elif guess == "q":
        print("\nOkay")
        playing = False
    else:
        q_num = q_num + 1
        print(f"\nQuestion {q_num}: ")

