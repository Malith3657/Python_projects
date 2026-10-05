list_01 = ["Malith", 100, False, True, 20,]

print(f"\n{list_01}")

print("\n—————————————————————————")

print(f"\nFirst Element = {list_01[0]}")
print(f"\nThird Element = {list_01[2]}")
print(f"\nlast Element = {list_01[-1]}")

print("\n—————————————————————————")

list_01.append("C-Clarke")
print(f"\n{list_01}")

print("\n—————————————————————————")

list_01.insert(2,"Moratuva")
print(f"\n{list_01}")

print("\n—————————————————————————")

print(list_01.index("Malith"))


print("\n—————————————————————————")


shopping_list =["ice creem","soap","tea bags","toffee",]

for i in range(len(shopping_list)):
    print(f"{i+1}. {shopping_list[i]}")













