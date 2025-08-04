def check_score(score):
    if score >= 80:
        print("やったね!")
        print("次もこの調子だ")
    else:
        print("残念でした")
if __name__ == "__main__":
    score = 60
    check_score(score)
