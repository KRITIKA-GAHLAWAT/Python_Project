
# Part A - Mutable Default Argument Bug

def add_item_bug(item, cart=[]):
    cart.append(item)
    return cart


print("Part A:")
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


print("\nPart B:")
print(add_item("apple"))
print(add_item("banana"))


# Part C - Shopping Cart

def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })


def update_price(price_tuple, new_price):
    try:
        price_tuple[1] = new_price
    except TypeError:
        print("TypeError: Tuples are immutable and cannot be changed.")


def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount_amount = total * cart["discount"] / 100
    final_total = total - discount_amount

    return final_total


# Two independent carts

cart1 = create_cart("Aarav", 10)
cart2 = create_cart("Priya", 5)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 1000, 2)

add_to_cart(cart2, "Phone", 30000, 1)
add_to_cart(cart2, "Headphones", 2000, 2)

print("\nCart 1:")
print(cart1)

print("\nCart 2:")
print(cart2)

print("\nCart 1 Total:", calculate_total(cart1))
print("Cart 2 Total:", calculate_total(cart2))


# Tuple immutability demonstration

price_tuple = ("Laptop", 50000)
update_price(price_tuple, 45000)


# Discussion Points

# 1. discount=0 is safe because integers are immutable.
# cart=[] is dangerous because lists are mutable and can be shared
# between function calls.

# 2. Rebinding means assigning a variable to a new object.
# Mutating means changing the existing object.

# 3. Mutable: list, dict, set
# Immutable: tuple, str, int

# 4. Yes, changes to a list can reflect outside the function because
# the list is mutable and the function receives the same list object.
