import tkinter as tk
import random

def omikuji():
    kuji = ["大吉","中吉","小吉","凶"]
    lbl.configure(text=random.choice(kuji))

root = tk.Tk()
root = geometry("200x100")

lbl = tk.Label(text="おみくじアプリ")
btn = tk.Button(text="おみくじ!", command = omikuji)


lbl.pack()
btn.pack()
tk.mainloop()

