# super market bill

#ask how many products the customer wants to purches
#for each product has name, quantity, price
#need to show product total

#calculate subtotal

#if subtotal over than 20000 hav 20% , over 10000 10% , over 5000 5%

#display welcome note, each product name quantity , price , product total
#subtotal, discount , final bill amount , thank you note.


print("\n===== Welcome To Our Shop =====")

#how many product
product = int(input("\nHow many products do you want :  "))

subtotal = 0

for i in range(product):
    print("product",i + 1)


    product_name = input("Enter your product name :")
    quantity = float(input("Enter quantity :"))
    price = float(input("Enter price :"))

    product_total = quantity * price

    print("product_total :", product_total)

    subtotal = subtotal + product_total


#calculate discount

if subtotal > 200000 :
    discount = 20
elif subtotal > 10000 :
    discount = 10
elif subtotal > 5000 :
    discount = 5
else:
    discount = 0


discount_price = subtotal * discount / 100
final_bill = subtotal - discount_price

#bill

print("\n======================================")
print("  ⟪⟪⟪⟪⟪⟪ WELCOME TO OUR SHOP ⟫⟫⟫⟫⟫⟫")
print("======================================")

print("SUBTOTAL                     ", subtotal)
print("DISCOUNT                     ", discount)
print("DISCOUNT PRICE               ",discount_price)
print("TOTAL                        ", final_bill)

print("\n——————————————————————————————————————")
print("              THANK YOU")
print("——————————————————————————————————————")


















