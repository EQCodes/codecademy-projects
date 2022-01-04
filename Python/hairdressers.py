hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#calculating average price
total_price = 0
for price in prices:
  total_price += price

average_price = total_price / len(prices)

print("Average Haircut Price: " + str(average_price))

#changing prices because average price exp.
new_prices = [price - 5 for price in prices]
print(new_prices)

#revenue calculations
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print("Total Revenue: " + str(total_revenue))

#average daily revenue
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: " + str(average_daily_revenue))

#list comprehension cuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)