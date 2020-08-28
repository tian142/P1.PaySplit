# this script takes the user's inputs of meal price, tip paid, and the number of people splitting the meal to calculate the cost each individual has to pay

# prompts the user to enter meal price:
meal_price = int(input('Please enter the price of your meal: '))
# tax variable set to CA average of 7.5%
tax = 7.5
# promots the user to enter tip paid:
tip_paid = int(input('Please enter your tip paid: '))
# calculate how much tax is paid
tax_paid = meal_price * (tax/100)
# calculate how much the entire meal cost, store in total_meal_price variable
total_meal_price = meal_price + tax_paid + tip_paid
# prompts user to enter the number of people splitting the bill:
split_between = int(
    input('Please enter the total number of people splitting this meal: '))
# calculates price per person:
price_per_person = total_meal_price / split_between
# constructs result string: with the summary of the meal:
result = f"The meal was: ${meal_price}. \nWith Tax of {tax}%, tax paid: ${tax_paid} \nTips paid: ${tip_paid} \nGross cost of meal: {total_meal_price}\nSplitting between {split_between} people, each person pays: ${round(price_per_person, 2)}"
# creates a line in the terminal for better visuals
line_break = "-------------------------------------------------------"
# prints the result with line_breaks
print(line_break + "\n" + result + "\n" + line_break)
