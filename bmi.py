#エントリーポイントを設定したbmi.py
def main():
    h = float(input("身長は何cmですか?"))/ 100.0
    w = float(input("体重は何kgですか?"))
    bmi = w / (h * h)
    print("あなたのBMI値は、",bmi,"です。")

if __name__ == "__main__":
    main()
