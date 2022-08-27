from PIL import Image
from card import *

flipped = 0
asked = 0

m = Image.open("cards/ace_of_clubs.png")
w, l = m.size 
scale_factor = .25

# shuffle(deck)
# shuffle(q_deck_remaining)

q_deck_remaining = copy_deck(q_deck)
