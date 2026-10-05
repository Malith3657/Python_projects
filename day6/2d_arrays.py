two_dim_arr = [['x','x','x'],
               ['x','x','x'],
               ['x','x','x']]

print(len(two_dim_arr))

print(two_dim_arr[0])

print(two_dim_arr[0][1])

two_dim_arr[0] [0] = "Y"
print(two_dim_arr[0][0])

print(two_dim_arr)

print("======================")

for i in two_dim_arr:
    print(i)
    for l in i:
        print(l)