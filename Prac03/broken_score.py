def getScore():
    score = float(input("Enter score: "))
    return score

def main():
    score = getScore()
    if (score < 0) or (score > 100):
        print("Invalid score")
    else:
        if score >= 50:
            print("Passable")
        if score >= 90:
            print("Excellent")
        if score < 50:
            print("Bad")
main()