# Deduce or Die (single player practice)
## Based on the 3-player version of Deduce or Die; rules and gameplay are similar to that of [the full version](http://www.thegamesjournal.com/rules/DeduceOrDie.shtml).

# How to use
Download this repo to your computer. Decide which version you want to play:

## Versions
### Graphic interface:
#### See images of the visible cards; ask questions and accuse by selecting options from dropdowns and clicking buttons. To play this version, run ```python deduce_graphic.py```.

- The interface will open with a new game. View your hand along the bottom of the screen and the witness card at the top.
- Click on the deck (facedown card in the middle row) to flip up the first three question cards.
- Use the dropdowns next to these three cards to select two cards and a player to direct the question to. Make sure to list the cards in the order you want the range to be evaluated in!
- Once you click "INTERROGATE", the answer to your question will display below the question cards.
- Click on the deck again to display the next three question cards.
- Continue flipping cards and asking questions until you wish to make a guess. Remember, once you guess, you will either win or lose - no second chances! 
- To make a guess, select options from the dropdowns in the top right of the screen, then click "GUESS". The order of the two evidence cards doesn't matter - just make sure you match up the correct value with the correct suit. Select the player who has the murderer card, or, if the murderer card is in your hand, the evidence cards, or the witness card, select the player with the card that you would like to frame.
- If you wish to see all of the hidden cards, click the "REVEAL" button at the bottom of the screen. This action will end the game. The murderer card is highlighted in yellow. If there is a frame card instead, it is highlighted in red.

### Command line:
#### Interact with the program by typing responses to prompts given in the command line. Use the exact response options given in the prompt. To play this version, run `python deduce.py`.

If you wish to see all of the hidden cards, look at the file `dontread.txt`.
