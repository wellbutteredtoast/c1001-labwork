steps = int(input("Enter the number of steps: "))

MAX_TWIRLS = 5

for i in range(1, steps + 1):
    twirl_count = 0
    
    while twirl_count <= MAX_TWIRLS:
        if twirl_count == 0:
            twirl_count += 1

        print(f"Step: {i} -- Twirl: {twirl_count}")
        twirl_count += 1

    print("")