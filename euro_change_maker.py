

# Taking input from the user
total_euro_cents = int(input('Enter number of euro cents: '))

# Calculation
coins_2 = total_euro_cents // 200
coins_1 = total_euro_cents % 200 // 100
cent_50 = total_euro_cents % 200 % 100 // 50
cent_20 = total_euro_cents % 200 % 100 % 50 // 20
cent_10 = total_euro_cents % 200 % 100 % 50 % 20 // 10
cent_5 = total_euro_cents % 200 % 100 % 50 % 20 % 10 // 5
cent_2 = total_euro_cents % 200 % 100 % 50 % 20 % 10 % 5 // 2
cent_1 = total_euro_cents % 200 % 100 % 50 % 20 % 10 % 5 % 2 // 1

# Show the results
print(f"2 euro coins: {coins_2}")
print(f"1 euro coins: {coins_1}")
print(f"50 cent coins: {cent_50}")
print(f"20 cent coins: {cent_20}")
print(f"10 cent coins: {cent_10}")
print(f"5 cent coins: {cent_5}")
print(f"2 cent coins: {cent_2}")
print(f"1 cent coins: {cent_1}")