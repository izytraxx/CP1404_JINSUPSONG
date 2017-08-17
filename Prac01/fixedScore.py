score = float(input("Enter score: "))
if (score < 0) or (score > 100):
    print("Invalid score")
else:
    if score >= 50:
        print("Passable")
    if score >= 90:
        print("Excellent")
    if score < 50:
        print("Bad")
