import tkinter as tk
import random

def omikuji():
    kuji = ["大吉","中吉","小吉","凶"]
    lbl2.configure(text=random.choice(kuji))

root = tk.Tk()
root.title("おみくじアプリ")
root. geometry("400x100")

btn = tk.Button(text="おみくじ!", command = omikuji)
lbl2 = tk.Label(text="ここに結果が表示されるよ",font=("",16))


btn.pack()
lbl2.pack()
tk.mainloop()

