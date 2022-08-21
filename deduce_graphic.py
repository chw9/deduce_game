import tkinter as tk
from PIL import ImageTk, Image

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
menu_frm = tk.Frame(master=window, width=100, height=25, bg=grn_grey) # or dk grey?

frames = [guess_frm, deck_frm, hand_frm, menu_frm]

for frame in frames:
    frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=2.5)

menu_btn_frms = []
for i in range(3):
    menu_frm.columnconfigure(i, weight=1)
    menu_btn_frms.append(tk.Frame(master=menu_frm))
    menu_btn_frms[i].grid(row=0, column=i, sticky="W" if i==2 else "E" if i==0 else "")

new_btn = tk.Button(
    # master=menu_frm,
    master=menu_btn_frms[0],
    text="NEW GAME",
    # width=25,
    # height=5,
    bg=dk_green,
    fg="white",
    activebackground=mid_green
)
# new_btn.grid(row=0, column=0)
new_btn.pack(side="right", anchor="w")

reveal_btn = tk.Button(
    # master=menu_frm,
    master=menu_btn_frms[1],
    text="REVEAL",
    # width=25,
    # height=5,
    bg=dk_green,
    fg="white",
    activebackground=mid_green
)
# reveal_btn.pack(side="left")
# reveal_btn.grid(row=0, column=1)
reveal_btn.pack()

quit_btn = tk.Button(
    # master=menu_frm,
    master=menu_btn_frms[2],
    text="QUIT",
    # width=25,
    # height=5,
    bg=dk_green,
    fg="white",
    activebackground=mid_green
)
# quit_btn.pack(side="left")
# quit_btn.grid(row=0, column=2)
quit_btn.pack(side="left")

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