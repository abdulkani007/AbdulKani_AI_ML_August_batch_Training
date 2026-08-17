
# Q3 - Shopping Cart with Default & Mutable Pitfall


# Part A - Mutable Default Argument
def add_item_bug(item, cart=[]):
    cart.append(item)
    return cart


print("Part A - Mutable Default Argument Bug")
print(add_item_bug("apple"))
print(add_item_bug("banana"))
print(add_item_bug("milk", cart=["bread"]))
print(add_item_bug("eggs"))


# Part B - Correct Version
def add_item(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart


print("\nPart B - Correct Version")
print(add_item("apple"))
print(add_item("banana"))


# Part C - Create Cart
def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


# Add item to cart
def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })


# Try to modify tuple
def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError:
        print("TypeError: Tuple elements cannot be modified because tuples are immutable.")


# Calculate total
def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount_amount = total * cart["discount"] / 100
    final_total = total - discount_amount

    return final_total


# Create two independent carts
cart1 = create_cart("Aarav", discount=10)
cart2 = create_cart("Rahul", discount=5)


# Add items to first cart
add_to_cart(cart1, "Apple", 100, 2)
add_to_cart(cart1, "Milk", 50, 1)


# Add items to second cart
add_to_cart(cart2, "Bread", 40, 2)
add_to_cart(cart2, "Eggs", 60, 1)


# Display carts
print("\nPart C - Shopping Carts")

print("Cart 1:", cart1)
print("Cart 2:", cart2)

print("Cart 1 Total:", calculate_total(cart1))
print("Cart 2 Total:", calculate_total(cart2))


# Demonstrate tuple immutability
price_tuple = (100, 200, 300)

print("\nTrying to modify tuple:")
update_price(price_tuple, 500)


