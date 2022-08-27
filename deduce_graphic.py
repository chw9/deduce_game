# Caroline Winakur 2022
# Based on Deduce or Die game http://www.thegamesjournal.com/rules/DeduceOrDie.shtml

import tkinter as tk
from PIL import ImageTk, Image
from card import *
import vars

# this is a method so that theoretically someday the "new game" button might be functional :D
def game_start():
    shuffle(deck)
    shuffle(q_deck_remaining)
    vars.asked = 0
    vars.flipped = 0

game_start()
p1, p2, p3, ev, witness, murderer = deal(deck)

murderer_frame_card = Card(murderer.val, murderer.suit)

while murderer_frame_card in p1 or murderer_frame_card == witness or murderer_frame_card in ev:
    murderer_frame_card = Card(murderer_frame_card.val + 1 if murderer_frame_card.val < 6 else 1, murderer_frame_card.suit)

#################### button commands #######################
# TODO:? move this to a separate file called button_commands.py then 
# from button_commands import new_game, reveal, ....... etc   ??

# clear all widgets in frame
def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()

# remove these frames
def del_frames():
    guess_frm.destroy()
    deck_frm.destroy()
    hand_frm.destroy()

# reveals the evidence cards, murderer card, and player who had it (or framed card)
def reveal():
    clear_frame(guess_frm)
    clear_frame(deck_frm)
    clear_frame(hand_frm)

    # TODO: prob don't use global? but don't want to deal with that now bc it works so /shrug
    global j
    j = []
    display_cards(guess_frm, p2, 2, j)
    global k
    k = []
    display_cards(deck_frm, p3, 3, k)

    # manually display witness, evidence, and murderer i guess
    hand_frm.columnconfigure(0, weight=1)
    hand_frm.columnconfigure(1, weight=1)
    hand_frm.columnconfigure(2, weight=1)
    hand_frm.columnconfigure(3, weight=1)
    hand_frm.rowconfigure(0, weight=1)
    hand_frm.rowconfigure(1, weight=2)

    tk.Label(text=f"W I T N E S S", master=hand_frm, bg=dk_green, fg="white").grid(row=0, column=0)
    tk.Label(text=f"E V I D E N C E", master=hand_frm, bg=dk_green, fg="white").grid(row=0, column=1, columnspan=2)
    tk.Label(text=f"M U R D E R E R", master=hand_frm, bg=dk_green, fg="white").grid(row=0, column=3)

    global w_card
    wit_card_name = card_path(witness)  
    wit_path = "cards/" + wit_card_name
    wit_img = Image.open(wit_path).resize([int(vars.w*vars.scale_factor), int(vars.l*vars.scale_factor)], Image.ANTIALIAS)
    w_card = (ImageTk.PhotoImage(wit_img))
    w_card_im = tk.Label(master=hand_frm, height=vars.l*vars.scale_factor, width=vars.w*vars.scale_factor, image=w_card, bg=dk_green)
    w_card_im.grid(row=1, column=0)

    global ev_1_card
    e1_card_name = card_path(ev[0])  
    e1_path = "cards/" + e1_card_name
    e1_img = Image.open(e1_path).resize([int(vars.w*vars.scale_factor), int(vars.l*vars.scale_factor)], Image.ANTIALIAS)
    ev_1_card = (ImageTk.PhotoImage(e1_img))
    e1_card_im = tk.Label(master=hand_frm, height=vars.l*vars.scale_factor, width=vars.w*vars.scale_factor, image=ev_1_card, bg=dk_green)
    e1_card_im.grid(row=1, column=1)

    global ev_2_card
    e2_card_name = card_path(ev[1])  
    e2_path = "cards/" + e2_card_name
    e2_img = Image.open(e2_path).resize([int(vars.w*vars.scale_factor), int(vars.l*vars.scale_factor)], Image.ANTIALIAS)
    ev_2_card = (ImageTk.PhotoImage(e2_img))
    e2_card_im = tk.Label(master=hand_frm, height=vars.l*vars.scale_factor, width=vars.w*vars.scale_factor, image=ev_2_card, bg=dk_green)
    e2_card_im.grid(row=1, column=2)

    global m_card
    m_card_name = card_path(murderer)  
    m_path = "cards/" + m_card_name
    hand_img = Image.open(m_path).resize([int(vars.w*vars.scale_factor), int(vars.l*vars.scale_factor)], Image.ANTIALIAS)
    m_card = (ImageTk.PhotoImage(hand_img))
    m_card_im = tk.Label(master=hand_frm, height=vars.l*vars.scale_factor, width=vars.w*vars.scale_factor, image=m_card, bg="yellow")
    m_card_im.grid(row=1, column=3)


