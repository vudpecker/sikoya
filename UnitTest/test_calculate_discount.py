


def calculate_discount(price, discount_rate):
    if not isinstance(price, (int, float)):
        raise TypeError("Price must be a number")
    if not isinstance(discount_rate, (int, float)):
        raise TypeError("Discount rate must be a number")
    if price < 0 or discount_rate < 0:
        raise ValueError(
            "Price and discount rate must be non-negative"
        )
    discount = price * discount_rate
    return price - discount


num, div = input("Enter the number and diviser: ").split()
res = calculate_discount(int(num),int(div))
#a, b = input("Enter two values: ").split()
#print("First number is {} and second number is {}".format(a, b))