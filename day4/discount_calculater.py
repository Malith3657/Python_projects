

is_member = input("\nAre you member ? (yes/no)") == "yes"
is_using_coupon = input("\nDo you have coupon ? (yes/no)") == "yes"
total_bill = int(input("\nyour total bill - "))
have_vegetables = input("\nAre you buying vegitables (yes/no)") == "yes"

if is_member and not is_using_coupon and total_bill > 5000 and not have_vegetables :
    print("\nDo you have 20% Discount")
    discount = total_bill * 0.20
    print(f"TOTAL =  {total_bill - discount}" )
else:
    print("\nNo Discount")