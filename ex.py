cart = []
input_cart = input("Enter the prices of items you have added to the cart (separated by spaces): ")
# Split the input string and convert each value to float
prices = [float(price) for price in input_cart.split()]
cart.extend(prices)

print("Your cart contains:", cart)

#Filtering below 500rs
items_above_500=list(filter(lambda x:x>=500,cart))
# filtering above 500 rs
items_below_500=list(filter(lambda x:x<=500,cart))
#calculating 18% tax on items above or equal to 500
map_cart=list(map(lambda x:(x*18/100),items_above_500))




from functools import reduce
# Summing up toatl tax
def t_tax(x,y):
    return x+y
total_tax=reduce(t_tax,map_cart)

# summing bill of items below 500
def total_b(x,y):
    return x+y
total_bi=reduce(total_b,items_below_500)

# summing bill of items above 500
def total_u(x,y):
    return x+y
total_up=reduce(total_u,items_above_500)

# printing toatl bill
print(f"YOur total bill with 18% tax on items above 500 is {total_up+total_tax+total_bi}Rs/-")