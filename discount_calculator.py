def calculate_discount(price, discount_percent):

 if discount_percent >= 20:
   discount = price * (discount_percent / 100) 
   final_price = price - discount
   return final_price
 else:
    return price
    
#prompting the user for input

original_price = float(input("Enter the original price of the item: "))
discount_percent= float(input("Enter the dicount percent of the item: "))

final_price = calculate_discount(original_price, discount_percent)

print(final_price)
