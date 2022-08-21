from re import M
import tkinter as tk
from turtle import bgcolor
from PIL import ImageTk, Image
from tblib import Frame

dk_grey = "#2D2D2D"
grn_grey = "#1F2E26"
dk_green = "#07391E"
mid_green = "#09502A"

window = tk.Tk()
window['bg']=grn_grey
window.title("Deduce or Die")

guess_frm = tk.Frame(master=window, width=100, height=100, bg=dk_green)
deck_frm = tk.Frame(master=window, width=100, height=100, bg=mid_green)
hand_frm = tk.Frame(master=window, width=100, height=100, bg=dk_green)
menu_frm = tk.Frame(master=window, width=100, height=50, bg=grn_grey) # or dk grey?

frames = [guess_frm, deck_frm, hand_frm, menu_frm]

for frame in frames:
    frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=2.5)

# guess_frm = tk.Frame(master=window, borderwidth=1, bg=dk_green)
# deck_frm = tk.Frame(master=window, bg=mid_green)
# hand_frm = tk.Frame(master=window, bg=dk_green)
# menu_frm = tk.Frame(master=window, bg=grn_grey) # or dk grey?

# frames = [guess_frm, deck_frm, hand_frm, menu_frm]

# for i in range(len(frames)):
#     window.rowconfigure(i, weight=1, minsize=150)
#     frames[i].grid(row=i, sticky='NESW', padx=5, pady=5)
#     # label = tk.Label(master=frames[i], text=f"Row {i}")
#     # label.pack(padx=5, pady=5)

window.mainloop()