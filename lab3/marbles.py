# Init counter variables
countRed = 0
countGreen = 0

colour = ""

while colour != "b":
    colour = str(input("Enter marble colour as R or G, [B] closes the program. >> ")).lower()

    if colour == "r": countRed += 1
    elif colour == "g": countGreen += 1
    elif colour == "b": break;

percentRed = 100 * float(countRed) / float(countRed+countGreen)
percentGreen = 100 * float(countGreen) / float(countRed + countGreen)

print(f"Number of RED marbles: {countRed}")
print(f"Number of GREEN marbles: {countGreen}")
print(f"Red marbles are {round(percentRed, 1)}% of the total.")
print(f"Green marbles are {round(percentGreen, 1)}% of the total.")