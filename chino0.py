import tkinter as tk
import tkinter.filedialog as fd
from PIL import Image, ImageTk

# 画像ファイルを数値リストに変換する
def imageToData(filename):
    # 画像を8x8のグレースケールに変換
    grayImage = Image.open(filename).convert("L")
    grayImage = grayImage.resize((8, 8), Image.Resampling.LANCZOS)

    # 数値リストを取得
    data = list(grayImage.getdata())

    # 表示用に拡大
    dispImage = ImageTk.PhotoImage(
        grayImage.resize((300, 300), resample=Image.NEAREST)
    )
    imageLabel.configure(image=dispImage)
    imageLabel.image = dispImage

    return data

# ファイルダイアログを開く
def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        data = imageToData(fpath)
        print(data)  # 数値リストを表示（デバッグ用）

# アプリのウィンドウを作る
root = tk.Tk()
root.geometry("400x400")

btn = tk.Button(root, text="ファイルを開く", command=openFile)
imageLabel = tk.Label()

btn.pack()
imageLabel.pack()

root.mainloop()

