

foods =[ "pizza","Burger","Sandwich","Chees Bun","BBQ Chicken"]
prices = [3000,1500,750,500,2500]
order_list = []
ordered_price_list = []
quantities = []
total = 0


while True:
      print("\n====Welcome to Shop====\n"
            "\n1.Menu\n"
            "2.Add to cart\n"
            "3.Bill\n"
            "4.Exit")

      main = int(input("Select your number :-"))

      if main == 1:
            print("\nNo           Item               Price\n"
                  "—————————————————————————————————————")

            for i in range(len(foods)):
                  print(f"{i + 1}            {foods[i]:<15}     {prices[i]} ")
      elif main == 2:
            food = input("Enter you want foods :-")
            order_list.append(food)
            price = foods.index(food)
            ordered_price_list.append(prices[price])
            quantity = int(input("Enter your food quantity"))
            quantities.append(quantity)

      elif main == 3:
            print("=================================="
                  "\n        WELCOME TO SHOP"
                  "\n=================================="
                  "\nProduct    Price      Qty    Total")
            for i in range(len(order_list)):
                  print(f"\n{order_list[i]}      {ordered_price_list[i]}       {quantities[i]}      {ordered_price_list[i] * quantities[i]}\n")
                  total = total + (ordered_price_list[i] * quantities[i])
            print("\n----------------------------------"
                  f"\ntotal                    Rs.{total}"
                  "\n----------------------------------"
                  "\n    Thank You | Come Again"
                  "\n==================================")
      elif main == 4:
            exit()
      else:
            print("Please Enter valid number")






