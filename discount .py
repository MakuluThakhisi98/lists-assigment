def calculate_discount(price, discount_percent):
    """Calculate the final price after applying discount if >= 20%."""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price  # No discount applied

# Get user input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Output
if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
else:
    print(f"No discount applied. Price remains: {final_price:.2f}")