# TODO: deal with this later. maybe need to segment functionality out to diff files/functions. idk bro
def new_game():
    clear_frame(guess_frm)
    clear_frame(deck_frm)
    clear_frame(hand_frm)

# get the file path for the image corresponding to a card
def card_path(card_name):
    return str(card_name).replace(" ", "_").replace("A", "ace") + ".png"

# show a group of cards (player hand)
def display_cards(frame, player, p, list_var):
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.columnconfigure(3, weight=1)
    frame.columnconfigure(4, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=2)

    tk.Label(text=f"P L A Y E R  {p} ' S  H A N D", master=frame, bg=(mid_green if p == 3 else dk_green), fg="white").grid(row=0, column=0, columnspan=5)
    for c in player:
        card_name = card_path(c)
        
        path = "cards/" + card_name
        hand_img = Image.open(path).resize([int(vars.w*vars.scale_factor), int(vars.l*vars.scale_factor)], Image.ANTIALIAS)
        list_var.append(ImageTk.PhotoImage(hand_img))
        # TODO: make this account for if murderer is in p1's hand
        card_im = tk.Label(master=frame, height=vars.l*vars.scale_factor, width=vars.w*vars.scale_factor, image=list_var[len(list_var)-1], bg=("yellow" if c == murderer else "red" if c == murderer_frame_card else mid_green if p == 3 else dk_green))
        card_im.grid(row=1, column=player.index(c))
    
# when deck card is clicked, show the next three cards if a question was asked for the previous three    
def flip_deck():
    if vars.flipped == vars.asked:
        a = show_q_cards(q_deck_remaining)
        global ii
        ii = []
        colind=1
        for card in a:
            card_name = card_path(card)

            path = "cards/" + card_name
            flip_img = Image.open(path)
            flip_img = flip_img.resize([int(vars.w*vars.scale_factor), int(vars.l*vars.scale_factor)], Image.ANTIALIAS)
            ii.append(ImageTk.PhotoImage(flip_img))
            im_ind = len(ii)-1
            card_im = tk.Label(master=deck_frm, bd=0, height=vars.l*vars.scale_factor, width=vars.w*vars.scale_factor, image=ii[im_ind], bg=mid_green)
            card_im.grid(row=0, column=(colind), rowspan=4)
            colind=colind+1

        vars.flipped = vars.flipped + 1

        a = list(a)
        if a[0] == a[1]:
            a[1] = str(a[1]) + " (2)"
        if a[0] == a[2]:
            a[2] = str(a[2]) + " (2)"
        if a[2] == a[1]:
            a[2] = str(a[2]) + " (2)"
        
        global card_selection
        card_selection = tk.StringVar()
        card_selection.set("First card:")

        card_s = tk.OptionMenu(deck_frm, card_selection, *a)
        card_s.config(bg=mid_green, width=15, highlightbackground=mid_green, activebackground=light_green, fg="white")
        card_s["menu"].config(activebackground=mid_green)
        card_s.grid(row=0, column=4)

        global card_selection2
        card_selection2 = tk.StringVar()
        card_selection2.set("Second card:")

        card_s2 = tk.OptionMenu(deck_frm, card_selection2, *a)
        card_s2.config(bg=mid_green, width=15, highlightbackground=mid_green, activebackground=light_green, fg="white")
        card_s2["menu"].config(activebackground=mid_green)
        card_s2.grid(row=1, column=4)

def win():
    clear_frame(guess_frm)
    clear_frame(deck_frm)
    clear_frame(hand_frm)

    tk.Label(text="YOU WIN!", master=deck_frm, bg=mid_green, fg="white", height=10).pack()

def lose():
    clear_frame(guess_frm)
    clear_frame(deck_frm)
    clear_frame(hand_frm)

    tk.Label(text="hmm, that's not correct....\nclick \"reveal\" for the answer.", master=deck_frm, bg=mid_green, fg="white", height=10).pack()

# get info from guess to determine if the guess is correct
def guess():
    # check if there are values for e1v, e1s, e2v, e2s, and p:
    if e1_val_guess.get() != "Value of evidence card 1:" and e1_suit_guess.get() != "Suit of evidence card 1:" and e2_val_guess != "Value of evidence card 2:" and e2_suit_guess != "Suit of evidence card 2:" and player_guess.get() != "Player:":
        if accuse(p1, p2 if player_guess.get() == "2" else p3, Card(int(e1_val_guess.get()), e1_suit_guess.get()), Card(int(e2_val_guess.get()), e2_suit_guess.get()), witness, ev[0], ev[1], murderer):
            win()
        else:
            lose()

