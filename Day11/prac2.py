class CheckOutError(Exception):
    pass

def add_to_cart(*prices):
    total_price = 0
    for price in prices:
        if price<0:
            raise CheckOutError("Invalid price:", price)
        total_price += price

    if total_price ==0:
        raise CheckOutError('Cart is empty. Please add items to cart before checkout.')
    
    return total_price
try:
    price = add_to_cart(1,2,46,78,56)
    # price = add_to_cart(0,0,0)
except CheckOutError as e:
    print("Error:",e)
else:
    print(price)