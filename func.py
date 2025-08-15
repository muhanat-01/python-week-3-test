# function to calculate discount
def calculate_discount(price, discount_percent):
    # check if discount is 20% or more
    if discount_percent >= 20:
        # apply discount
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        # no discount applied
        return price

# ask the user for input
price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

# call the function
final_price = calculate_discount(price, discount)

# print the result
print("The final price is:", final_price)
