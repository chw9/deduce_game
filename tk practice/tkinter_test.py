import tkinter as tk
from PIL import ImageTk, Image

bg_color = "#4A4A4A"
fg_color = "#191C2A"
abg_c = "#797979" # active background (when button is clicked)

window = tk.Tk()
frame = tk.Frame()
frame.pack()

label = tk.Label(
    text="Deduce or Die (solo practice)",
    foreground=fg_color,
    background=bg_color,
    width=25,
)
label.pack()

cards_button = tk.Button(
    text="Deal three question cards",
    width=25,
    height=5,
    bg=bg_color,
    fg=fg_color,
    activebackground=abg_c
)
cards_button.pack()

accusation_button = tk.Button(
    text="Make an accusation",
    width=25,
    height=5,
    bg=bg_color,
    fg=fg_color,
    activebackground=abg_c
)
accusation_button.pack()

quit_button = tk.Button(
    text="Quit game",
    width=25,
    height=5,
    bg=bg_color,
    fg=fg_color,
    activebackground=abg_c
)
quit_button.pack()

input_label = tk.Label(text="Enter your guess for one evidence card: ")
first_guess = tk.Entry()
first_guess.insert(0, "guess: ")
input_label.pack()
first_guess.pack()
g1 = first_guess.get()

input_label2 = tk.Label(text="Enter your guess for the other evidence card: ")
second_guess = tk.Entry()
input_label2.pack()
second_guess.pack()
g2 = second_guess.get()

print(g1)
print(g2)

ace_ = Image.open("../cards/ace_of_spades.png")
w = ace_.size[0] # don't actually know which is length and which is width but pretty sure this is right?
l = ace_.size[1]
ace_ = ace_.resize([int(w*.3), int(l*.3)], Image.ANTIALIAS)
ace_spades = ImageTk.PhotoImage(ace_)
# img = ace_spades.subsample(1,2)

# a_label = tk.Label
# tk.Label(text = 'card', font = ('Times', 32)).pack(side = 'top', padx = 10, pady = 10)
tk.Button(image = ace_spades).pack(side = "bottom", pady = 10) #padx = 400

window.mainloop()
