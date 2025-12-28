"""Flipkart Project Mini"""

#User details

name = str(input("Enter your name: " ))
product_name = str(input("Product Name: " ))
quantity = int(input("Enter the quantity: " ))
price=float(input("Enter the price per item: " ))
print("CUSTOMER DETAILS")
print(f"{name.capitalize()}\n{product_name}\n{quantity}\n{price}")

#Operations

convert = product_name.upper()
print(convert)
total = quantity * price
print("Total cost= ", total)
#Discount
if total >= 5000:
    discount = total * 0.10
else:
    discount = total * 0.05
#final amt
final_amount = total - discount
#even or not
even = int(final_amount) % 2 ==0

#printing
print("INVOICE DETAILS")
print("PRODUCT NAME: ", convert, "\nTOTAL: ",round(total), "\nDISCOUNT APPLIED: ",round(discount), "\nFINAL AMOUNT: ",round(final_amount), "\nEVEN: ", even)