# get question from dropdown values, determine answer
def interrogate():
    if vars.asked < vars.flipped and (player_inter.get() != "Player:" and card_selection.get() != "First card:" and card_selection2.get() != "Second card:" and card_selection.get() != card_selection2.get()):
        player_to_be_asked = player_inter.get()
        c1 = card_selection.get().lower().split(" ")
        c2 = card_selection2.get().lower().split(" ")

        for o in range(3):
            if c1[o] == "a":
                c1[o] = 1
            if c2[o] == "a":
                c2[o] = 1

        first_card = Card(int(c1[0]), c1[2])
        second_card = Card(int(c2[0]), c2[2])

        vars.asked = vars.asked + 1

        answer = parse(first_card, second_card, player_to_be_asked, p2 if player_to_be_asked == "2" else p3)

        tk.Label(master=deck_frm, text=f"{answer}", bg=mid_green, fg="white", font=("Arial", 15)).grid(row=4, column=0, columnspan=5)

#################### graphics/display ####################

dk_grey = "#2D2D2D"
grn_grey = "#1F2E26"
dk_green = "#07391E"
mid_green = "#09502A"
light_green = "#0A6032"

window = tk.Tk()
window['bg']=grn_grey
window.title("Deduce or Die")

# four outer frames to organize content vertically
guess_frm = tk.Frame(master=window, width=100, height=100, bg=dk_green)
deck_frm = tk.Frame(master=window, width=100, height=100, bg=mid_green)
hand_frm = tk.Frame(master=window, width=100, height=110, bg=dk_green)
menu_frm = tk.Frame(master=window, width=100, height=25, bg=grn_grey) # or dk grey?

frames = [guess_frm, deck_frm, hand_frm, menu_frm]

for frame in frames:
    frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=2.5)

# two frames within guess_frm to separate cards from guessing options
guess_cards_frm = tk.Frame(master=guess_frm, width=50, height=100, bg=dk_green)
guess_cards_frm.pack(fill=tk.BOTH, side=tk.LEFT, anchor=tk.CENTER, expand=True, padx=0, pady=0)
guess_cards_frm.columnconfigure(0, weight=1)
guess_cards_frm.columnconfigure(1, weight=1)
guess_cards_frm.columnconfigure(2, weight=1)
guess_cards_frm.rowconfigure(0, weight=1)


guess_select_frm = tk.Frame(master=guess_frm, width=50, height=100, bg=dk_green)
guess_select_frm.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=0, pady=0)

# place witness and evidence
wit = Image.open("cards/" + card_path(witness))
wit = wit.resize([int(vars.w*vars.scale_factor), int(vars.l*vars.scale_factor)], Image.ANTIALIAS)
wit_img = ImageTk.PhotoImage(wit)
witness_ = tk.Label(master=guess_cards_frm, height=vars.l*vars.scale_factor, width=vars.w*vars.scale_factor, image=wit_img, bg=dk_green)
witness_.grid(column=0)

e = Image.open("cards/card_back.png") # not getting size here keeps all cards same size
e = e.resize([int(vars.w*vars.scale_factor), int(vars.l*vars.scale_factor)], Image.ANTIALIAS)
eimg = ImageTk.PhotoImage(e)
evidence1 = tk.Label(master=guess_cards_frm, height=vars.l*vars.scale_factor, width=vars.w*vars.scale_factor, image=eimg, bg=dk_green)
evidence1.grid(row=0, column=1)
evidence2 = tk.Label(master=guess_cards_frm, height=vars.l*vars.scale_factor, width=vars.w*vars.scale_factor, image=eimg, bg=dk_green)
evidence2.grid(row=0, column=2)

# place dropdowns for guessing
val_options = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6"
]

suit_opts = [
    "clubs",
    "hearts",
    "spades"
]

# TODO: try to center dropdown; should they reset each time?
e1_val_guess = tk.StringVar()
e1_val_guess.set("Value of evidence card 1:")

e1v = tk.OptionMenu(guess_select_frm, e1_val_guess, *val_options)
e1v.config(bg=mid_green, width=30, highlightbackground=dk_green, activebackground=light_green, fg="white")
e1v["menu"].config(activebackground=mid_green)
e1v.pack()

e1_suit_guess = tk.StringVar()
e1_suit_guess.set("Suit of evidence card 1:")

e1s = tk.OptionMenu(guess_select_frm, e1_suit_guess, *suit_opts)
e1s.config(bg=mid_green, width=30, highlightbackground=dk_green, activebackground=light_green, fg="white")
e1s["menu"].config(activebackground=mid_green)
e1s.pack()

e2_val_guess = tk.StringVar()
e2_val_guess.set("Value of evidence card 2:")

