product = input("Product : ")
Price = float(input("Price: "))
Quantity = int(input("Quantity: "))




print("=====RECEIPT=====")
print(f"{product} x {Quantity}")
print(f"Total: {Price*Quantity:.2f} THB.-")
print(f"================")


discount = int(input("Discont: "))


print()
print(f"{product} x {Quantity}")
print(f"Discount : {discount}%")
print(f"Total : {Price*Quantity*((100-discount)/100):.2f} THB")
print("===================")

