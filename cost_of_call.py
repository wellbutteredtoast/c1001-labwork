# RATES:
# < 99km  -> $0.12 for the first 5m, $0.10/m after
# < 199km -> $0.15 for the first 5m, $0.13/m after
# > 200km -> $0.18/m regardless of length

def main():
    distance = float(input("Enter the distance (km) for the call: "))
    minutes = int(input("Enter the number of minutes spent on call: "))

    if distance <= 99.0:
        callCost = computeCostUnder100k(minutes)
    elif distance <= 199.0:
        callCost = computeCostUnder200k(minutes)
    else:
        callCost = computeCostPast200k(minutes)

    printCost(callCost)

# List firstFiveMinutes is used in place of nesting loops or using huge if statements
def computeCostUnder100k(minutes: int) -> float:
    firstFiveMins = [0, 1, 2, 3, 4]
    finalCost = 0
    for j in range(minutes):
        if j in firstFiveMins:
            finalCost += 0.12
        else:
            finalCost += 0.10

    return finalCost

def computeCostUnder200k(minutes: int) -> float:
    firstFiveMins = [0, 1, 2, 3, 4]
    finalCost = 0
    for k in range(minutes):
        if k in firstFiveMins:
            finalCost += 0.15
        else:
            finalCost += 0.13

    return finalCost


def computeCostPast200k(minutes: int) -> float:
    finalCost = 0
    for n in range(minutes):
        finalCost += 0.18

    return finalCost

def printCost(cost: float):
    print("The cost of your call is $%.2f" % cost)

main()