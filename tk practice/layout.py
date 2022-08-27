import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("layout")

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=50, height=50, bg="orange")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=5, height=5, bg="yellow")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()