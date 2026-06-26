user_input = int(input("Enter a number: "))


odds_under_input = [num for num in range(user_input) if num % 2 != 0]


general_odds = [num for num in range(1, 20, 2)]

print("Odd numbers under input:", odds_under_input)
print("General odd numbers:", general_odds)



fruits = ["apple", "banana", "cherry", "dragonfruit"]

# Convert the first letter of every element to capital
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Original fruits:", fruits)
print("Updated fruits:", capitalized_fruits)
