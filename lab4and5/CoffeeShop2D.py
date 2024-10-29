coffeeSales = [
    [5000, 3000, 3500, 3700, 3750, 4950, 6000],
    [2000, 1000,  500, 1500, 1700, 1900, 2000],
    [4000, 4050, 4070, 5000, 4050, 3700, 4000],
    [5500, 5420, 4000, 3800, 3500, 4050, 6000],
    [6000, 5000, 4000, 4050, 4075, 5000, 6500]
]

# Output the following
#   - total sales for the week
#   - total sales for each shop
#   - total sales for each dotw
#   - the shop with the best sales
#   - the dotw with best sales
#   - highest recorded sales

def sales_for_week(salesList):
    total_sales_week = 0
    total_per_shop = []
    total_sales_daily = [0] * len(salesList[0])
    highest = 0
    shop_best_sales = 0
    day_bestsales = 0

    for i in range(len(salesList)):
        shop_sales = sum(salesList[i])
        total_sales_per_shop.append(shop_sales)
        total_sales_week += shop_sales
        
        # Check for highest sales in the shop
        if shop_sales > total_sales_per_shop[shop_best_sales]:
            shop_best_sales = i
    
        # Calculate total sales per day
        for j in range(len(salesList[i])):
            total_sales_per_day[j] += salesList[i][j]
            # Check for highest recorded sales
            if salesList[i][j] > highest_sales:
                highest_sales = salesList[i][j]

    # Check for the best day of the week
    day_best_sales = total_sales_per_day.index(max(total_sales_per_day))

    # Output results
    print("Total sales for the week:", total_sales_week)
    print("Total sales for each shop:", total_sales_per_shop)
    print("Total sales for each day of the week:", total_sales_per_day)
    print("Shop with the best sales (Shop index):", shop_best_sales)
    print("Day of the week with best sales (Day index):", day_best_sales)
    print("Highest recorded sales:", highest_sales)

# Call the function
sales_for_week(coffeeSales)