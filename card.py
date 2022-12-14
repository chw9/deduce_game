# Caroline Winakur 2022
# Based on Deduce or Die game http://www.thegamesjournal.com/rules/DeduceOrDie.shtml

import random
from os.path import exists

class Card:
    """
    class to create Card objects which are used for gameplay
    """
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
    """
    flips the next three cards in the q_deck and returns them as a tuple
    """
    # TODO: make this work properly (currently reshuffles deck each time after q_deck_remaining depletes)
    # probably an issue with variable scope
    if len(q_deck_remaining) == 0:
        q_deck_remaining = copy_deck(q_deck)
        shuffle(q_deck_remaining)
    
    print(len(q_deck_remaining))

    three_q_cards = (q_deck_remaining[0], q_deck_remaining[1], q_deck_remaining[2])
   
    for i in range(3):
        del q_deck_remaining[0]
        # print(len(q_deck_remaining))
    return three_q_cards, q_deck_remaining

# TODO: maybe add "confirm selection? y/n"
# player = 1, 2, or 3 depending on whose turn it is; default is 1
def get_q_selection(three_cards, player=1):
    """
    method for command line version of the game (uses printed prompts rather than GUI)
    """
    print(f"  Card options: 1.) {three_cards[0]}, 2.) {three_cards[1]}, 3.) {three_cards[2]} ")
    print("  Remember: order matters! Range will be determined in order of selection.")
    choice = input("> Select two cards for your question by typing two numbers (no spaces or punctuation): ")
    c1 = int(choice[0:1]) - 1
    c2 = int(choice[1]) - 1

    selected = (three_cards[c1], three_cards[c2])

    p = list(set((1, 2, 3)) - set([player]))

    player = input(f"\nWould you like to interrogate player {p[0]} or player {p[1]}? ({p[0]}/{p[1]}): ")

    return selected, player

def parse(firstcard, secondcard, player, hand):
    """
    function for graphical version, determines the number of cards the player has in the 
    interrogation range and returns as a string
    """
    numcards = 0

    if firstcard.val == secondcard.val and firstcard.suit == secondcard.suit:
        numcards = 1 if firstcard in list(hand) else 0
    elif firstcard.val == secondcard.val:
        for card in hand:
            if card.val == firstcard.val:
                numcards=numcards+1
    elif firstcard.suit == secondcard.suit:
        for card in hand:
            if firstcard.val < secondcard.val:
                if card.suit == firstcard.suit and card.val >= firstcard.val and card.val <= secondcard.val:
                    numcards=numcards+1
            else:
                if card.suit == firstcard.suit and (card.val >= firstcard.val or card.val <= secondcard.val):
                    numcards=numcards+1
    else:
        for card in hand:
            if firstcard.val < secondcard.val:
                if card.val >= firstcard.val and card.val <= secondcard.val:
                    numcards=numcards+1
            else:
                if card.val >= firstcard.val or card.val <= secondcard.val:
                    numcards=numcards+1

    s = "" if numcards == 1 else "s"
    return (f"Player {player} has {numcards} card{s} in this range")

def accuse(player_hand, hand, e1_guess, e2_guess, witness, true_e1, true_e2, murderer):
    """
    graphic version, determines if user's guess is correct, accounts for if the murderer
    card is in the user's hand, evidence, or witness cards. returns true if user wins
    """
    frame = Card(murderer.val, murderer.suit)

    while frame in player_hand or frame == witness or frame == true_e1 or frame == true_e2:
        frame = Card(frame.val + 1 if frame.val < 6 else 1, frame.suit)

    if frame in hand:
        if (e1_guess == true_e1 and e2_guess == true_e2) or (e2_guess == true_e1 and e1_guess == true_e2):
            return True
        else:
            return False
    else:
        return False