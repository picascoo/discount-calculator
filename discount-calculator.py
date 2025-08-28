def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    elif discount_percent < 20:
        return price
    else:
        return price  # fallback, though logically redundant

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percentage)

    if discount_percentage >= 20:
        print(f"Discount applied. The final price is: ${final_price:.2f}")
    elif discount_percentage < 20:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
    else:
        print("Invalid discount percentage.")
except ValueError:
    print("Please enter valid numbers for price and discount.")