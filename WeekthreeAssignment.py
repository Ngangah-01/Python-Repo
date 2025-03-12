def calculate_discount(price,discount_percent):
    
    if discount_percent >= 0.2:
        discount = price * discount_percent
        price = price - discount
        print(f"The final price of the item after discount is Ksh: {price}")
    else:
        print(f"Discount percentage is too low. No discount applied. Pay Ksh {price}")

price = float(input("Enter the original Price of the Item: "))
discount_percent = float(input("Enter the discount percentage of the item: "))/100

calculate_discount(price, discount_percent)
