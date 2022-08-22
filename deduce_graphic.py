# Caroline Winakur 2022
# Based on Deduce or Die game http://www.thegamesjournal.com/rules/DeduceOrDie.shtml

import tkinter as tk
from PIL import ImageTk, Image
from card import *

m = Image.open("cards/ace_of_clubs.png")
w, l = m.size 
scale_factor = .25

def game_start():
    shuffle(deck)
    shuffle(q_deck_remaining)

game_start()
p1, p2, p3, ev, witness, murderer = deal(deck)

############### button commands ###############
# TODO: move this to a separate file called button_commands.py then 
# from button_commands import new_game, reveal, .......    ??

# clear all widgets in frame
def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()

# remove these frames
def del_frames():
    guess_frm.destroy()
    deck_frm.destroy()
    hand_frm.destroy()

# TODO: make it so this reveals the evidence cards, murderer card, and player who had it
def reveal():
    clear_frame(guess_frm)
    clear_frame(deck_frm)
    clear_frame(hand_frm)

    # TODO: create method to display each players' hand and the evidence cards.
    global j
    j = []
    display_cards(guess_frm, p2, 2, j)
    global k
    k = []
    display_cards(deck_frm, p3, 3, k)
    global l
    l = []
    ev_wit = []
    for n in ev:
        ev_wit.append(n)
    ev_wit.append(witness)
    display_cards(hand_frm, ev_wit, 0, l)

# TODO: deal with this later. maybe need to segment functionality out to diff files/functions. idk bro
def new_game():
    clear_frame(guess_frm)
    clear_frame(deck_frm)
    clear_frame(hand_frm)

def card_path(card_name):
    return str(card_name).replace(" ", "_").replace("A", "ace") + ".png"

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
        
        # TODO: figure out wtf is going on here
        path = "cards/" + card_name
        hand_img = Image.open(path).resize([int(w*scale_factor), int(l*scale_factor)], Image.ANTIALIAS)
        list_var.append(ImageTk.PhotoImage(hand_img))
        card_im = tk.Label(master=frame, height=l*scale_factor, width=w*scale_factor, image=list_var[len(list_var)-1], bg=(mid_green if p == 3 else dk_green))
        card_im.grid(row=1, column=player.index(c))
    
    frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=2.5)

def flip_deck():
    a = show_q_cards(q_deck_remaining)
    global i
    i = []
    for card in a:
        card_name = card_path(card)

        path = "cards/" + card_name
        flip_img = Image.open(path)
        flip_img = flip_img.resize([int(w*scale_factor), int(l*scale_factor)], Image.ANTIALIAS)
        i.append(ImageTk.PhotoImage(flip_img))
        # needs to be a button eventually
        card_im = tk.Button(master=deck_frm, bd=0, height=l*scale_factor, width=w*scale_factor, image=i[len(i)-1], bg=mid_green)
        card_im.grid(row=0, column=(a.index(card) + 1), rowspan=2)


###############################################

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
w, l = m.size 
scale_factor = .25
wit = wit.resize([int(w*scale_factor), int(l*scale_factor)], Image.ANTIALIAS)
wit_img = ImageTk.PhotoImage(wit)
witness_ = tk.Label(master=guess_cards_frm, height=l*scale_factor, width=w*scale_factor, image=wit_img, bg=dk_green)
witness_.grid(column=0)

e = Image.open("cards/card_back.png") # not getting size here keeps all cards same size
e = e.resize([int(w*scale_factor), int(l*scale_factor)], Image.ANTIALIAS)
eimg = ImageTk.PhotoImage(e)
evidence1 = tk.Label(master=guess_cards_frm, height=l*scale_factor, width=w*scale_factor, image=eimg, bg=dk_green)
evidence1.grid(row=0, column=1)
evidence2 = tk.Label(master=guess_cards_frm, height=l*scale_factor, width=w*scale_factor, image=eimg, bg=dk_green)
evidence2.grid(row=0, column=2)

# place dropdowns for guessing
val_options = [
    "A",
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

# TODO: decide about additional labels, try to center dropdown
e1_val_guess = tk.StringVar()
e1_val_guess.set("Value of evidence card 1:")

e1v = tk.OptionMenu(guess_select_frm, e1_val_guess, *val_options)
e1v.config(bg=mid_green, width=30, highlightbackground=dk_green, activebackground=light_green, fg="white")
# e1v["menu"].config(bg=light_green, activebackground=mid_green)
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
)
guess_btn.pack(pady=3)

# stuff in deck frame
for i in range(5):
    deck_frm.columnconfigure(i, weight=1)
deck_frm.rowconfigure(0, weight=1)
deck_frm.rowconfigure(1, weight=1)

deck_im = Image.open("cards/card_back.png") # not getting size here keeps all cards same size
deck_im = deck_im.resize([int(w*scale_factor), int(l*scale_factor)], Image.ANTIALIAS)
deckimg = ImageTk.PhotoImage(deck_im)
deck_img = tk.Button(master=deck_frm, height=l*scale_factor, width=w*scale_factor, image=deckimg, bg=light_green, bd=0, command=flip_deck)
deck_img.grid(row=0, column=0, rowspan=2)

# player selection dropdown
player_inter = tk.StringVar()
player_inter.set("Player:")

player_q = tk.OptionMenu(deck_frm, player_inter, *["2", "3"])
player_q.config(bg=mid_green, width=10, highlightbackground=dk_green, activebackground=light_green, fg="white")
player_q["menu"].config(activebackground=mid_green)
player_q.grid(row=0, column=4)

# interrogate button
interrogate_btn = tk.Button(
    master=deck_frm,
    text="INTERROGATE",
    bg=dk_green,
    fg="white",
    activebackground=mid_green,
    width=15,
    # command=interrogate
)
interrogate_btn.grid(row=1, column=4)

# stuff in your hand
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
    a_img.append(ImageTk.PhotoImage(Image.open(p).resize([int(w*scale_factor), int(l*scale_factor)], Image.ANTIALIAS)))
    ace = tk.Label(master=hand_frm, height=l*scale_factor, width=w*scale_factor, image=a_img[card_list.index(p)], bg=dk_green)
    ace.grid(column=card_list.index(p), row=1)


# three frames within menu_frm to organize buttons
menu_btn_frms = []
for i in range(3):
    menu_frm.columnconfigure(i, weight=1)
    menu_btn_frms.append(tk.Frame(master=menu_frm))
    menu_btn_frms[i].grid(row=0, column=i, sticky="W" if i==2 else "E" if i==0 else "")

new_btn = tk.Button(
    master=menu_btn_frms[0],
    text="NEW GAME",
    bg=dk_green,
    fg="white",
    activebackground=mid_green,
    command=new_game
)
new_btn.pack(side="right", anchor="w")

reveal_btn = tk.Button(
    master=menu_btn_frms[1],
    text="REVEAL",
    bg=dk_green,
    fg="white",
    activebackground=mid_green,
    command=reveal
)
reveal_btn.pack()

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