e2v = tk.OptionMenu(guess_select_frm, e2_val_guess, *val_options)
e2v.config(bg=mid_green, width=30, highlightbackground=dk_green, activebackground=light_green, fg="white")
e2v["menu"].config(activebackground=mid_green)
e2v.pack()

e2_suit_guess = tk.StringVar()
e2_suit_guess.set("Suit of evidence card 2:")

e2s = tk.OptionMenu(guess_select_frm, e2_suit_guess, *suit_opts)
e2s.config(bg=mid_green, width=30, highlightbackground=dk_green, activebackground=light_green, fg="white")
e2s["menu"].config(activebackground=mid_green)
e2s.pack()

player_guess = tk.StringVar()
player_guess.set("Player:")

player = tk.OptionMenu(guess_select_frm, player_guess, *["2", "3"])
player.config(bg=mid_green, width=30, highlightbackground=dk_green, activebackground=light_green, fg="white")
player["menu"].config(activebackground=mid_green)
player.pack()

guess_btn = tk.Button(
    master=guess_select_frm,
    text="GUESS!",
    bg=light_green,
    fg="white",
    activebackground=mid_green,
    width=30,
    command=guess
)
guess_btn.pack(pady=3)

# stuff in deck frame
for i in range(5):
    deck_frm.columnconfigure(i, weight=1)
    deck_frm.rowconfigure(i, weight=1)


deck_im = Image.open("cards/card_back.png") # not getting size here keeps all cards same size
deck_im = deck_im.resize([int(vars.w*vars.scale_factor), int(vars.l*vars.scale_factor)], Image.ANTIALIAS)
deckimg = ImageTk.PhotoImage(deck_im)
deck_img = tk.Button(master=deck_frm, height=vars.l*vars.scale_factor, width=vars.w*vars.scale_factor, image=deckimg, bg=light_green, bd=0, command=flip_deck)
deck_img.grid(row=0, column=0, rowspan=4)

# player selection dropdown
player_inter = tk.StringVar()
player_inter.set("Player:")

player_q = tk.OptionMenu(deck_frm, player_inter, *["2", "3"])
player_q.config(bg=mid_green, width=15, highlightbackground=mid_green, activebackground=light_green, fg="white")
player_q["menu"].config(activebackground=mid_green)
player_q.grid(row=2, column=4)

# interrogate button
interrogate_btn = tk.Button(
    master=deck_frm,
    text="INTERROGATE",
    bg=dk_green,
    fg="white",
    activebackground=mid_green,
    highlightbackground=mid_green,
    width=17,
    padx=2,
    command=interrogate
)
interrogate_btn.grid(row=3, column=4)

# stuff in user's hand
for i in range(6):
    hand_frm.columnconfigure(i, weight=1)
hand_frm.rowconfigure(0, weight=1)
hand_frm.rowconfigure(1, weight=2)

your_hand = tk.Label(text="Y O U R   H A N D", master=hand_frm, bg=dk_green, fg="white")
your_hand.grid(row=0, column=0, columnspan=5)

# generate p1 hand as image paths
card_list = []
for t in p1:
    card_list.append("cards/" + card_path(t))

# save images globally by storing each as an entry in a list
a_img = []

for p in card_list:
    a_img.append(ImageTk.PhotoImage(Image.open(p).resize([int(vars.w*vars.scale_factor), int(vars.l*vars.scale_factor)], Image.ANTIALIAS)))
    ace = tk.Label(master=hand_frm, height=vars.l*vars.scale_factor, width=vars.w*vars.scale_factor, image=a_img[card_list.index(p)], bg=dk_green)
    ace.grid(column=card_list.index(p), row=1)


# three frames within menu_frm to organize buttons
menu_btn_frms = []
for i in range(3):
    menu_frm.columnconfigure(i, weight=1)
    menu_btn_frms.append(tk.Frame(master=menu_frm))
    menu_btn_frms[i].grid(row=0, column=i, sticky="W" if i==2 else "E" if i==0 else "")

# TODO: make this functional
new_btn = tk.Button(
    master=menu_btn_frms[0],
    text="NEW GAME",
    bg=dk_green,
    fg="white",
    activebackground=mid_green,
    command=new_game
)
new_btn.pack(side="right", anchor="w")

# button to reveal all cards
reveal_btn = tk.Button(
    master=menu_btn_frms[1],
    text="REVEAL",
    bg=dk_green,
    fg="white",
    activebackground=mid_green,
    command=reveal
)
reveal_btn.pack()

# quits window
quit_btn = tk.Button(
    master=menu_btn_frms[2],
    text="QUIT",
    bg=dk_green,
    fg="white",
    activebackground=mid_green,
    command = window.destroy
)
quit_btn.pack(side="left")

window.mainloop()