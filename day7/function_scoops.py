def test_scope():  #naming conversation snake case
    y = 2 #function scoped variable
    global x #Modifiying global scope variable
    x = 2
    print(f"value odf z - {z}")
    print(f"value of x - {x}")


z = 3

x = 1 # global scope

test_scope()

print(x)