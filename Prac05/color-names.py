from operator import itemgetter

COLORS = {"AliceBlue": "#f0f8ff", "beige": "#f5f5dc", "black": "#000000", "brown": "#a52a2a", "coral": "#ff7f50", "DimGray": "#696969", "firebrick": "#b22222", "gray": "#bebebe", "lavender": "#e6e6fa", "khaki": "#f0e68c"}
COLORS = {k.lower(): v for k, v in COLORS.items()}

color_input = input("Enter the color: ").lower()
while not color_input in COLORS:
    print("Invalid color")
    color_input = input("Enter the color: ").lower()

print(COLORS[color_input])




